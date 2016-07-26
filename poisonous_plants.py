def calculateDays(plants):
    global days
    originalPlants = plants[:]
    counter = []
    i = 1
    while i < len(plants):
        if plants[i] > plants[i - 1]:
            counter.append(i)
        i += 1
    if counter:
        while counter:
            plants.pop(counter.pop())
    if len(originalPlants) == len(plants):
        return days
    else:
        days += 1
        calculateDays(plants)

n = raw_input().strip()
plants = []
plants = raw_input().strip().split(' ')

days = 0
plants = map(int, plants)
calculateDays(plants)
print days
