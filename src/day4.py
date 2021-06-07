from dataclasses import dataclass
from datetime import datetime
from enum import Enum


def part1(data: [str]) -> int:
    guard_data = {}

    parsed = []
    parsed_current = []
    for i, d in enumerate(list(data)):
        if i != 0 and "begins shift" in d:
            parsed.append(list(parsed_current))
            parsed_current.clear()
            parsed_current.append(d)
        else:
            parsed_current.append(d)
            if i == len(data) - 1:
                parsed.append(list(parsed_current))

    events = []

    for shift in list(parsed):
        start = shift.pop(0)
        events.append(ShiftEvent(EventType.START, start))
        guard_id = int(start.split(" #")[1].split(" ")[0].strip())

        for event in shift:
            if "falls asleep" in event:
                events.append(ShiftEvent(EventType.SLEEP, event))
            elif "wakes up" in event:
                events.append(ShiftEvent(EventType.WAKE, event))

        existing = guard_data.get(guard_id, [])
        existing.append(GuardShift(guard_id, events))
        guard_data[guard_id] = existing
        events = []

    time = {}

    for id, shifts in guard_data.items():
        for shift in shifts:
            print(shift)
        cumulative = sum(map(lambda s: s.sleep_duration(), shifts))
        time[id] = cumulative

    print(time)

    return 0


class EventType(Enum):
    START = 0
    SLEEP = 1
    WAKE = 2


@dataclass(frozen=True)
class ShiftEvent:
    type: EventType
    value: str

    def get_date(self) -> datetime:
        return datetime.strptime(self.value.split("] ")[0][1:], "%Y-%m-%d %H:%M")

    def minutes_difference(self, other: 'ShiftEvent') -> int:
        return abs(self.get_date() - other.get_date()).total_seconds() / 60.0



@dataclass
class GuardShift:
    """A shift for a guard consisting of the times they begin their shift, fall asleep and wake up."""
    """[1518-11-01 00:00] Guard #10 begins shift"""
    """[1518-11-01 00:05] falls asleep"""
    """[1518-11-01 00:25] wakes up"""

    def __init__(self, id: int, events: [ShiftEvent]):
        self.id = id
        self.events = events

    def sleep_duration(self):
        sleep = 0
        awake = 0
        last = None
        for e in self.events:
            if e.type == EventType.START:
                s = ""
                #print(f"[{self.id}] Start: {current}")
            elif e.type == EventType.SLEEP:
                #print(f"[{self.id}] Sleep: {current}")
                awake += e.minutes_difference(last)
                #print(f"Stayed awake for {(current - last).total_seconds() / 60.0} minutes")
            elif e.type == EventType.WAKE:
                #print(f"[{self.id}] Wake: {current}")
                sleep += e.minutes_difference(last)
                #print(f"Slept for {(current - last).total_seconds() / 60.0} minutes")
            last = e
            #print(f"Total Sleep Time: {sleep}\n")

        return sleep

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return "\n" + "\n".join(e.value for e in self.events)

@dataclass
class GuardRecord:
    def __int__(self, shifts: [GuardShift]):
        self.shifts = shifts