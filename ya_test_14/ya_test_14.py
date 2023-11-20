def check_num(num):
    """check number"""
    try:
        try_check = int(num)
    except ValueError:
        print("it's not a number!")
    else:
        print(f"================good. its a number = {try_check}")
        return try_check


def open_file(a, b):
    name_file = input("Как назовём текстовый файл? ")
    with open('{}.txt'.format(name_file), 'x') as my_file:
        my_file.write('{}'.format(a))
        my_file.write(' ')
        my_file.write('{}'.format(b))
    my_file.close()


def sum_num(a, b):
    open_file(a, b)
    return (int(a) + int(b))


def main():
    """base function"""
    while True:
        first_number = input("Введите первое число: ")
        check_num(first_number)
        second_number = input("Введите второе число: ")
        check_num(second_number)
        if first_number == 'q' or second_number == 'q':
            print("Выход")
            break
        print(
            f'===================================== '
            f'Первое число + Второе число равно = '
            f'{sum_num(first_number, second_number)}')


if __name__ == "__main__":
    main()
