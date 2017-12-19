import sys

data = open("bikes.csv", "r")
lines = data.readlines()

list_of_bikes = []

def list_travel(list_of_bikes, travel):
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")

		if info[6] == (travel +- 10):
			list_of_bikes.append(info[1])
			list_of_bikes.append(info[2])

	return list_of_bikes

print list_travel(list_of_bikes, "100")

def list_wheel(list_of_bikes, wheel):
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")

		if info[3] == wheel:
			list_of_bikes.append(info[1])
			list_of_bikes.append(info[2])

	return list_of_bikes
