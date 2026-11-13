KEY_WORDS = ["программа", "целое", "пока", "счёт", "если", "печать", "иначе", "конец"]
SINGL = [":", ";", "=", "<", ">", "%", "(", ")", "{", "}"]
DOUBLE = ["==", "+="]

class lexer:
    def __init__(self, text: str):
        self.string = text
        self.cur_symbol = 0
        self.cur_string = 1
        self.cur_column = 1

    def ch_symbol(self):
        char = self.text[self.cur_symbol]
        self.is_new_string(char)
        if self.cur_symbol == len(self.text):
            return char
        else:
            char


    def is_new_string(self, char: str):
        if char == "/n":
            self.cur_string += 1
            self.cur_column = 1
        else: self.cur_column += 1
        self.cur_symbol += 1

   # def print_cur_status(self, char: str):






