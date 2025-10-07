
class User:
    def __init__(self, id, name):
        self._user_id = id
        self._name = name
        self._level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_level(self):
        return self._level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._level = 'admin'

    def add_user(self, user_list, user):
        user_id = user.get_user_id()
        if any(u.get_user_id() == user_id for u in user_list):
            print("Ошибка: пользователь с таким ID уже существует")
            return

        user_list.append(user)
        print(f"Пользователь {user.get_name()} добавлен")

    def remove_user(self, user_list, user_id):
        for i, user in enumerate(user_list):
            if user.get_user_id() == user_id:
                user_list.pop(i)
                print(f"Пользователь с ID {user_id} удален")
                return
        print("Ошибка: пользователь с указанным ID не найден")


users = []


admin = Admin(1, "Вася")


user1 = User(2, "Ваня")
user2 = User(3, "Петя")


admin.add_user(users, user1)
admin.add_user(users, user2)



print("\n Список пользователей:")
for user in users:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень: {user.get_level()}")


admin.remove_user(users, 2)


print("\n Обновленный список:")
for user in users:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень: {user.get_level()}")