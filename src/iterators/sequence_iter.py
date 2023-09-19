class SequenceIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.sequence):
            raise StopIteration

        item = self.sequence[self.index]
        self.index += 1
        return item


class SquareIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index == len(self._sequence):
            raise StopIteration

        square = self._sequence[self._index] ** 2
        self._index += 1
        return square


class FibonacciIterator:
    def __init__(self, stop=10):
        self._stop = stop
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index == self._stop:
            raise StopIteration

        fib_number = self._current
        self._index += 1
        self._current, self._next = (self._next, self._current + self._next)
        return fib_number


# for item in SequenceIterator([1, 2, 3, 4]):
#     print(item)


# sequence = SequenceIterator([1, 2, 3, 4])
# print(id(sequence))

# # get an iterator over the data
# iterator = sequence.__iter__()
# print(id(iterator))
# print(iterator.index)
# while True:
#     try:
#         item = iterator.__next__()
#     except StopIteration:
#         break
#     else:
#         print(item)

# print(iterator.index)
# iterator = sequence.__iter__()
# print(id(iterator))
# while True:
#     try:
#         item = iterator.__next__()
#     except StopIteration:
#         break
#     else:
#         print(item)


# for item in SquareIterator([1, 2, 3, 4]):
#     print(item)


# for i in FibonacciIterator(10):
#     print(i)
