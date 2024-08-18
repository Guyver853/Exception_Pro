"""
Содержит пользовательские исключения UserAlreadyExistsError и UserNotFoundError, а также класс UserManager,
который управляет пользователями
"""

# Пользовательские исключения
class UserAlreadyExistsError(Exception):
    def __init__(self, username):
        self.username = username
        self.message = f"Пользователь с именем '{self.username}' уже существует."
        super().__init__(self.message)


class UserNotFoundError(Exception):
    def __init__(self, username):
        self.username = username
        self.message = f"Пользователь с именем '{self.username}' не найден."
        super().__init__(self.message)


# Класс UserManager
class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        if user.username in self.users:
            raise UserAlreadyExistsError(user.username)
        self.users[user.username] = user

    def remove_user(self, username: str):
        if username not in self.users:
            raise UserNotFoundError(username)
        del self.users[username]

    def find_user(self, username: str):
        if username not in self.users:
            raise UserNotFoundError(username)
        return self.users[username]
