from math import log
from random import random


class Device:
    ERLANG_SHAPE = 2

    def __init__(self, break_intensity, repair_intensity):
        self._break_intensity = break_intensity
        self._repair_intensity = repair_intensity
        self._need_time = self._get_working_time()
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
        return Device._get_random_time_erlang(self._break_intensity, 1)

    def _get_repair_time(self):
        return Device._get_random_time_erlang(self._repair_intensity)

    @staticmethod
    def _get_random_time_erlang(intensity, k=ERLANG_SHAPE):
        return -1 / intensity * sum((log(random()) for _ in range(k)))
