#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  if (len(s) < 3): return s

  result = ''

  if (s[-3:] == 'ing'):
    result = '%sly' % (s)
  else:
    result = '%sing' % (s)

  return result


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  first_not_idx = s.find('not')
  first_bad_idx = s.find('bad')

  if (first_not_idx > -1 and first_bad_idx > -1 and first_not_idx < first_bad_idx):
    s = s[:first_not_idx] + 'good' + s[first_bad_idx + len('bad'):]

  return s

def split_string(s):
  str_len = len(s)
  if (str_len % 2 == 0):
    return s[:str_len / 2], s[str_len / 2:]
  else:
    return s[:str_len / 2 + 1], s[str_len / 2 + 1:]

def split_string_test():
  test(split_string('abcd'), ('ab', 'cd'))
  test(split_string('abcde'), ('abc', 'de'))

# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  first_str_split = split_string(a)
  second_str_split = split_string(b)

  return first_str_split[0] + second_str_split[0] + first_str_split[1] + second_str_split[1]


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print 'verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print 'not_bad'
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

  print
  print 'split_string'
  split_string_test()

if __name__ == '__main__':
  main()
