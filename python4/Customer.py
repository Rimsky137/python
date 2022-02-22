class Customer:

    def __init__(self, name, surname,patronymic, age, phone, email):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.age = age
        self.phone = phone
        self.email = email
    def __str__(self):
        return " Имя - {}\n Фамилия - {}\n Отчество - {}\n Возраст - {}\n Телефон - {}\n email - {}".format(self.name, self.surname, self.patronymic, self.age, self.phone, self.email)
