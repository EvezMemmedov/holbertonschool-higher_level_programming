#!/usr/bin/python3
class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0
    def __next__(self):
        self.count += 1
        return next(self,iterator)
    def get_count(self):
        return self.count

if __name__ == "__main__":
    data = [1, 2, 3, 4]
    counted_iter = CountedIterator(data)

    try:
        while True:
            item = next(counted_iter)
            print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
    except StopIteration:
        print("No more items.")
