# Класс пользователя
class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin

# Декоратор, разрешающий выполнение функции только для админа
def admin_only(func):
    def wrapper(user, *args, **kwargs):
        if not isinstance(user, User):
            raise TypeError("Аргумент должен быть объектом User")
        if user.is_admin:
            return func(user, *args, **kwargs)
        else:
            raise PermissionError("Доступ запрещён! Только админ может выполнить эту операцию.")
    return wrapper

# Применяем декоратор
@admin_only
def delete_database(user):
    print("База данных удалена!")

# Пример использования
admin = User("Алексей", is_admin=True)
user = User("Мария", is_admin=False)

# Админ может удалить
delete_database(admin)  # Вывод: База данных удалена!

# Обычный пользователь — нет
try:
    delete_database(user)  # Ошибка PermissionError
except PermissionError as e:
    print(e)