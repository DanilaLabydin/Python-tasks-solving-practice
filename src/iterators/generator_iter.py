def generator_sequence(seq):
    for i in seq:
        yield i


def fib_generator(stop=10):
    current = 0
    next = 1
    for _ in range(stop):
        nb = current
        current, next = (next, current + next)
        yield nb


array = [1, 2, 3, 4]
gen_func = generator_sequence(array)
for i in gen_func:
    print(i)

for i in gen_func:
    print(i)


gen_func2 = (item for item in range(1, 5))
for i in gen_func2:
    print(i)


square_gen = (item**2 for item in range(10))
for i in square_gen:
    print(i)


fib_nums = fib_generator()
for i in fib_nums:
    print(i)
