import math

Q_LIMIT = 100
BUSY = 1
IDLE = 0

next_event_type, num_custs_delayed, num_delays_required, num_events, num_in_q, server_status = 0, 0, 0, 2, 0, IDLE
area_num_in_q, area_server_status, mean_interarrival, mean_service, sim_time, total_of_delays = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
time_arrival = [0.0] * (Q_LIMIT + 1)
time_last_event, time_next_event = 0.0, [0.0] * 3

MODLUS = 2147483647
MULT1 = 24112
MULT2 = 26143

zrng = [1, 1973272912, 281629770, 20006270, 1280689831, 2096730329, 1933576050, 913566091, 246780520, 1363774876,
        604901985, 1511192140, 1259851944, 824064364, 150493284, 242708531, 75253171, 1964472944, 1202299975,
        233217322, 1911216000, 726370533, 403498145, 993232223, 1103205531, 762430696, 1922803170, 1385516923,
        76271663, 413682397, 726466604, 336157058, 1432650381, 1120463904, 595778810, 877722890, 1046574445,
        68911991, 2088367019, 748545416, 622401386, 2122378830, 640690903, 1774806513, 2132545692, 2079249579,
        78130110, 852776735, 1187867272, 1351423507, 1645973084, 1997049139, 922510944, 2045512870, 898585771,
        243649545, 1004818771, 773686062, 403188473, 372279877, 1901633463, 498067494, 2087759558, 493157915,
        597104727, 1530940798, 1814496276, 536444882, 1663153658, 855503735, 67784357, 1432404475, 619691088,
        119025595, 880802310, 176192644, 1116780070, 277854671, 1366580350, 1142483975, 2026948561, 1053920743,
        786262391, 1792203830, 1494667770, 1923011392, 1433700034, 1244184613, 1147297105, 539712780, 1545929719,
        190641742, 1645390429, 264907697, 620389253, 1502074852, 927711160, 364849192, 2049576050, 638580085, 547070247]

def lcgrand(stream):
    global zrng
    zi, lowprd, hi31 = zrng[stream], 0, 0
    lowprd = (zi & 65535) * MULT1
    hi31 = (zi >> 16) * MULT1 + (lowprd >> 16)
    zi = ((lowprd & 65535) - MODLUS) + ((hi31 & 32767) << 16) + (hi31 >> 15)
    if zi < 0:
        zi += MODLUS
    lowprd = (zi & 65535) * MULT2
    hi31 = (zi >> 16) * MULT2 + (lowprd >> 16)
    zi = ((lowprd & 65535) - MODLUS) + ((hi31 & 32767) << 16) + (hi31 >> 15)
    if zi < 0:
        zi += MODLUS
    zrng[stream] = zi
    return (zi >> 7 | 1) / 16777216.0

def lcgrandst(zset, stream):
    global zrng
    zrng[stream] = zset

def lcgrandgt(stream):
    global zrng
    return zrng[stream]

def expon(mean):
    return -mean * math.log(lcgrand(1))

def initialize():
    global sim_time, server_status, num_in_q, time_last_event, num_custs_delayed, total_of_delays, area_num_in_q, area_server_status, time_next_event
    sim_time = 0.0
    server_status = IDLE
    num_in_q = 0
    time_last_event = 0.0
    num_custs_delayed = 0
    total_of_delays = 0.0
    area_num_in_q = 0.0
    area_server_status = 0.0
    time_next_event[1] = sim_time + expon(mean_interarrival)
    time_next_event[2] = 1.0e+30

def timing():
    global next_event_type, sim_time
    min_time_next_event = 1.0e+29
    next_event_type = 0
    for i in range(1, num_events + 1):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i
    if next_event_type == 0:
        print("\nEvent list empty at time", sim_time)
        exit(1)
    sim_time = min_time_next_event

def arrive():
    global num_in_q, server_status, num_custs_delayed, total_of_delays
    delay = 0.0
    time_next_event[1] = sim_time + expon(mean_interarrival)
    if server_status == BUSY:
        num_in_q += 1
        if num_in_q > Q_LIMIT:
            print("\nOverflow of the array time_arrival at time", sim_time)
            exit(2)
        time_arrival[num_in_q] = sim_time
    else:
        delay = 0.0
        total_of_delays += delay
        num_custs_delayed += 1
        server_status = BUSY
        time_next_event[2] = sim_time + expon(mean_service)

def depart():
    global num_in_q, server_status, num_custs_delayed, total_of_delays
    delay = 0.0
    if num_in_q == 0:
        server_status = IDLE
        time_next_event[2] = 1.0e+30
    else:
        num_in_q -= 1
        delay = sim_time - time_arrival[1]
        total_of_delays += delay
        num_custs_delayed += 1
        time_next_event[2] = sim_time + expon(mean_service)
        for i in range(1, num_in_q + 1):
            time_arrival[i] = time_arrival[i + 1]

def report():
    global area_num_in_q, area_server_status, num_custs_delayed, sim_time
    print("\n\nSingle-server queueing system\n")
    print("Mean interarrival time{:11.3f} minutes".format(mean_interarrival))
    print("Mean service time{:16.3f} minutes".format(mean_service))
    print("Number of customers{:14d}".format(num_delays_required))
    if num_custs_delayed > 0:
        print("\n\nAverage delay in queue{:11.3f} minutes".format(total_of_delays / num_custs_delayed))
    else:
        print("\n\nAverage delay in queue: N/A (No customers have been delayed)")
    if sim_time > 0:
        print("Average number in queue{:10.3f}".format(area_num_in_q / sim_time))
        print("Server utilization{:15.3f}".format(area_server_status / sim_time))
        print("Time simulation ended{:15.3f} minutes".format(sim_time))
    else:
        print("Average number in queue: N/A (Simulation has not started)")
        print("Server utilization: N/A (Simulation has not started)")
        print("Time simulation ended: N/A (Simulation has not started)")

def update_time_avg_stats():
    global area_num_in_q, area_server_status, time_last_event
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time
    area_num_in_q += num_in_q * time_since_last_event
    area_server_status += server_status * time_since_last_event

def main():
    global mean_interarrival, mean_service, num_delays_required
    mean_interarrival = 1.0
    mean_service = 0.5
    num_delays_required = 1000
    initialize()
    while num_custs_delayed < num_delays_required:
        timing()
        update_time_avg_stats()
        if next_event_type == 1:
            arrive()
        elif next_event_type == 2:
            depart()
    report()

if __name__ == "__main__":
    main()
