GRAPH = {
    'Адмиралтейская': {'Садовая': 4},
    'Садовая': {'Адмиралтейская': 4, 'Сенная площадь': 4, 'Спасская': 3, 'Звенигородская': 5},
    'Сенная площадь': {'Садовая': 4, 'Спасская': 4},
    'Спасская': {'Садовая': 3, 'Сенная площадь': 4, 'Достоеваская': 6},
    'Достоеваская': {'Спасская': 6, 'Владимирская': 3},
    'Владимирская': {'Достоеваская': 3, 'Пушкинская': 4},
    'Пушкинская': {'Звенигородская': 3, 'Владимирская': 4},
    'Звенигородская': {'Пушкинская': 3, 'Садовая': 5}
}



D = {k: 100 for k in GRAPH.keys()}
U = {k: False for k in GRAPH.keys()}
P = {k: None for k in GRAPH.keys()}


start_k = 'Адмиралтейская'  # стартовая вершина
D[start_k] = 0  # расстояние от неё до самой себя равно

for _ in range(len(D)):
    print('Вывод всех не просмотренных Вершин')
    print([k for k in U.keys() if not U[k]])

    print('Все все станции', {k: D[k] for k in U.keys() if not U[k]})

    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in U.keys() if not U[k]], key=lambda x: D[x])
    print('Самая короткая', min_k)

    print('цикл', _)

    for v in GRAPH[min_k].keys():  # проходимся по всем смежным вершинам
        print(min_k, '-', v)
        print(D[v], 'или', D[min_k], '+', GRAPH[min_k][v])
        if D[v] > D[min_k] + GRAPH[min_k][v]:  # если расстояние от текущей вершины меньше
            D[v] = D[min_k] + GRAPH[min_k][v]  # то фиксируем его
            print('!!!!!!', min_k)
            P[v] = min_k  # и записываем как предок
            print('Меньшее', D[v])
    U[min_k] = True  # просмотренную вершину помечаем
    print('Все вершины пути от', min_k)
    for v in GRAPH[min_k].keys():
        print(v, '-', D[v], end=', ')
    print()

print('__________')
for i in D:
    print(i, D[i])
print('__________')

print(D)
print(P)
Z = list(GRAPH.keys())
pointer = Z[5] # куда должны прийти

print('__________')
while pointer is not None:  # перемещаемся, пока не придём в стартовую точку
    print(pointer, P)
    pointer = P[pointer]
