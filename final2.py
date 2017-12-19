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

def list_wheel(list_of_wheel, wheel):
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")

		if info[3] == wheel:
			list_of_wheel.append(info[1])

	return list_of_wheel


def list_price_range(list_of_price, price):
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")

		if info[4] == price:
			list_of_price.append(info[1])

	return list_of_price

list_price_range(list_of_price, "3800")
list_wheel(list_of_wheel, "29")
list_travel(list_of_travel, "90")

def compare_lists():
	price_travel_compare = []
	for i in list_of_price:
		if list_of_price(i) == list_of_travel(i):
			price_travel_compare += i

	final_list = []
	for i in price_travel_compare:
		if list_of_wheel(i) == price_travel_compare(i):
			final_list += i

	return final_list

print compare_lists()

"""def bike_finder(list_price_range, list_wheel, list_travel, price, travel, wheel):
	print "These are the bikes that match your price range:"
	print list_price_range(list_of_price, price)
	print "------"
	print "These are the bikes that match your travel requirements:"
	print list_travel(list_of_travel, travel)
	print "------"
	print "These are the bikes that match your desired wheel size:"
	print list_wheel(list_of_wheel, wheel)
	print "------"

bike_finder(list_price_range, list_wheel, list_travel, "3800", "90", "29")"""