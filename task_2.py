import types

def flat_generator(list_of_lists):
    for item in list_of_lists:
        if not isinstance(item, list):
            yield item
        else:
            yield from flat_generator(item)


def test_2():

    list_of_list_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for flat_iterator_item, check_item in zip(flat_generator(list_of_list_1),  
                                              ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_list_1)) ==  ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_list_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()