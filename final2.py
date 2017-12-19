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
		else:
			list_of_travel += 'a'
	return list_of_travel

def list_wheel(list_of_wheel, wheel):
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")

		if info[3] == wheel:
			list_of_wheel.append(info[1])
		else:
			list_of_wheel += 'b'

	return list_of_wheel


def list_price_range(list_of_price, price):
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")

		if info[4] == price:
			list_of_price.append(info[1])
		else:
			list_of_price += 'c'

	return list_of_price

def determine_bikes(price, travel, wheel):
	p_list = list_price_range(list_of_price, price)
	t_list = list_travel(list_of_travel, travel)
	w_list = list_wheel(list_of_wheel, wheel)

	a = p_list
	b = t_list
	c = w_list


	def compare_lists():
		new_list = []
		for element in a:
			if element in b:
				new_list.append(element)
		final_list = []
		for element in new_list:
			if element in c:
				final_list.append(element)

		return final_list

	return compare_lists()