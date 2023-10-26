# TODO Найдите количество книг, которое можно разместить на дискете
papers = 100
strings = 50
items = 25
symbol = 4
volume = 1.44
k = 1024
total_symbols = items * symbol
total_strings = total_symbols * strings

total_papers = total_strings * papers
volume_2 = volume * k * k

number_of_books = volume_2 // total_papers

#print("Количество книг, помещающихся на дискету:", print(f'{number_of_books : .0f}'))
print("Количество книг, помещающихся на дискету:",int(number_of_books))
