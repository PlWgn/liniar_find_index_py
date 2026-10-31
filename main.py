from random import randint
import time
try:
    import matplotlib.pyplot as plt
except ImportError as err:
    print(err)

times = []

def find_index(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1

for i in range(20000):
    arr = []
    
    for i in range(0, 10000):
        arr.append(randint(0, 100))
    
    start = time.perf_counter()
    found_index = find_index(arr, 50)
    end = time.perf_counter()
    
    times.append((found_index, round((end - start) * 1000, 5)))
    
print(times)

found = [(index, t) for index, t in times if index != -1]
not_found = [t for index, t in times if index == -1]

x = [index for index, _ in found]
y = [t for _, t in found]

plt.figure(figsize=(12, 6))

plt.scatter(
    x, y,
    s=8,
    alpha=0.25,
    label="Элемент найден"
)

if not_found:
    plt.scatter(
        [10000] * len(not_found),
        not_found,
        color="red",
        s=25,
        alpha=0.6,
        label="Элемент не найден"
    )

plt.xlabel("Количество проверенных элементов")
plt.ylabel("Время поиска (мс)")
plt.title("Зависимость времени линейного поиска от глубины поиска")

plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
