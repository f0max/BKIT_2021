import json
import sys
from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1

try:
    path = "../data_light.json" #sys.argv[1]
except IndexError:
    raise ValueError("Не указан путь к файлу")
else:
    with open(path, encoding='utf-8') as f:
        data = json.load(f)

@print_result
def f1(lst):
    return sorted(list(Unique(field(lst, 'job-name'), ignore_case=True)), key=str.lower)


@print_result
def f2(lst):
    return list(filter(lambda s: str.startswith(str.lower(s), 'программист'), lst))


@print_result
def f3(lst):
    return list(map(lambda s: s + " с опытом Python", lst))


@print_result
def f4(lst):
    return dict(zip(lst, [f"зарплата {num} руб." for num in gen_random(len(lst), 1000000, 2000000)]))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))