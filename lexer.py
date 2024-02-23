import re
class lexer(object):
    def __init__(self, input_string):
        self.input_string = input_string
        self.tokens = []
        
    def tokenize(self):
        rules = [
            ('NUMBER', r'\d+'),
            ('OPERATOR', r'[+\-*/]')
        ]
        for rule_name, pattern in rules:
            for match in re.finditer(pattern, self.input_string):
                self.tokens.append((rule_name, match.group()))
                
    def print_tokens(self):
        for token in self.tokens:
            print(f"{token[0]}, {token[1]}")