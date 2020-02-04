
"""
A restaurant recommendation system.

Here are some example dictionaries.  These correspond to the information in
restaurants_small.txt.

Restaurant name to rating:
# dict of {str: int}
{'Georgie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 71,
 'Mexican Grill': 85,
 'Deep Fried Everything': 52}

Price to list of restaurant names:
# dict of {str, list of str}
{'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georgie Porgie'],
 '$$$$': []}

Cuisine to list of restaurant names:
# dict of {str, list of str}
{'Canadian': ['Georgie Porgie'],
 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
 'Malaysian': ['Queen St. Cafe'],
 'Thai': ['Queen St. Cafe'],
 'Chinese': ['Dumplings R Us'],
 'Mexican': ['Mexican Grill']}

With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we
would produce this list:

[[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
"""

# The file containing the restaurant data.
FILENAME = 'restaurants.txt'


def recommend(file, price, cuisines_list):
	"""(file open for reading, str, list of str) -> list of [int, str] list

	Find restaurants in file that are priced according to price and that are
	tagged with any of the items in cuisines_list.  Return a list of lists of
	the form [rating%, restaurant name], sorted by rating%.
	"""

	# Read the file and build the data structures.
	# - a dict of {restaurant name: rating%}
	# - a dict of {price: list of restaurant names}
	# - a dict of {cusine: list of restaurant names}
	name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)


	# Look for price or cuisines first?
	# Price: look up the list of restaurant names for the requested price.
	names_matching_price = price_to_names[price]

	# Now we have a list of restaurants in the right price range.
	# Need a new list of restaurants that serve one of the cuisines.
	names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)

	# Now we have a list of restaurants that are in the right price range and serve the requested cuisine.
	# Need to look at ratings and sort this list.
	result = build_rating_list(name_to_rating, names_final)
	print(result)

	# We're done!  Return that sorted list.
	return result

def build_rating_list(name_to_rating, names_final):
	""" (dict of {str: int}, list of str) -> list of list of [int, str]

	Return a list of [rating%, restaurant name], sorted by rating%

	>>> name_to_rating = {'Georgie Porgie': 87,
	 'Queen St. Cafe': 82,
	 'Dumplings R Us': 71,
	 'Mexican Grill': 85,
	 'Deep Fried Everything': 52}
	>>> names = ['Queen St. Cafe', 'Dumplings R Us']
	[[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
	"""

	result = []
	for i in names_final:
		result.append([name_to_rating[i], i])

	result.sort(reverse=True)

	return result

def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
	""" (list of str, dict of {str: list of str}, list of str) -> list of str

	>>> names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
	>>> cuis = 'Canadian': ['Georgie Porgie'],
	 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
	 'Malaysian': ['Queen St. Cafe'],
	 'Thai': ['Queen St. Cafe'],
	 'Chinese': ['Dumplings R Us'],
	 'Mexican': ['Mexican Grill']}
	>>> cuisines = ['Chinese', 'Thai']
		>>> filter_by_cuisine(names, cuis, cuisines)
		['Queen St. Cafe', 'Dumplings R Us']
		"""

	names_final = []
	for i in cuisines_list:
		if i in cuisine_to_names.keys():
			names_final = names_final + cuisine_to_names[i]

	names_final = set(names_final)
	names_matching_price = set(names_matching_price)
	names_final = list(names_final.intersection(names_matching_price))

	return names_final


def read_restaurants(file):
	""" (file) -> (dict, dict, dict)

	Return a tuple of three dictionaries based on the information in the file:

	- a dict of {restaurant name: rating%}
	- a dict of {price: list of restaurant names}
	- a dict of {cusine: list of restaurant names}
	"""

	name_to_rating = {}
	price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
	cuisine_to_names = {}


	f=open(file, "r")
	lines_per_rest = 5

	fl =f.readlines()

	rest = {
	'name': '',
	'rating': 0,
	'price': '',
	'cuisine': []
	}

	for count, line in enumerate(fl):
		line = line.rstrip()

		if count%lines_per_rest == 0:
			rest['name'] = line
		elif count%lines_per_rest == 1:
			rest['rating'] = int(line[:-1])
		elif count%lines_per_rest == 2:
			rest['price'] = line
		elif count%lines_per_rest == 3:
			rest['cuisine'] = line.split(",")

			name_to_rating[rest['name']] = rest['rating']
			price_to_names[rest['price']].append(rest['name'])
			for ac_cui in rest['cuisine']:
				if ac_cui in cuisine_to_names.keys():
					cuisine_to_names[ac_cui].append(rest['name'])
				else:
					cuisine_to_names[ac_cui] = [rest['name']]

	return name_to_rating, price_to_names, cuisine_to_names


recommend(FILENAME, '$', ['Thai', 'Chinese', 'Mexican', 'Pub Food'])