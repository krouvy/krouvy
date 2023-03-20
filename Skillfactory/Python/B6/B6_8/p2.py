def foo(arg='there'):
    print('hello', arg)


number500 = 500
str = 'number500'

print(str, '=', locals()[str])

fooStr = 'foo'
print(f'{fooStr}()')
locals()[fooStr]()

# Можно
eval('print')('Жопа')

# Нельзя
# eval('print(С ручкой)')

# Можно
exec('print(123)')

# Нельзя
# exec('print(Жопа)')

# Можно
exec('print("Жопа c ручкой")')

