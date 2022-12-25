```
class Book:
    title: str
    author: str
    pages: int
    year: int

    def __init__(
            self,
            title: str = "",
            author: str = "",
            pages: int = 0,
            year: int = 0,
    ) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value) -> None:
        if not isinstance(value, self.__annotations__.get(key, object)):
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)

    def __repr__(self) -> str:
        return f"{self.title} - {self.author}"


book = Book(title="Python ООП", author="Сергей Балакирев", year=2022, pages=123)
```
