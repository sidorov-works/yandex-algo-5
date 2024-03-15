# Колесо фортуны

n = int(input())
values = list(map(int, input().split()))
a, b, k = list(map(int, input().split()))

# Сколько секторов мы сможем прокрутить при максимальной скорости
x_max = (b - 1) // k
x_min = (a - 1) // k

# Если мы покрываем все сектора,
if x_max - x_min >= n - 1:
    print(max(values)) # то результат – максимум из исходных значений
else:
    x_min = x_min % n
    x_max = x_max % n

    if x_max < x_min:
        print(max(
            set(values[x_min: ] + values[: n - x_min + 1] + values[: x_max + 1] + values[n - x_max:])
        ))
    else:
        print(max(
            set(values[x_min: x_max + 1] + values[n - x_max: n - x_min + 1])
        ))