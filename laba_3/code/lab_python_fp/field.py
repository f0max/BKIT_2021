goods = [
   {'title': 'Ковер', 'price': 2000, 'color': 'green'},
   {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(dicts, *keys):
    assert len(keys) > 0
    if len(keys) == 1:
        for d in dicts:
            val = d.get(keys[0])
            if val != None:
                yield val
    else:
        for d in dicts:
            res_dict = dict()
            for key in keys:
                val = d.get(key)
                if val != None:
                    res_dict[key] = val
            if len(res_dict) != 0:
                yield res_dict