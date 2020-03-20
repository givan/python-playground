#!/usr/bin/python -tt


#  messing around with dict
# read up on dictoinaries at: https://docs.python.org/2/tutorial/datastructures.html#dictionaries

def create_dict(key_value_tuples):
    d = {}

    for (key, value) in key_value_tuples:
        d[key] = value

    return d

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def main():
    print 'create dictionary'
    dict1 = create_dict([('a', 'alpha'), ('b', 'beta'), ('o', 'omega')])
    test('b' in dict1, True)
    test(dict1['a'], 'alpha')
    test(dict1.get('x'), None)

    dict2 = {"1": 111, "2": 2222, "3": 3333}
    test(str(type(dict2)), "<type 'dict'>")

    dict3 = dict([('a', 'alpha'), ('b', 'beta'),
                  ('o', 'omega-1'), ('o', 'omega')])
    print(dict3)
    test(dict3, dict1)

    # only works when the keys are strings
    dict4 = dict(one=111, two=2222, three=3333)
    test(str(type(dict4)), "<type 'dict'>")
    test(dict4.get('one'), 111)

    dict5 = {x: x ** 2 for x in (2, 4, 6)}
    print(dict5)
    test(dict5.get(6), 36)

    print
    print 'get all keys'
    print(dict1.keys())

    for k in sorted(dict1.keys()):
        print 'key:', k, '->', dict1[k]

    for (key, val) in dict1.items():
        print 'key:', key, '->', val


if __name__ == '__main__':
    main()
