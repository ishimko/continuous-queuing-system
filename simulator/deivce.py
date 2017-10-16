from math import log
from random import random


class Device:
    def __init__(self, erlang_shape, break_intensity, repair_intensity):
        self._break_intensity = break_intensity
        self._repair_intensity = repair_intensity
        self._need_time = self._get_working_time()
        self._erlang_shape = erlang_shape
        self.broken = False

    def refresh(self, time):
        if self.broken:
            self._try_repair(time)
        else:
            self._try_break(time)

    def _try_repair(self, time):
        if time >= self._need_time:
            self._need_time = self._get_working_time()
            self.broken = False
        else:
            self._need_time -= time

    def _try_break(self, time):
        if time >= self._need_time:
            self._need_time = self._get_repair_time()
            self.broken = True
        else:
            self._need_time -= time

    def _get_working_time(self):
        return self._get_random_time_erlang(self._break_intensity)

    def _get_repair_time(self):
        return self._get_random_time_erlang(self._repair_intensity, self._erlang_shape)

    def _get_random_time_erlang(self, intensity, k=1):
        if intensity != 0:
            return -1 / intensity * sum((log(random()) for _ in range(k)))
        else:
            return float('+inf')
