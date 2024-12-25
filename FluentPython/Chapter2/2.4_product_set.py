# EX) 티셔츠 리스트
# Color: Black, White
# Size: Small, Medium, Large

colors = ['black', 'white']
sizes = ['S', 'M', 'L']


tshirts_1 = [ (color, size) for color in colors for size in sizes]

for color in colors:
    for size in sizes:
        print(color, size)

symbols = '$ASDF'
tuple(ord(symbol) for symbol in symbols)

import array
array.array('I', (ord(symbol) for symbol in symbols))
