"""
Решено самостоятельно
"""


class WindowDlg:
    def __init__(self, title: str, width: int, height: int):
        self.__title = title
        self.__width = None
        self.__height = None
        if self.__check_value(width, height):
            self.__width = width
            self.__height = height

    def show(self) -> None:
        """View info about our window"""
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int) -> None:
        if self.__check_value(width):
            self.__width = width
            self.show()

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int) -> None:
        if self.__check_value(height):
            self.__height = height
            self.show()

    @staticmethod
    def __check_value(*args: [int, str]) -> bool:
        return all([i in range(0, 1001) and type(i) == int for i in args])


wnd = WindowDlg('title', 100, 50)
wnd.show()
wnd.width = 54
