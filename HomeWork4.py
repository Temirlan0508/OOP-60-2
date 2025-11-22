class Book:
    def __init__(self, title, author, pages, format="бумажная"):
        self.title = title       # Название книги
        self.author = author     # Автор книги
        self.pages = pages       # Количество страниц
        self.format = format     # Формат книги (по умолчанию "бумажная")

    def __str__(self):
        return f'"{self.title}" — {self.author}, {self.pages} стр.'

    def __len__(self):
        return self.pages

    def __add__(self, other):
        if isinstance(other, Book):
            total_pages = self.pages + other.pages
            return f"Вместе: {total_pages} страниц"
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.pages == other.pages
        return NotImplemented

    def __getitem__(self, chapter):
        return f"Глава {chapter}: содержание книги '{self.title}'"

    @classmethod
    def from_string(cls, s):
        parts = s.split(", ")
        title = parts[0]
        author = parts[1]
        pages = int(parts[2])
        return cls(title, author, pages)

    @staticmethod
    def is_thick(pages):
        return pages > 500

# Обычное создание
book1 = Book("ABC", "John Doe", 100)

# Через класс-метод
book2 = Book.from_string("ABC, John Smith, 100")

# Магические методы
print(book1)
print(len(book1))
print(book1 + book2)
print(book1 == book2)
print(book1[5])

# Статический метод
print(Book.is_thick(600))
print(Book.is_thick(300))       # False

# Формат по умолчанию
book3 = Book("ABC", "John Doe", 100)
print(book3.format)