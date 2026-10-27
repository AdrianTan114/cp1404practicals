"""ProgrammingLanguages class."""


class ProgrammingLanguage:
    def __init__(self, name="", typing="", has_reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.has_reflection = has_reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.has_reflection}, First appeared in {self.year}"
