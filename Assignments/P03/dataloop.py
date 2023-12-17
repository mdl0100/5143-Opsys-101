from main import *
algorithms = ["RR", "FCFS", "PB"]
cpus = [1,2,3,4]
ios = [2, 4, 6]
ts = [3, 5, 7, 9]
data = ["SEven.dat", "SIOInt.dat", "SCPUInt.dat"]

# algorithms = ["PB"]
# cpus = [4]
# ios = [6]
# ts = [9]
# data = ["SEven.dat", "SIOInt.dat", "SCPUInt.dat"]


for filename in data:
    for algorithm in algorithms:
        for cpu in cpus:
            for io in ios:
                if algorithm == "RR":
                    for t in ts:
                        main(filename, cpu, io, algorithm, t, 0, f'{filename[:2]}_{algorithm}_{cpu}_{io}_{t}.csv')
                else:
                    main(filename, cpu, io, algorithm, 1, 0, f'{filename[:2]}_{algorithm}_{cpu}_{io}.csv')

