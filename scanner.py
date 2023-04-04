import re

class Scanner(object):
    def __init__(self, PythonWordTokens_re, PythonSymbols_re, PythonSymbols_eq, quote_regexp, WhiteSpace, comment_regexp, number_regexp, symbolicnames, eq_symbolicnames, ws_names):
        """Takes a list of tuples and configures the scanner."""
        # Initializes the pattern recognition engine for the scanner
        self.PythonWordTokens_re = PythonWordTokens_re
        self.PythonSymbols_re = PythonSymbols_re
        self.PythonSymbols_eq = PythonSymbols_eq
        self.quote_regexp = quote_regexp
        self.WhiteSpace = WhiteSpace
        self.comment_regexp = comment_regexp
        self.number_regexp = number_regexp
        self.symbolicnames = symbolicnames
        self.eq_symbolicnames = eq_symbolicnames
        self.ws_names = ws_names

    def scan(self, string):
        """Takes a string and runs the scan on it, creating a list of tokens for later. You should keep this string around for people to access later."""
        Scanned = [] # holds the output in the form of a list of tuples each tuple being (pattern, token)
        hold = string # Debug check 2
        falss = "" # Debug check 1
        Debug_print = False # Debug check 3

        while string != "":
            falss = string # Debug check 1
            
            # RECOGNITION FOR QUOTES
            if re.findall(self.quote_regexp, string):
                if Debug_print:
                    print("some string")
                match = re.findall(self.quote_regexp, string)[0]
                string_capture = match[0] + match[1]
                Debug_animation = [string]
                string = re.sub(self.quote_regexp, "", string)

                # FSTRING RECOGNITION
                if match[0] == "f":
                    TokenName = 'FSTRING'
                else:
                # REGULAR STRING RECOGNITION
                    TokenName = "STRING"
                while string[0:len(match[1])] != match[1]:
                    if string[0] == "\\":
                        string_capture += string[0:2]
                        string = string[2:]
                    else:
                        string_capture += string[0]
                        string = string[1:]
                    Debug_animation.append(string)
                    
                string_capture += match[1]
                string = string[len(match[1]):]
                Found = True
                Scanned.append((string_capture, TokenName))

            # KEYWORD OR PYTHON KEYWORD RECOGNITION
            elif re.findall("^[a-zA-Z_][a-zA-Z0-9_]*", string):
                keyword = re.findall("^([a-zA-Z_][a-zA-Z0-9_]*)", string)[0]
                if keyword in self.PythonWordTokens_re.split():
                    Scanned.append((keyword, keyword.upper()))
                else:
                    # Wasn't a python keyword so it must be a user defined keyword
                    Scanned.append((keyword, "KEYWORD"))
                string = re.sub("^[a-zA-Z_][a-zA-Z0-9_]*", "", string)

            else:
                # if it is not a keyword of any kind then it comes to this reg exp section
                # in which finding it in one of these  loops prevents it from being searched
                # in the following loops
                Found = False

                # SYMBOL RECOGNITION
                for i in range(len(self.PythonSymbols_re.split())):
                    if re.findall(f"^{self.PythonSymbols_re.split()[i]}", string):
                        Scanned.append((re.findall(f"^{self.PythonSymbols_re.split()[i]}", string)[0], self.symbolicnames.split()[i]))
                        string = re.sub(f"^{self.PythonSymbols_re.split()[i]}", "", string)
                        Found = True
                        break

                # RECOGNITION FOR SYMBOLS NOT HANDELABLE BY REGULAR EXPRESSIONS
                if not Found:
                    for i in range(len(self.PythonSymbols_eq.split())):
                        symbol, name = self.PythonSymbols_eq.split()[i], self.eq_symbolicnames.split()[i]
                        if string[0:len(symbol)] == symbol:
                            if Debug_print:
                                print("non-regexp symbol")
                            Scanned.append((symbol, name))
                            string = string[len(symbol):]
                            Found = True
                            break

                # RECOGNITION FOR WHITE SPACE
                if not Found:
                    index = -1
                    for i in self.WhiteSpace.split("|"):
                        index += 1
                        if re.findall(f"^{i}", string):
                            if Debug_print:
                                print("white space")
                            Scanned.append((re.findall(f"^{i}", string)[0], self.ws_names.split()[index]))
                            string = re.sub(f"^{i}", "", string)
                            Found = True
                            break

                # NUMBER RECOGNITION
                if not Found:
                    for i in self.number_regexp:
                        if re.findall(i, string):
                            if Debug_print:
                                print('number')
                            Scanned.append((re.findall(i, string)[0][0], "NUMBER"))
                            string = re.sub(i, "", string)
                            Found = True
                            break

                # COMMENT RECOGNITION
                if not Found:
                    if re.findall(self.comment_regexp, string):
                        if Debug_print:
                            print("comment")
                        Scanned.append((re.findall(self.comment_regexp, string)[0], "COMMENT"))
                        string = re.sub(self.comment_regexp, "", string)
                        Found = True

            if falss == string: # Debug check 1
                # if falss == string then string hasn't changed which means
                # no pattern recognizes the start of string so string hasn't been
                # altered,
                # this will result in the while endlessly looping so the break down
                # below will prevent that
                print("Possible scenario not having associated regexp: ") # Debug check 1
                if Debug_print:
                    print(f"__{string}__")
                break # Debug check 1

        return Scanned


    
    def match(self, TupleSyntaxFromScannedInput, Token):
        """Given a list of possible tokens (these tokens come from a scanned string), and a specific token to match against, return the first token in the given list and remove it, otherwise return None"""
        if TupleSyntaxFromScannedInput[0][1] == Token:
            return TupleSyntaxFromScannedInput.pop(0)

    def peek(self, TupleSyntaxFromScannedInput, Token):
        """Given a list of possible tokens (these tokens come from a scanned string), and a specific token to match against, return the first token in the given list, otherwise return None"""
        if TupleSyntaxFromScannedInput[0][1] == Token:
            return TupleSyntaxFromScannedInput[0]

    def push(self, TupleSyntaxFromScannedInput, Token): 
        """Push a token back on the token stream so that a later peek or match will return it."""
        TupleSyntaxFromScannedInput.append(Token)






PythonWordTokens_re = "from import global class object __init__ def if True False try except pass break next last and print or return else elif as"
PythonSymbols_re = "\. != <= >= == \+= -= < > = \[ \] \{ \} \( \) \+ : , \|"
PythonSymbols_eq = "\\"
quote_regexp = "^(f?)('''|\"\"\"|'|\")"
WhiteSpace = "\n|    |[ ]+"
comment_regexp = "^(#.*)"
number_regexp = ["^(-?([1-9]|\.)\d+(e\d+|e-\d+)?)", "^(-?[1-9]\d+\.?\d*(e\d+|e-\d+)?)", "^(-?[0-9](\.\d*)?(e\d+|e-\d+)?)"]
TokenNamesForSymbols = "DOT NOTEQ SMALL_OR_EQ GREAT_OR_EQ TWICEEQ PLUSEQ MINUSEQ LESS GREAT EQ LBRACK RBRACK LCBRACK RCBRACK LPAREN RPAREN PLUS COLON COMMA BAR"
eq_SymbolNames = "ESCAPE"
WhiteSpaceNames = "NEWLINE INDENT WS"




# Opening a file down here and getting the contents
handle1 = open("?????")
file_contents = handle1.read()
handle1.close()

# Initializing the scanner
scanner = Scanner(PythonWordTokens_re, PythonSymbols_re, PythonSymbols_eq, quote_regexp, WhiteSpace, comment_regexp, number_regexp, TokenNamesForSymbols, eq_SymbolNames, WhiteSpaceNames)
Rigid_Tuple_List = scanner.scan(file_contents)
