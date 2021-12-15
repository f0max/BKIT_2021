# Итератор для удаления дубликатов
class Unique(object):
    '''Итератор для удаления дубликатов'''
    
    def __init__(self, items, **kwargs):
        self.items = items
        self.ignore_case = kwargs.get('ignore_case')
        self.used_elements = set()

    def __iter__(self):
        return self

    def __next__(self):
        it = iter(self.items)
        while True:
            try:
                curr = next(it)
            except StopIteration:
                raise
            else:
                if self.ignore_case and isinstance(curr, str):
                    if curr.lower() not in self.used_elements:
                        self.used_elements.add(curr.lower())
                        return curr
                elif curr not in self.used_elements:
                    self.used_elements.add(curr)
                    return curr
