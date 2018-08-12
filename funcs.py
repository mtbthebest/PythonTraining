
# coding=utf-8

from functools import reduce, partial
from operator import add, methodcaller,mul

def factorial(n):
    """:return n!"""
    return 1 if n<2 else n * factorial(n-1)

def tag(name,*content,cls=None, **attrs):
    """
    Generate html tags
    :param name: str
    :param content: list
    :param cls:  str
    :param attrs: dict
    :return: name, attr_str, c, name
    """
    if cls is not None:
        attrs['class']  = cls
    if attrs:
        attr_str =  ''.join(' %s="%s"' % (attr, value)
                            for attr, value
                            in sorted(attrs.items()))
    else:
        attr_str =''
    
    if content:
        return '\n'.join('<%s%s>%s</%s>'%
                         (name,attr_str,c,name) for c in content)
    else:
        return '<%s%s />'%(name,attr_str)

def fac(n:int) ->int:
    """
    
    :param n:  number
    :return:   n!
    """
    return reduce(lambda a,b:a *b, range(1,n+1))
 

if __name__ == '__main__':
    #Factorial
    # print(factorial(10))
    # print(factorial.__doc__)
    #
    # b = map(factorial,range(10))
    # print(list(b))
    #
    # c = list(map(factorial, filter(lambda n: n%2, range(6))))
    # print(c)
    #
    # d=reduce(add,range(5))
    # print(d)
    #
    
    #tag
    # a = tag('br')
    # print(a)
    #
    # b = tag('p','hello')
    # print(b)
    #
    # print(tag('p', 'hello', 'world'))
    # print(tag('p', 'hello', id=33))
    # print(tag('p', 'hello', 'world', cls = 'sidebar'))
    # print(tag(content='testing', name="img"))
    # my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
    #           'src': 'sunset.jpg', 'cls': 'framed'}
    # print(tag(**my_tag))
    
    
    # print(fac(5))
    s = 'The time has come'
    print(methodcaller('upper')(s))
    print(methodcaller('replace', ' ', '-')(s))
    print(partial(mul,3)(7))
    triple = partial(mul,3)
    print(list(map(triple,range(1,10))))
    
    picture= partial(tag,'img',cls='pic-frame')
    print(picture(src='wumpus.jpeg'))
    