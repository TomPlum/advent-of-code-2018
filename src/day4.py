from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from reader import read


def part1(data: [str]) -> int:
    records = get_guard_records(data)
    sorted_by_sleep = sorted(records.items(), key=lambda r: r[1].total_time_slept(), reverse=True)
    most_sleep = sorted_by_sleep[0]
    minutes_slept = most_sleep[1].minutes_slept()
    most_slept_minute = max(set(minutes_slept), key=minutes_slept.count)
    most_slept_guard_id = most_sleep[0]
    return most_slept_minute * most_slept_guard_id


def part2(data: [str]) -> int:
    guard_data = get_guard_records(data)

    #for i, d in guard_data.items():
        #print(f"{i}: {d}")

    all_minutes = flatten(map(lambda r: r.minutes_slept(), guard_data.values()))
    most_freq_minute = max(set(all_minutes), key=all_minutes.count)
    print(f"Most Frequent Minute: {most_freq_minute}")

    guard_slept_most = None
    most_minutes = 0

    for id, record in guard_data.items():
        minutes_slept = record.minutes_slept()
        occurrences = minutes_slept.count(most_freq_minute)
        if occurrences > most_minutes:
            most_minutes = occurrences
            guard_slept_most = id

    return guard_slept_most * most_freq_minute


def solution_part_1() -> int:
    return part1(read(4).toString())


def solution_part_2() -> int:
    return part2(read(4).toString())  # 90317 too high


def get_guard_records(data: [str]):
    data = sorted(data, key=lambda s: (datetime.strptime(s.split("] ")[0][1:], "%Y-%m-%d %H:%M") - datetime.utcfromtimestamp(0)).total_seconds() * 1000.0)

    for d in data:
        print(d)

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

    records = {}

    for id, shifts in guard_data.items():
        records[id] = GuardRecord(shifts)

    return records


def flatten(arr):
    return [item for sublist in arr for item in sublist]


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


@dataclass(frozen=True)
class GuardShift:
    """A shift for a guard consisting of the times they begin their shift, fall asleep and wake up."""
    """[1518-11-01 00:00] Guard #10 begins shift"""
    """[1518-11-01 00:05] falls asleep"""
    """[1518-11-01 00:25] wakes up"""

    id: int
    events: [ShiftEvent]

    def sleep_duration(self):
        sleep = 0
        awake = 0
        last = None
        for e in self.events:
            if e.type == EventType.SLEEP:
                awake += e.minutes_difference(last)
            elif e.type == EventType.WAKE:
                sleep += e.minutes_difference(last)

            last = e

        return sleep

    def minutes_asleep(self) -> [int]:
        minutes_asleep = []
        last = None
        for e in self.events:
            if e.type == EventType.WAKE:
                #print(f"Found Wake Event: {e}")
                start = last.get_date()
                end = e.get_date()
                #print(f"Originally fell asleep at: {last}")
                minute = start.minute
                #print(f"Fell asleep on minute: {start.minute}")
                #print(f"Should stop counting at: {end.minute}")
                finished = False
                while not finished:
                    minutes_asleep.append(minute)
                    if minute == end.minute:
                        finished = True
                    elif minute == 59:
                        minute = 0

                    minute = minute + 1

            last = e
        return minutes_asleep

    def __repr__(self):
        return "\n" + "\n".join(e.value for e in self.events)


@dataclass(frozen=True)
class GuardRecord:
    shifts: [GuardShift]

    def minutes_slept(self) -> [int]:
        return flatten(map(lambda s: s.minutes_asleep(), self.shifts))

    def total_time_slept(self) -> int:
        return sum(map(lambda s: s.sleep_duration(), self.shifts))
