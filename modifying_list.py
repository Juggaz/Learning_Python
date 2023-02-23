list = []

def make_great(list):
    for i in range(len(list)):
        list[i] = 'the Great ' + list[i]
        print(list[i])

def print_list(list):
        print(list)

while True:
    name = input('Enter a name: ')
    if name == 'q':
        break
    list.append(name)
    print(list)

make_great(list)
print_list(list)