import threading


THREADS = 2
MAX_COUNT = 1000000

counter = 0


def cuenta():
    global counter

    for i in range(int(MAX_COUNT/THREADS)):
        counter += 1



threads = []

for i in range(THREADS):
    t = threading.Thread(target=cuenta)
    threads.append(t)

    t.start()

for t in threads:
    t.join()

print(f"Valor del contador: {counter}")



