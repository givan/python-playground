#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
    count = 0

    for word in words:
      if (len(word) >= 2 and 
          word[0] == word[-1]):
        count += 1

    return count

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    x_arr = []
    other_arr = []

    for word in words:
      if (word[0] == 'x'): x_arr.append(word)
      else: other_arr.append(word)

    result = sorted(x_arr) + sorted(other_arr)
    return result

# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.

def last_elem_tuple(tuple):
  return tuple[-1]

def sort_last(tuples):
    result = sorted(tuples, key=last_elem_tuple)
    return result

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

    # the last elem in a sequence

def Last(x):
    return x[-1]

# Calls the above functions with interesting inputs.
def main():

    print 'messing around with arrays'
    a = [2, 3, 4]
    first = a.pop(0)
    test(first, 2)

    a.append(5)
    last = a[-1]
    test(last, 5)

    del a
    # print a # Error - local variable 'a' referenced before assignment
    a = [1, 3, 4]
    b = a
    del a
    print b  # that works just fine

    c = [3, 2, 1, 6]
    c = sorted(c)
    print(c)

    c = sorted(c, reverse=True)
    print(c)

    # sorted by using key sort function
    a = ['aaaa', 'bb', 'c', 'dddd']
    print(sorted(a, key=len))  # sort by string len
    # > ['c', 'bb', 'aaaa', 'dddd']

    # now sort using the last character in each string
    print(sorted(a, key=Last))
    # > ['aaaa', 'bb', 'c', 'dddd']

    # join() and split()
    joined_list = ':'.join(a)
    print(joined_list)
    # > 'aaaa:bb:c:dddd'

    split_str = joined_list.split(':')
    print(split_str)
    # > ['aaaa', 'bb', 'c', 'dddd']

    a = [i for i in range(7)]
    print(a)
    # > [0, 1, 2, 3, 4, 5, 6]

    for x in range(7, 12): a.append(x)
    print(a)
    # > [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    # Tuples - immutable
    three_tuple = (1, 2, 3)
    print(three_tuple)
    print(len(three_tuple)) # 3
    # three_tuple[2] = "ddd" -> error - tuple is immutable

    # sort by one thing and then sort by second thing
    a = [(1, 'b'), (2, 'a'), (1, 'a')]
    print(sorted(a)) 
    # > [(1, 'a'), (1, 'b'), (2, 'a')]

    (x, y) = (1, 2)
    print(x) # x == 1
    print(y) # y == 2

    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print
    print 'sort_last'
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()
