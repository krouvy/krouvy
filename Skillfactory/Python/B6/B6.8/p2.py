def foo(arg='there'):
    print('hello', arg)


number500 = 500
str = 'number500'

print(str, '=', locals()[str])

fooStr = 'foo'
print(f'{fooStr}()')
locals()[fooStr]()
