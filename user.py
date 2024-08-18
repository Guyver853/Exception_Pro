"""
Содержит определение класса User, который описывает пользователя с атрибутами username, email и age
Переопределен метод __str__, который возвращает строковое представление объекта пользователя.
"""

class User:
    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age

    def __str__(self):
        return f"User(username='{self.username}', email='{self.email}', age={self.age})"
