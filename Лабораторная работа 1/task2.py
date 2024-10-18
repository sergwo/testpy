# TODO Найдите количество книг, которое можно разместить на дискете

one_symbol=4
symbol_in_string=25
string_in_page=50
page_in_book=100
disk=1.44

book=one_symbol*symbol_in_string*string_in_page*page_in_book
book_mb=book/1024/1024
count_book=round(disk/book_mb)

print("Количество книг, помещающихся на дискету:", count_book)
