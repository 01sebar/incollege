import string
class Format:
    def __init__(self) -> None:
        pass

    def titleCase(self, str1: str):
        str1 = string.capwords(str1, sep = None)
        return str1