
def is_palindrome_v1(s):

	''' str -> bool

	Return True if s is a palindrome
	Inputs:
	s = (String) String to be checked as a palindrome
	Outputs:
	is_palindrome = (Boolean) True if s is palindrome

	Examples:
	>>> is_palindrome_alg1('noon')
	True
	>>> is_palindrome_alg1('denter')
	False
	'''

	# Compare reversed string 
	if s_rev == s[::-1]:
		return True
	else:
		return False


def is_palindrome_v2(s):

	''' str -> bool

	Return True if s is a palindrome
	Inputs:
	s = (String) String to be checked as a palindrome
	Outputs:
	is_palindrome = (Boolean) True if s is palindrome

	Examples:
	>>> is_palindrome_alg1('noon')
	True
	>>> is_palindrome_alg1('denter')
	False
	'''
	# Get length of string and mid character
	len_s = len(s)
	mid_s = len_s // 2

	# Grab first half of the string Grab second half of the string reversed and compare them
	if s[:mid_s] == s[:(len_s-mid_s-1):-1]:
		return True
	else:
		return False


def is_palindrome_v3(s):

	''' str -> bool

	Return True if s is a palindrome
	Inputs:
	s = (String) String to be checked as a palindrome
	Outputs:
	is_palindrome = (Boolean) True if s is palindrome

	Examples:
	>>> is_palindrome_alg1('noon')
	True
	>>> is_palindrome_alg1('denter')
	False
	'''
	# Get length of string 
	len_s = len(s)
	for i in range(len_s//2):
		if s[i] != s[len_s-i-1]:
			return False

	return True
