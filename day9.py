from get_data import get_data_as_list
from collections import defaultdict
from enum import Flag,auto
class Token(Flag):
    LT = auto()
    GT = auto()
    RBRACE = auto()
    LBRACE = auto()
    COMMA  = auto()
    BANG   = auto() # !
    LETTER = auto()


lex_table = defaultdict(lambda : Token.LETTER)
lex_table.update({"<": Token.LT , ">":Token.GT, 
    "{":Token.LBRACE, "}":Token.RBRACE,
     ",":Token.COMMA, "!":Token.BANG})

print(lex_table)

def lex(data):
    return [lex_table[char] for char in data]



class Parser:
    def __init__(self,dbgprint=False):
        self.i = 0
        self.group = 0
        self.score = 0
        self.garbage = False
        self.parse_table = defaultdict
        self.garbage_chars = 0
        self.dbgprint = dbgprint

    def inc(self, n=1):
        self.i += n
        if self.garbage:
            self.garbage_chars += 1

    def skip(self, n=1):
        self.i += n

    def bang(self):
        self.skip(2) #Skip the ! and next char
    
    def lt(self):
        self.inc()
        self.garbage = True

    def gt(self):
        self.garbage = False
        self.inc()
    
    def rbrace(self):
        self.inc()
        self.score += self.group
        self.group -= 1

    def lbrace(self):
        self.inc()
        self.group += 1


    def parse(self, lexed):
        while self.i < len(lexed):
            if self.dbgprint:
                print("Current Token: {}/{}  {} {}".format(self.i+1, len(lexed), lexed[self.i], self.garbage if "garbage" else ""))

            if not self.garbage:
                defaultdict(lambda: self.inc,{
                    Token.LT: self.lt,
                    Token.GT: self.gt,
                    Token.COMMA: self.inc,
                    Token.COMMA: self.inc,
                    Token.RBRACE: self.rbrace,
                    Token.LBRACE: self.lbrace})[lexed[self.i]]()
            
            else:
                defaultdict(lambda: self.inc, 
                    {Token.LT: self.lt,
                     Token.GT: self.gt,
                     Token.BANG: self.bang})[lexed[self.i]]()

        return self


def lex_and_parse(string):
    return Parser().parse(lex(string))

if __name__ == '__main__':
    data = get_data_as_list(9, str)[0] # Get as string
    lexed = lex(data)
    parser = Parser()

    # {}, score of 1.
    # {{{}}}, score of 1 + 2 + 3 = 6.
    # {{},{}}, score of 1 + 2 + 2 = 5.
    # {{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
    # {<a>,<a>,<a>,<a>}, score of 1.
    # {{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
    # {{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
    # {{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.
    print(1 , "==", lex_and_parse("{}").score)
    print(6 , "==", lex_and_parse("{{{}}}").score)
    print(16, "==", lex_and_parse("{{{},{},{{}}}}").score)
    print(1 , "==", lex_and_parse("{<a>,<a>,<a>,<a>}").score)
    print(9 , "==", lex_and_parse("{{<ab>},{<ab>},{<ab>},{<ab>}}").score)
    print(9 , "==", lex_and_parse("{{<!!>},{<!!>},{<!!>},{<!!>}}").score)
    print(3 , "==", lex_and_parse("{{<a!>},{<a!>},{<a!>},{<ab>}}").score)
    print("10 ==" , Parser(True).parse(lex("<{o\"i!a,<{i<a>")).garbage_chars)


    print("Task 1 score: ",parser.parse(lexed).score)
    print("Garbage Chars:", parser.garbage_chars)
