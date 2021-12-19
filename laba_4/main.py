import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt, end='')
        coef_str = input()

    # Проверка, что А != 0
    while index == 1 and coef_str == '0':
        print('А не может быть 0. Введите снова: ', end='')
        coef_str = input()
    
    # Переводим строку в действительное число
    while True:
        try:
            coef = float(coef_str)
        except ValueError:
            print('Неверный формат.', prompt, end='')
            coef_str = input()
        else:
            break
    
    return coef

def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения с заменой x^2 = t

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b*b - 4*a*c

    if D == 0.0:
        root = -b / (2.0*a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        result.append(round(root1, 2))
        result.append(round(root2, 2))
    return result

def reverse_roots(roots):
    '''
    Обратная замена x = sqrt(t)

    Args:
        roots[float]: Список решений квадратного уравнения относительно t

    Returns:
        list[float]: Список окончательных решений
    '''
    result = []
    for root in roots:
        if root > 0:
            rev_root1 = math.sqrt(root)
            rev_root2 = -math.sqrt(root)
            result.append(round(rev_root1, 2))
            result.append(round(rev_root2, 2))
        elif root == 0:
            rev_root = 0
            result.append(round(rev_root, 2))
    return result

def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А: ')
    b = get_coef(2, 'Введите коэффициент B: ')
    c = get_coef(3, 'Введите коэффициент C: ')

    # Вычисление корней
    intermediate_roots = get_roots(a, b, c)
    roots = reverse_roots(intermediate_roots)

    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет действительных корней')
    elif len_roots == 1:
        print(f'Один корень: {roots[0]}')
    elif len_roots == 2:
        print(f'Два различных корня: {roots[0]} и {roots[1]}')
    elif len_roots == 3:
        print(f'Три различных корня: {roots[0]}, {roots[1]} и {roots[2]}')
    else:
        print(f"Четыре различных корня: {roots[0]}, {roots[1]}, {roots[2]} и {roots[3]}")

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()