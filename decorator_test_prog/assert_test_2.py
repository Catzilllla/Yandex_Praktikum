class Contact:
    def __init__(self, name, year_birth, is_programmer):
        self.name = name        
        self.year_birth = year_birth        
        self.is_programmer = is_programmer

    def age_define(self):
        if 1946 < self.year_birth < 1980:
            return 'Олдскул'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Старейшина'

    def programmer_define(self):
        if self.is_programmer:
            return 'Программист'
        return 'Нормальный'

    def show_contact(self):
        return(f'{self.name}, '              
               f'возраст: {self.age_define()}, '
               f'статус: {self.programmer_define()}')

    def print_contact(self):
        print(self.show_contact())

# Создайте экземпляр класса Contact с необходимыми параметрами
# Например, test_old_none_programmer = Contact('Пушкин', 1799, False).
# Напишите assert, и в нём проверьте, 
# что метод programmer_define() этого экземпляра возвращает строку "Нормальный"
# Во втором assert проверьте, возвращает ли метод age_define() значение "Старейшина"

# Затем создайте другой экземпляр с другими параметрами
# И в assert проверьте, вернут ли и его методы ожидаемый результат.

# Создайте столько экземпляров, сколько нужно, 
# чтобы через разные assert проверить все методы во всех вариантах.

test_old_none_programmer = Contact('Пушкин', 1799, False)
expected_string = 'Нормальный'
assert test_old_none_programmer.programmer_define() == expected_string, 'Ошибка статуса'
expected_age = 'Старейшина'
assert test_old_none_programmer.age_define() == expected_age, 'Ошибка возраста'

test_age = Contact('Дулепов', 1960, True)
expected_string = 'Программист'
assert test_age.programmer_define() == expected_string, 'Ошибка статуса'
expected_age = 'Олдскул'
assert test_age.age_define() == expected_age, 'Ошибка возраста'

test_prog = Contact('Платон', 2000, False)
expected_string = 'Нормальный'
assert test_prog.programmer_define() == expected_string, 'Ошибка статуса'
expected_age = 'Молодой'
assert test_prog.age_define() == expected_age, 'Ошибка возраста'