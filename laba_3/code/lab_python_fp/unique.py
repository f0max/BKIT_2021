# Итератор для удаления дубликатов
class Unique(object):
    '''Итератор для удаления дубликатов'''
    
    def __init__(self, items, **kwargs):
        self.items = list(items)
        self.ignore_case = kwargs.get('ignore_case')
        self.used_elements = set()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= len(self.items):
                raise StopIteration
            else:
                curr = self.items[self.index]
                if self.ignore_case and isinstance(curr, str):
                    curr = curr.lower()
                self.index += 1
                try:
                    if curr not in self.used_elements:
                        self.used_elements.add(curr)
                        return curr
                except TypeError:
                    continue
