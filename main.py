import sys

from simulator.simulator import Simulator
from simulator.reader import read_positive_float


DEVICES_COUNT = 2
ITERATIONS_COUNT = 100000
DEFAULT_BREAK_INTENSITY = 0.1
DEFAULT_REPAIR_TIME = 4
ERLANG_SHAPE = 2


def mean_time_to_erlang_intensity(mean_in_hours):
    HOURS_IN_DAY = 24
    return ERLANG_SHAPE * HOURS_IN_DAY / mean_in_hours


def read_repair_intensity():
    return read_positive_float('Среднее значение времени ремонта (в часах)')


def read_break_intensity():
    return read_positive_float('Интенсивность потока неисправностей (ед./сут.)')


def use_default():
    return len(sys.argv) == 2 and sys.argv[1] == '-d'


def print_results(simulation_results):
    print('S0 (оба узла работают) = {}'.format(simulation_results.all_up))
    print('S01 (один узел работает, второй ремонтируется) = {}'.format(simulation_results.one_up))
    print('S11 (оба узла ремонтируются) = {}'.format(simulation_results.all_down))


def main():
    if use_default():
        break_intensity = DEFAULT_BREAK_INTENSITY
        repair_time = DEFAULT_REPAIR_TIME
    else:
        break_intensity = read_break_intensity()
        repair_time = read_repair_intensity()
    repair_intensity = mean_time_to_erlang_intensity(repair_time)
    simulator = Simulator(DEVICES_COUNT, ERLANG_SHAPE, break_intensity, repair_intensity)
    simulation_results = simulator.run_simulation(ITERATIONS_COUNT)
    print_results(simulation_results)


if __name__ == '__main__':
    main()
