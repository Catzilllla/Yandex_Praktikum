def check_str(A, B):
    for index in B:
        if index == A


def main():
    """base function"""
    while True:
        ost_str = input("НАЗВАНИЕ А: ")
        snd_str = input("НАЗВАНИЕ B: ")
        check_str(ost_str, snd_str)
        if ost_str == 'q' or snd_str == 'q':
            print("Выход")
            break


if __name__ == "__main__":
    main()

#ввести строки А и B
#берем каждый символ строки B и проверяем по правилам
#1_правило: Вывод P - Bi = Ai
#2_правило: Вывод I - Bi != Ai и нет совпадений с другими буквами
#3_правило: Вывод S - Bi != Ai и есть совпадения с другими буквами
#ABCBCYA
#ZBBACAA
#IPSSPIP