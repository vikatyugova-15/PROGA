def field(items, *args):
    if not args:
        for item in items:
            if item:
                yield
    else:
        for item in items:
            result = {}
            for key in args:
                if key in item and item[key] is not None :
                    result[key] = item [key]
            if result:
                yield result
    
goods = [
    {'title': 'Carpet', 'price': 2000, 'color': 'green'},
    {'title': 'Sofa for relax', 'color': 'black'}
]


for title  in field (goods, 'title'):
    print(title)

for item in field (goods, 'title', 'price'):
    print (item)

