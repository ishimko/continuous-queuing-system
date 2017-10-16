from simulator.simulator import Simulator


DEVICES_COUNT = 2
ITERATIONS_COUNT = 100000
BREAK_INTENSITY = 0.1
REPAIR_INTESITY = 12


def main():
    simulator = Simulator(DEVICES_COUNT, BREAK_INTENSITY, REPAIR_INTESITY)
    print(simulator.run_simulation(ITERATIONS_COUNT))


if __name__ == '__main__':
    main()
