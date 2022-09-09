def str_(string):
    print(string)
    if len(string) == 0:
        return ''
    else:
        return string[-1] + str_(string[:-1])

print(str_('Жопа'))