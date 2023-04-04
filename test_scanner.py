import os
import random
import re
from scanner import Scanner, PythonWordTokens_re, PythonSymbols_re, PythonSymbols_eq, quote_regexp, WhiteSpace, comment_regexp, number_regexp, TokenNamesForSymbols, eq_SymbolNames, WhiteSpaceNames
class generate(object):
    def __init__(self):
        pass

    def string(self):
        """This method generates a string with built in quotations"""
        string = ""
        quote = random.choice(['"', "'"])
        charList = []
        char = "`1234567 890[],.pyfgcrl/=aoe uidhtns-;qjk xbm wvz~!@#$%^&*(){}<>PYFGCRL ?+|AOEUIDHTNS _:QJKXBMWVZ"
        for i in char:
            charList.append(i)
        charList.append(" ")
        charList.append("\\n")
        charList.append("\\\\")
        if quote == '"':
            charList.append("\\\"")
            charList.append("'")
        else:
            charList.append('"')
            charList.append("\\'")
        for i in range(random.randint(1, 100)):
            string += random.choice(charList)
        string = quote + string + quote
        return string
    
    def docstring(self):
        """This method generates a docstring with built in quotations"""
        string = ""
        quote = random.choice(['"', "'"]) * 3
        charList = []
        char = "`1234567 890[],.pyfgcrl/=aoe uidhtns-;qjk xbm wvz~!@#$%^&*(){}<>PYFGCRL ?+|AOEUIDHTNS _:QJKXBMWVZ"
        for i in char:
            charList.append(i)
        charList.append(" ")
        charList.append("\\n")
        charList.append("\\\\")
        if quote == '"""':
            charList.append("\\\"")
            charList.append("'")
        else:
            charList.append('"')
            charList.append("\\'")
        for i in range(random.randint(1, 100)):
            string += random.choice(charList)
        string = quote + string + quote
        return string
    
    def fstring(self):
        """This method generates an fstring that is either a string or a docstring"""
        num = random.randint(1, 2)
        if num == 1:
            return "f" + self.string()
        else:
            return "f" + self.docstring()

    
    def keyword(self):
        """This method generates an alphanumeric keyword"""
        char = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9 _"
        onlyLetters = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
        var = random.choice(onlyLetters.split())
        for i in range(random.randint(0, 13)):
            var += random.choice(char.split())
        return var
    
    def comment(self):
        """This method generates a comment"""
        return "#" + self.string()
    
    def integer(self):
        """This method generates a number"""
        char = "1 2 3 4 5 6 7 8 9 0".split()
        inte = str(random.randint(1, 9))
        for i in range(random.randint(1, 5)):
            inte += random.choice(char)
        return inte
    
    def Tuple(self):
        """This method generates a tuple"""
        string = ""
        Tuple  = []
        for i in range(100):
            num = random.randint(1, 7)
            if num == 1:
                """python keyword in tuple"""
                pyword = random.choice("from import global class object __init__ def if True False try except pass break next last and print or return else elif as".split())
                space = " "
                string += pyword + space + "\n"
                Tuple.append((pyword, pyword.upper()))
                Tuple.append((space, 'WS'))
                Tuple.append(("\n", "NEWLINE"))
            elif num == 2:
                """whitespace in tuple"""
                comment = self.comment()
                string += "\n" + comment + "\n"
                Tuple.append(("\n", "NEWLINE"))
                Tuple.append((comment, "COMMENT"))
                Tuple.append(("\n", "NEWLINE"))
            elif num ==  3:
                """symbol in tuple"""
                symbolLinks = {"!=": 'NOTEQ', ",": "COMMA", ".": "DOT", "<": "LESS", ">": "GREAT", "<=": 'SMALL_OR_EQ', 
                            ">=": 'GREAT_OR_EQ', '==': 'TWICEEQ', "-=": 'MINUSEQ', "+=": "PLUSEQ", "=": 'EQ', "\\": "ESCAPE", 
                            ":": "COLON", "{": "LCBRACK", "}": "RCBRACK", "+": 'PLUS', "[": "LBRACK", "]": 'RBRACK',
                            "(":  "LPAREN", ")": "RPAREN"}
                keysymbols = random.choice("!= , . < > <= >= == -= += = \\ : { } + [ ] ( )".split())
                space = " " * random.randint(1, 8)
                string += keysymbols + space
                Tuple.append((keysymbols, symbolLinks[keysymbols]))
                while space != "":
                    if len(space) > 3:
                        Tuple.append(("    ", "INDENT"))
                        space = space[4:]
                    else:
                        Tuple.append((space, 'WS'))
                        space = ""
            elif num ==  4:
                """fstring in tuple"""
                fstring = self.fstring()
                string += fstring + "   \n"
                Tuple.append((fstring, "FSTRING"))
                Tuple.append(("   ", "WS"))
                Tuple.append(("\n", "NEWLINE"))
            elif num == 5:
                """string in tuple"""
                rstring = self.string()
                string += rstring + "\n"
                Tuple.append((rstring, "STRING"))
                Tuple.append(("\n", 'NEWLINE'))
            elif num == 6:
                """keyword in tuple"""
                keyword = self.keyword()
                if keyword in PythonWordTokens_re.split():
                    Tuple.append((keyword, keyword.upper()))
                else:
                    Tuple.append((keyword, 'KEYWORD'))
                string += keyword + " "
                Tuple.append((" ", 'WS'))

            elif num == 7:
                """number in tuple"""
                inte = self.integer()
                string += inte  + " "
                Tuple.append((inte, "NUMBER"))
                Tuple.append((" ", 'WS'))
    
        TestedClass = Scanner(PythonWordTokens_re, PythonSymbols_re, PythonSymbols_eq, quote_regexp, WhiteSpace, comment_regexp, number_regexp, TokenNamesForSymbols, eq_SymbolNames, WhiteSpaceNames)
        
        """Under the  assumption that some setup is possible in the list of Tuples, the following code blocks are commented instead of deleted"""
        # Debugging section below
        # DebugProgrammer_sets_this_to = False
        # if DebugProgrammer_sets_this_to:
        #     from custom_debugger_output import Tupl
        #     string = ""
        #     for i in Tupl:
        #         string += i[0]
        #     TesttheTuple = TestedClass.scan(string)
        #     if TesttheTuple != Tupl:
        #         for i in range(len(Tupl)):
        #             if  Tupl[i] != TesttheTuple[i]:
        #                 print(f"{i}: {Tupl[i]} {TesttheTuple[i]}")
        #         assert TesttheTuple == Tupl
        # else:
        TesttheTuple = TestedClass.scan(string)
        assert TesttheTuple == Tuple
        # if below is true then custom_debugger_output.py is written to 
        # so that the same issue can be revaluated until the problem is discovered

        # if TesttheTuple != Tuple:
        #     h1 = open('custom_debugger_output.py', 'w')
        #     h1.write("Tupl = ")
        #     h1.write(str(Tuple))
        #     h1.close()
        #     for i in range(len(Tuple)):
        #         if  Tuple[i] != TesttheTuple[i]:
        #             print(f"{i}: {Tuple[i]} {TesttheTuple[i]}")
        #     assert TesttheTuple == Tuple
        j = 0
        for i in range(50):
            if len(Tuple) > 0:
                j += 1
                # Testing the match method
                if random.randint(1, 2) == 1:
                    type_of_token = Tuple[0][1]
                else:
                    type_of_token = random.choice(f"{PythonWordTokens_re.upper()} {TokenNamesForSymbols} {eq_SymbolNames} {WhiteSpaceNames} NUMBER STRING FSTRING".split())
                if type_of_token == Tuple[0][1]:
                    match_pattern = Tuple[0][0]
                    beforeModification = len(Tuple)
                    assert TestedClass.match(Tuple, type_of_token) == (match_pattern, type_of_token)
                    assert beforeModification == len(Tuple) + 1
                else:
                    bM = len(Tuple)
                    assert TestedClass.match(Tuple, type_of_token) == None
                    assert len(Tuple) == bM
                # Testing the peek method
                if random.randint(1, 2) == 1:
                    type_of_token = Tuple[0][1]
                else:
                    type_of_token = random.choice(f"{PythonWordTokens_re.upper()} {TokenNamesForSymbols} {eq_SymbolNames} {WhiteSpaceNames} NUMBER STRING FSTRING".split())
                if type_of_token == Tuple[0][1]:
                    match_pattern = Tuple[0][0]
                    assert TestedClass.peek(Tuple, type_of_token) == (match_pattern, type_of_token)
                else:
                    assert TestedClass.peek(Tuple, type_of_token) == None

                # Testing the push method
                random_string, random_token = Tuple[random.randint(0, len(Tuple) - 1)]
                TestedClass.push(Tuple, (random_string, random_token))
                assert Tuple[-1] == (random_string, random_token)





    
# Prints the index number of the instance it is running
# and runs the test tuple function <func: Tuple>

Gen = generate()
for i in range(1):
    print(f"<<<<<<<{i}>>>>>>>")
    Gen.Tuple()
