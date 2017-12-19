import sys

data = open("bikes.csv", "r")
lines = data.readlines()

list_of_bikes = []

def list_travel(list_of_bikes, travel):
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")

		if info[5] == travel:
			list_of_bikes.append(info[0])
			list_of_bikes.append(info[1])

	return list_of_bikes

print list_travel(list_of_bikes, "90")

def list_wheel(list_of_bikes, wheel):
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")

		if info[3] == wheel:
			list_of_bikes.append(info[0])
			list_of_bikes.append(info[1])

	return list_of_bikes

def list_price_range(list_of_bikes, price):
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")

		if info[4] == (price +- 500):
			list_of_bikes.append(info[0])
			list_of_bikes.append(info[1])

	return list_of_bikes