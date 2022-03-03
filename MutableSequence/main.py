from utils import print_header
from crayonbox import crayon_box

print_header('__len__')
print(len(crayon_box))

print_header('__getitem__')
print(crayon_box[3])

print_header('__contains__')
if 'Blue' in crayon_box:
    print('Blue crayon is in the crayon box')

print_header('__iter__')
for crayon in crayon_box:
    print(crayon)

print_header('__delitem__')
print(crayon_box.__delitem__(0))

print_header('__setitem__')
print(crayon_box.__setitem__(0, 'Black'))

print_header('Insert')
print(crayon_box.insert(0, 'Yellow'))
