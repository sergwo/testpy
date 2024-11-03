# TODO Напишите функцию для поиска индекса товара
def find_index(items,find):
    check=0
    for i in items:
        if i == find:
            check=1
            return(items.index(i))
    if i==0:
        return(None)


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list,find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

