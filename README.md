# Python-code-scanner
Takes in Python code, scans it, and outputs a list of tuples containing a string of the code, and a token that matches it

# The following code writes these first 4 lines to a file

def write_initial_lines():
    print("# Python-code-scanner\n")
    print("""Takes in Python code, scans it, and outputs a list of tuples containing a string of the code, and a token that matches it
    # The following code writes these first 4 lines to a  file
    """
    
When uploading the first 9 lines to a file and then using that as an input file for the scanner returns the following Tuple:
[('# Python-code-scanner', 'COMMENT'), ('\n', 'NEWLINE'), ('Takes', 'KEYWORD'), (' ', 'WS'), ('in', 'KEYWORD'), (' ', 'WS'), ('Python', 'KEYWORD'), (' ', 'WS'), ('code', 'KEYWORD'), (',', 'COMMA'), (' ', 'WS'), ('scans', 'KEYWORD'), (' ', 'WS'), ('it', 'KEYWORD'), (',', 'COMMA'), (' ', 'WS'), ('and', 'AND'), (' ', 'WS'), ('outputs', 'KEYWORD'), (' ', 'WS'), ('a', 'KEYWORD'), (' ', 'WS'), ('list', 'KEYWORD'), (' ', 'WS'), ('of', 'KEYWORD'), (' ', 'WS'), ('tuples', 'KEYWORD'), (' ', 'WS'), ('containing', 'KEYWORD'), (' ', 'WS'), ('a', 'KEYWORD'), (' ', 'WS'), ('string', 'KEYWORD'), (' ', 'WS'), ('of', 'KEYWORD'), (' ', 'WS'), ('the', 'KEYWORD'), (' ', 'WS'), ('code', 'KEYWORD'), (',', 'COMMA'), (' ', 'WS'), ('and', 'AND'), (' ', 'WS'), ('a', 'KEYWORD'), (' ', 'WS'), ('token', 'KEYWORD'), (' ', 'WS'), ('that', 'KEYWORD'), (' ', 'WS'), ('matches', 'KEYWORD'), (' ', 'WS'), ('it', 'KEYWORD'), ('\n', 'NEWLINE'), ('\n', 'NEWLINE'), ('# The following code writes these first 4 lines to a file', 'COMMENT'), ('\n', 'NEWLINE'), ('\n', 'NEWLINE'), ('def', 'DEF'), (' ', 'WS'), ('write_initial_lines', 'KEYWORD'), ('(', 'LPAREN'), (')', 'RPAREN'), (':', 'COLON'), ('\n', 'NEWLINE'), ('    ', 'INDENT'), ('print', 'PRINT'), ('(', 'LPAREN'), ('"# Python-code-scanner\\n"', 'STRING'), (')', 'RPAREN'), ('\n', 'NEWLINE'), ('    ', 'INDENT'), ('print', 'PRINT'), ('(', 'LPAREN'), ('"""Takes in Python code, scans it, and outputs a list of tuples containing a string of the code, and a token that matches it\n    # The following code writes these first 4 lines to a  file\n    """', 'STRING')]
