
def compare_lists(list_price_range, list_wheel, list_travel, price, travel, wheel):
	price_travel = []
	for i in list_price_range(list_of_price, price), list_travel(list_of_travel, travel):
		if list_price_range(list_of_price, price)[i] == list_travel(list_of_travel, travel)[i]:
			price_travel += i

	final_list = []
	for i in price_travel, list_wheel(list_of_wheel, wheel):
		if price_travel[i] == list_wheel(list_of_wheel, wheel)[i]:
			final_list += i

	return final_list

print compare_lists(list_price_range, list_wheel, list_travel, "3800", "90", "29")



