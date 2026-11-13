from lexer import lexer as lex

with open("programm.bmstu", "r", encoding="UTF-8") as f:
    pr = f.read()
    cur_lex = lex(pr)
    cur_lex.ch_symbol()
