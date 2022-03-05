class User():

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city


    def describe_user(self):
        print (f"{self.first_name} {self.last_name} возрастом {self.age} проживает в городе {self.city}")


    def greet_user(self):
        print (f"Приветствую вас, {self.first_name} {self.last_name}")

class Admin(User):

    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)


    def show_privileges(self):
        print(f"\nСписок доступных привилегий пользователя {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(privilege.title())


user1 = Admin('Игорь', 'Петрович', '54 года','Москва')
user1.describe_user()
user1.greet_user()

user1.privileges = [
    'разрешено отправлять сообщения',
    'разрешено удалять страницы пользователей',
    'разрешено блокировать аккаунты пользователей',
    ]

user1.show_privileges()