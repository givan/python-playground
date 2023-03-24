import requests
import sys

# response = requests.get('https://httpbin.org/ip')

# origin_ip = response.json()['origin']
# print(f'Your ip is: {origin_ip}')

# Excercises from: https://developers.google.com/edu/python/strings
text = (
    "%d little pigs come out or I'll %s, and I'll %s, or I'll %s your house down"
    % ( 3, "huff", "puff", "blow")
    )
print(text)
print(len(text))

print(f"{'hello':>10} world")

# unicode strings
asciiStr = 'this is my unicode string'
print('%s - ASCII string len: %d' % (asciiStr, len(asciiStr)))

unicodeStr = u'this is my unicode string'
print('%s - Unicode string len: %d' % (unicodeStr, len(unicodeStr)))

ustring = u'A unicode \u018e string \xf1'
print(ustring)

s = ustring.encode('utf-8')
print(s)

pile = "\N{PILE OF POO}"
print(pile)
print(type(pile))

pile2 = u"\U0001F4A9"
print(pile2)
print(type(pile2))

print(sys.getdefaultencoding())

my_unicode = u"Hi \u2119\u01b4\u2602\u210c\xf8\u1f24"
print(my_unicode)
print(len(my_unicode)) # 9

my_utf8 = my_unicode.encode('utf-8')
print(len(my_utf8))  # 19
my_orig_unicode = my_utf8.decode('utf-8')
print(len(my_orig_unicode)) # 9

my_ascii = "hello google"
print(my_ascii[-3:]) # get the last 3 chars
print(my_ascii[:-3]) # get all chars up to the last 3 (not inclusive)