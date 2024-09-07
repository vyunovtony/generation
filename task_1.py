class FlatIterator:
    def __init__(self, list_of_list):
        self.iter = self.iterator(list_of_list)

    def iterator(self, lst: list):
        for item in lst:
            if not isinstance(item, list):
                yield item
            else:
                yield from self.iterator(item)

    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.iter)
    

def test_1():

    list_of_list_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]


    for flat_iterator_item, check_item in zip(FlatIterator(list_of_list_1), 
                                              ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        assert flat_iterator_item == check_item
    
    assert list(FlatIterator(list_of_list_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()