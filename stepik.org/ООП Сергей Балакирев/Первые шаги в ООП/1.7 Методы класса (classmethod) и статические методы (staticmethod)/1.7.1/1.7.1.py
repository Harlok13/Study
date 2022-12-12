class Factory:
    @staticmethod
    def build_sequence():
        """Creating an empty list"""
        return []

    @staticmethod
    def build_number(string: str) -> int:
        """Converting integer from string"""
        try:
            return int(string)
        except ValueError:
            print('string must be a number')


class Loader:
    @staticmethod
    def parse_format(string: str, factory: Factory):
        """Creating list of integer from string"""
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
print(res)
