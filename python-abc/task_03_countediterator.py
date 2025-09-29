#!/usr/bin/python3
class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0
    def __next__(self):
        self.count += 1
        return next(self.iterator)
    def get_count(self):
        return self.count

#!/usr/bin/python3

from task_03_countediterator import CountedIterator

def test_counted_iterator():
    data = [10, 20, 30]
    iterator = CountedIterator(data)

    # İlk element
    assert next(iterator) == 10, "Incorrect item received from iterator"
    assert iterator.get_count() == 1, "Count should be 1 after first next()"

    # İkinci element
    assert next(iterator) == 20, "Incorrect item received from iterator"
    assert iterator.get_count() == 2, "Count should be 2 after second next()"

    # Üçüncü element
    assert next(iterator) == 30, "Incorrect item received from iterator"
    assert iterator.get_count() == 3, "Count should be 3 after third next()"

    # İterator bitdiyi üçün StopIteration
    try:
        next(iterator)
        assert False, "Expected StopIteration exception"
    except StopIteration:
        pass  # düzgün işləyir

    print("All CountedIterator tests passed!")

if __name__ == "__main__":
    test_counted_iterator()

