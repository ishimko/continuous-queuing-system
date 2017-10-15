from math import log
from random import random
from collections import namedtuple


DEVICES_COUNT = 2
ERLANG_SHAPE = 2
ITERATIONS_COUNT = 100000
BREAK_INTENSITY = 0.1
REPAIR_INTESITY = 12


Result = namedtuple('Result', ['all_up', 'all_down', 'one_up'])


class Device:
    def __init__(self, break_intensity, repair_intensity):
        self.break_intensity = break_intensity
        self.repair_intensity = repair_intensity
        self.need_time = get_random_time_exponential(self.break_intensity)
        self.broken = False

    def refresh(self, time):
        if self.broken:
            self._try_repair(time)
        else:
            self._try_break(time)

    def _try_repair(self, time):
        if time >= self.need_time:
            self.need_time = get_random_time_exponential(self.break_intensity)
            self.broken = False
        else:
            self.need_time -= time

    def _try_break(self, time):
        if time >= self.need_time:
            self.need_time = get_random_time_erlang(self.repair_intensity)
            self.broken = True
        else:
            self.need_time -= time


def get_random_time_exponential(intensity):
    return get_random_time_erlang(intensity, 1)


def get_random_time_erlang(intensity, k=ERLANG_SHAPE):
    return - 1 / intensity * sum((log(random()) for _ in range(k)))


def simulate(break_intensity, repair_intensity, count):
    devices = [Device(break_intensity, repair_intensity) for _ in range(DEVICES_COUNT)]

    time = 0
    all_time = 0
    all_up = 0
    all_down = 0
    one_up = 0

    for _ in range(0, count):
        if all((not device.broken for device in devices)):
            all_up += time
        elif all((device.broken for device in devices)):
            all_down += time
        else:
            one_up += time

        for device in devices:
            device.refresh(time)

        time = min((device.need_time for device in devices))
        all_time += time

    return Result(
        all_up=all_up / all_time,
        all_down=all_down / all_time,
        one_up=one_up / all_time
    )


def main():
    print(simulate(BREAK_INTENSITY, REPAIR_INTESITY, ITERATIONS_COUNT))


if __name__ == '__main__':
    main()
