
# coding=utf-8

string_1 = 'Testing order {1} {0}'
print(string_1.format(0,1))

string_2 = 'Testing order {} {} {i}'
print(string_2.format(0,1,i=2))

string_3 = 'Testing type float {0:.3f}'
print(string_3.format(15))


string_4 = 'Padding space: {0:15d}'
print(string_4.format(15))


string_5 = 'Padding right: {0:>10}'
print(string_5.format(15))


string_5 = 'Padding left: {0:<10}'
print(string_5.format(15))

string_5 = 'Padding center: {0:^10}'
print(string_5.format(15))

string_5 = 'Padding center fill *: {0:*^10}'
print(string_5.format(15))