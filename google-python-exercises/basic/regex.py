#!/usr/bin/python -tt

import re

def find(pat, text):
    match = re.search(pat, text)
    if match: print match.group()
    else: print 'not found'

if __name__ == "__main__":

    # . -> any single char
    # \w -> any word char
    # \s -> any whitespace char
    # \S -> any NON whitespace char
    # + -> at least one
    # * -> zero or more

    find('iig', 'called piiig')
    find('iigs', 'called piiig')
    find('..g', 'called piiig') # will match any 2 cars and g
    find('c\.l', 'c.lled piig') #
    find(r'c.l', 'c.lled piig') # using raw strings with 'r' prefix so you d'nt have to escape the .
    find(r':\w\w\w', 'blah :cat blah blah')
    find(r'\d\d\d', 'blah :123xxxx  ')
    find(r'\d\s\d\s\d', '1 2 3')
    find(r'\d\s\d\s\d', '1 2    3') # not found
    find(r'\d\s\d\s+\d', '1 2    3')
    find(r':\w+', 'blah blah :kitten blah blah blah')
    find(r'\w+@\w+', 'blah blah :nick.p@gmail.com blah blah') # -> p@gmail
    find(r'[\w.]+@\w+', 'blah blah :nick.p@gmail.com blah blah') # nick.p@gmail
    find(r'[\w.]+@[\w.]+', 'blah blah :nick.p@gmail.com blah blah') # nick.p@gmail.com

    m = re.search(r'([\w.]+)@([\w.]+)', 'blah blah :nick.p@gmail.com blah blah')
    print(m.group()) # nick.p@gmail.com
    print(m.group(1)) # nick.p
    print(m.group(2)) # gmail.com

    m = re.findall(r'([\w.]+)@([\w.]+)', 'blah blah :nick.p@gmail.com blah blah foo@bar')
    print(m) # [('nick.p', 'gmail.com'), ('foo', 'bar')]

    m = re.findall(r'[\w.]+@[\w.]+', 'blah blah :nick.p@gmail.com blah blah foo@bar')
    print(m) # ['nick.p@gmail.com', 'foo@bar']

    print(dir(re)) # explore the symbols in a module

    m = re.findall(r'[\w.]+@[\w.]+', 'blah blah :nick.p@gmail.com blah blah foo@bar', re.IGNORECASE)
    print(m) # ['nick.p@gmail.com', 'foo@bar']
