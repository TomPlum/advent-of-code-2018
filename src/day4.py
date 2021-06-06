from dataclasses import dataclass
from datetime import datetime
from functools import reduce


def part1(data: [str]) -> int:
    shifts = []

    guard_data = {}
    guard_id = 0

    asleep = []
    wake = []
    begin = ""

    for d in list(data):
        if "begins shift" in d:
            if guard_id != 0:
                existing = guard_data.get(guard_id, [])
                existing.append(GuardShift(guard_id, begin, asleep, wake))
                guard_data[guard_id] = existing
            begin = d
            guard_id = int(d.split(" #")[1].split(" ")[0].strip())
            asleep.clear()
            wake.clear()
        elif "falls asleep" in d:
            asleep.append(d)
        elif "wakes up" in d:
            wake.append(d)

    print(guard_data)

    time = {}

    for id, shifts in guard_data.items():
        cumulative = sum(map(lambda s: s.sleep_duration(),  shifts))
        time[id] = cumulative

    print(time)

    return 0


@dataclass
class GuardShift:
    """A shift for a guard consisting of the times they begin their shift, fall asleep and wake up."""
    """[1518-11-01 00:00] Guard #10 begins shift"""
    """[1518-11-01 00:05] falls asleep"""
    """[1518-11-01 00:25] wakes up"""

    def __init__(self, id: int, begin: str, sleep: [str], wake: [str]):
        # self.id = begin.split(" #")[1].split(" ")[0].strip()
        self.id = id
        self.begin = self.__parse_date(begin)
        self.sleep = self.parse_time(sleep)
        self.wake = self.parse_time(wake)

    def add_sleep_time(self, entry: str):
        self.sleep.append(self.parse_time(entry)[0])

    def add_awake_time(self, entry: str):
        self.wake.append(self.parse_time(entry)[0])

    def parse_time(self, value: [str]) -> [datetime]:
        return list(map(lambda w: self.__parse_date(w), value))

    def __parse_date(self, string: str) -> datetime:
        return datetime.strptime(string.split("] ")[0][1:], "%Y-%m-%d %H:%M")

    def sleep_duration(self):
        time = list(zip(self.sleep, self.wake))
        sleep = 0
        awake = 0
        for i, t in enumerate(time):
            if i == 0 or i % 2 == 0:
                sleep += (t[1] - t[0]).total_seconds() / 60.0
            else:
                awake += (t[1] - t[0]).total_seconds() / 60.0
            print(f"Slept from {t[0]} to {t[1]}")
        return sleep

    def __eq__(self, other):
        return self.id == other.id

