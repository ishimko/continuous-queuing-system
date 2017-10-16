from math import isfinite
from collections import namedtuple

from simulator.deivce import Device

Result = namedtuple('Result', ['all_up', 'all_down', 'one_up'])

class Simulator:
    def __init__(self, erlang_shape, devices_count, break_intensity, repair_intensity):
        self._devices_count = devices_count
        self._break_intensity = break_intensity
        self._repair_intensity = repair_intensity
        self._erlang_shape = erlang_shape

    def run_simulation(self, iterations_count):
        device_constructor = lambda: Device(
            self._erlang_shape,
            self._break_intensity,
            self._repair_intensity
        )
        devices = [device_constructor() for _ in range(self._devices_count)]

        time = 0
        all_time = 0
        all_up = 0
        all_down = 0
        one_up = 0

        for _ in range(iterations_count):
            time = min((device._need_time for device in devices if isfinite(device._need_time)), default=1)

            if all((not device.broken for device in devices)):
                all_up += time
            elif all((device.broken for device in devices)):
                all_down += time
            else:
                one_up += time

            for device in devices:
                device.refresh(time)
            all_time += time

        return Result(
            all_up=all_up / all_time,
            all_down=all_down / all_time,
            one_up=one_up / all_time
        )
