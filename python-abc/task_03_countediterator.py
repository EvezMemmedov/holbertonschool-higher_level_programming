#!/usr/bin/python3

class CountedIterator:
    """Iterator wrapper that counts how many items have been iterated."""

    def __init__(self, iterable):
        """Initialize with an iterable and set counter to 0."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Return the next item from the iterator.
        Increment the counter only if an item is successfully fetched.
        """
        item = next(self.iterator)  # StopIteration atılırsa counter artmayacaq
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.count
