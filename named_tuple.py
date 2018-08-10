
# coding=utf-8

from collections import namedtuple

City = namedtuple('City','name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.name)
print(tokyo[1])
print(tokyo._fields)
LatLong = namedtuple('LatLong','lat long')
dehli_data =('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
print(dehli_data)
dehli = City._make(dehli_data)
print(dehli)
print(dehli._asdict())