from sequence_iter import SequenceIterator


class Iterable:
    def __init__(self, sequence):
        self._sequence = sequence

    def __iter__(self):
        return SequenceIterator(self._sequence)


class Stack:
    def __init__(self):
        self._items = []

    def __push__(self, item):
        self._items.append(item)

    def __pop__(self, item):
        try:
            return self._items.pop()
        except IndexError:
            raise IndexError("pop from an empty stack")

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)


for i in Iterable([1, 2, 3, 4]):
    print(i)

test = iter(Iterable([1, 2, 3, 4]))
print(test.__dir__())

a = [1, 2, 3, 4]
b = reversed(a)
print(type(b))

for i in b:
    print(i)


stack = Stack()
