from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from collections import Counter

from reader import read
from utility import flatten


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

    guard_slept_most = None
    most_freq_minute = 0
    most_occurrences = 0

    for id, record in guard_data.items():
        minutes_slept = record.minutes_slept()
        occurrences = Counter(minutes_slept).most_common(1)[0]
        if occurrences[1] > most_occurrences:
            most_occurrences = occurrences[1]
            guard_slept_most = id
            most_freq_minute = occurrences[0]

    return guard_slept_most * most_freq_minute


def solution_part_1() -> int:
    return part1(read(4).toString())


def solution_part_2() -> int:
    return part2(read(4).toString())  # 90317 and 21127 too high


def get_guard_records(data: [str]):
    data = sorted(data, key=lambda s: (datetime.strptime(s.split("] ")[0][1:], "%Y-%m-%d %H:%M") - datetime.utcfromtimestamp(0)).total_seconds() * 1000.0)

    guard_data = {}

    parsed = []
    parsed_current = []
    last_was_begin = False
    for i, d in enumerate(list(data)):
        if i != 0 and "begins shift" in d:
            if not last_was_begin:
                parsed.append(list(parsed_current))

            last_was_begin = True
            parsed_current.clear()
            parsed_current.append(d)
        else:
            last_was_begin = False
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
                start = last.get_date()
                end = e.get_date()
                minute = start.minute
                finished = False
                while not finished:
                    minutes_asleep.append(minute)
                    if minute == end.minute - 1:  # Guards count as awake on the minute they wake up
                        finished = True
                    elif minute == 60:
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
