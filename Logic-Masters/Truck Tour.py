def truckTour(petrolpumps):
    start, cum = 0, 0
    for i in range(len(petrolpumps)):
        petrol, distance = petrolpumps[i]
        cum += petrol - distance
        if cum < 0:
            start = i + 1
            cum = 0
    return start
