import hashlib

my_str = input('Введите строку: ')


def sub_str(str_):

    my_set = set()

    for i in range(len(str_)):
        for j in range(len(str_), i, -1):
            hash_str = hashlib.sha1(str_[i:j].encode('utf-8')).hexdigest()
            my_set.add(hash_str)
            print(my_str[i:j], hash_str)

    return len(my_set) - 1


print(f'в строке "{my_str}" - {sub_str(my_str)} различных подстрок')
