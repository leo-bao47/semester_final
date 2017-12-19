import sys

data = open("bikes.csv", "r")
lines = data.readlines()

list_of_travel = []
list_of_wheel = []
list_of_price = []

def list_travel(list_of_travel, travel):
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")

		if info[5] == travel:
			list_of_travel.append(info[1])

	return list_of_travel

print list_travel(list_of_travel, "200")

def list_wheel(list_of_wheel, wheel):
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")

		if info[3] == wheel:
			list_of_wheel.append(info[1])

	return list_of_wheel

print list_wheel(list_of_wheel, "29")

def list_price_range(list_of_price, price):
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")

		if info[4] == price:
			list_of_price.append(info[1])

	return list_of_price

print list_price_range(list_of_price, "4000")

