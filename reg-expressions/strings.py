import re

str = "Spain is a beautiful place to visit. Spain is a beautiful country to live in."

print('Spain' in str)           # True

a = re.search('Spain', str)
print(a)  # <re.Match object; span=(0, 5), match='Spain'> or None
print(a.span())  # (0, 5) Index of the first and last character 


pattern = re.compile('Spain')
a = pattern.search(str)  # <re.Match object; span=(0, 5), match='Spain'> or None
b = pattern.findall(str)  # ['Spain', 'Spain'] or []
c = pattern.fullmatch(str)  # None
d = pattern.match(str)  # <re.Match object; span=(0, 5), match='Spain'> or None
e = pattern.split(str)  # ['', ' is a beautiful place to visit. ', ' is a beautiful country to live in.']
d = pattern.sub('Germany', str)  # Germany is a beautiful place to visit. Germany is a beautiful country to live in.


print(d)