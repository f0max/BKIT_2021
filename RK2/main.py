# Вариант 20: Деталь - Поставщик
from operator import itemgetter
 
class Detail:
    """Деталь"""
    def __init__(self, id, name, mat, prov_id):
        self.id = id
        self.name = name
        self.mat = mat
        self.prov_id = prov_id
 
class Provider:
    """Поставщик"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class DetProv:
    """
    'Поставщики деталей' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, det_id, prov_id):
        self.det_id = det_id
        self.prov_id = prov_id
 
def task1(providers, details):
    one_to_many = [(d.name, d.mat, p.name) 
        for p in providers 
        for d in details 
        if d.prov_id == p.id]
    return sorted(one_to_many, key=itemgetter(0))

def task2(providers, details):
    res = list()

    one_to_many = [(d.name, d.mat, p.name) 
        for p in providers 
        for d in details 
        if d.prov_id == p.id]
    for p in providers:
        # Список деталей, поставляемых этим поставщиком
        p_dets = list(filter(lambda i: i[2]==p.name, one_to_many))        
        if len(p_dets) > 0:
            # Поставщик и количество деталей, им поставляемых
            res.append((p.name, len(p_dets)))
 
    # Сортировка по количеству поставляемых деталей
    return sorted(res, key=itemgetter(1), reverse=True)

def task3(providers, details, dets_provs):
    res = dict()

    many_to_many = [(d.name, d.mat, p.name)
        for d in details 
        for p in providers 
        for dp in dets_provs 
        if d.id == dp.det_id and 
           p.id == dp.prov_id]
    for p in providers:
        if p.name.startswith('ПК'):
            # Список деталей
            p_dets = list(filter(lambda i: i[2]==p.name, many_to_many))
            p_dets_names = [i for i,_,_ in p_dets]
            # Добавляем результат в словарь
            # ключ - поставщик, значение - список названий деталей
            res[p.name] = p_dets_names
    return res
 
def main():
    """Основная функция"""

    # Поставщики
    providers = [
        Provider(1, 'ПАО "Ижсталь"'),
        Provider(2, 'ПК "ГМК Норникель"'),
        Provider(3, 'ПК "Северсталь"'),
        Provider(4, 'ПК "РУСАЛ Красноярск"'),
        Provider(5, 'ООО "ПФ Инзенский ДОЗ"'),
        Provider(6, 'Тайшетский АЗ'),
        Provider(7, 'ПК Челябинский МК'),
        Provider(8, 'ПК Металлогорский МК')
    ]
    
    # Детали
    details = [
        Detail(1, 'Болт М2', 'Сталь', 1),
        Detail(2, 'Труба Д16Т', 'Никель', 2),
        Detail(3, 'Доска 160х20', 'Дерево', 5),
        Detail(4, 'Штуцер М26хШ22', 'Сталь', 3),
        Detail(5, 'Профиль 20х20х2000', 'Алюминий', 4),
        Detail(6, 'Фланец Д25', 'Алюминий', 8),
        Detail(7, 'Калиброванный прокат', 'Сталь', 1),
        Detail(8, 'Лента', 'Сталь', 1),
        Detail(9, 'Катодный лист Н-1У', 'Никель', 2),
        Detail(10, 'Фольга', 'Алюминий', 3),
        Detail(11, 'Колесный диск', 'Алюминий', 3),
        Detail(12, 'Катанка', 'Алюминий', 3)
    ]
    
    dets_provs = [
        DetProv(1, 1),
        DetProv(1, 3),
        DetProv(1, 7),
        DetProv(1, 8),

        DetProv(2, 2),

        DetProv(3, 5),
        
        DetProv(4, 1),
        DetProv(4, 3),
        DetProv(4, 7),
        DetProv(4, 8),

        DetProv(5, 4),
        DetProv(5, 6),

        DetProv(6, 4),
        DetProv(6, 6),

        DetProv(7, 1),
        DetProv(7, 3),
        DetProv(7, 7),
        DetProv(7, 8),

        DetProv(8, 1),
        DetProv(8, 3),
        DetProv(8, 7),
        DetProv(8, 8),

        DetProv(9, 2),

        DetProv(10, 4),
        DetProv(10, 6),

        DetProv(11, 4),
        DetProv(11, 6),

        DetProv(12, 4),
        DetProv(12, 6)
    ]
    
    
 
    print('Задание А1')
    res_1 = task1(providers, details)
    [print(res) for res in res_1]
    
    print('\nЗадание А2')
    res_2 = task2(providers, details)
    [print(res) for res in res_2]
 
    print('\nЗадание А3')
    res_3 = task3(providers, details, dets_provs)    
    [print(key, value) for key, value in res_3.items()]
 
if __name__ == '__main__':
    main()