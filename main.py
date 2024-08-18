"""
В основной функции программы:

1. Создается объект UserManager.
2. Выполняются тесты на добавление пользователей, удаление и поиск, с обработкой возможных исключений.
3. Выводятся сообщения об ошибках, если пользователи уже существуют или не найдены.
"""

from user import User
from user_manager import UserManager, UserAlreadyExistsError, UserNotFoundError

def main():
    user_manager = UserManager()

    # Попытка добавить пользователей
    try:
        user1 = User("Stepan", "stepan@example.com", 30)
        user_manager.add_user(user1)
        print(f"Добавлен: {user1}")

        user2 = User("Vlad", "vlad@example.com", 25)
        user_manager.add_user(user2)
        print(f"Добавлен: {user2}")

        # Попытка добавить пользователя с уже существующим именем
        user_manager.add_user(user1)  # Ожидается исключение
    except UserAlreadyExistsError as e:
        print(e)

    # Попытка удалить пользователей
    try:
        user_manager.remove_user("Evgen")  # Пользователь не найден
    except UserNotFoundError as e:
        print(e)

    try:
        user_manager.remove_user("Stepan")
        print("Пользователь 'Stepan' удален.")
    except UserNotFoundError as e:
        print(e)

    # Попытка найти пользователя
    try:
        user_manager.find_user("Vlad")
        print("Пользователь 'Vlad' найден.")
    except UserNotFoundError as e:
        print(e)

    try:
        user_manager.find_user("Evgen")  # Пользователь не найден
    except UserNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()

