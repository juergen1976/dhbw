class StringIterator:
    def __init__(self, strings):
        self.strings = strings
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.strings):
            result = self.strings[self.index]
            self.index += 1
            return result
        raise StopIteration

strings = ["hello", "world", "python"]
iterator = StringIterator(strings)
for string in iterator:
    print(string)

class NumberIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            result = self.numbers[self.index]
            self.index += 1
            return result
        raise StopIteration

numbers = [1, 2, 3, 4, 5]
iterator = NumberIterator(numbers)
for num in iterator:
    print(num)