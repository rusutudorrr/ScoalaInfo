from collections.abc import MutableSequence


class CrayonBox(MutableSequence):
    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        print(f'Crayon box gas a length of {len(self._crayons)} crayons')
        return len(self._crayons)

    def __getitem__(self, index):
        print(f'Get item with index {index} that is {self._crayons[index]}')
        return self._crayons[index]

    def __delitem__(self, index):
        print(f'The {self._crayons[index]} crayon with index {index} was deleted')
        del self._crayons[index]
        return self._crayons

    def __setitem__(self, index, value):
        self._crayons[index] = value
        return self._crayons

    def insert(self, index, value):
        self._crayons.insert(index, value)
        return self._crayons


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayon_box = CrayonBox(crayons)
