text = input('Введите текст... ')
text2 = set("""The Zen of Python Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never.Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!	""")

print(list(text))
text = set(text)

print(f'Текст в виде множества {text} длина {len(text)}')
print(f'Текст в виде множества {text2} длина {len(text2)}')

for i in text:
    if i not in text2:
        print(i, 'Нет')

