from Tokenizer.BooleanToken import BooleanToken
from Tokenizer.AdditionToken import AdditionToken
from Tokenizer.BreakToken import BreakToken
from Tokenizer.ClassToken import ClassToken
from Tokenizer.CommaToken import CommaToken
from Tokenizer.DivisionToken import DivisionToken
from Tokenizer.DotToken import DotToken
from Tokenizer.ElseToken import ElseToken
from Tokenizer.ExtendsToken import ExtendsToken
from Tokenizer.FalseToken import FalseToken
from Tokenizer.IdentifierToken import IdentifierToken
from Tokenizer.IfToken import IfToken
from Tokenizer.InitToken import InitToken
from Tokenizer.IntegerLiteralToken import IntegerLiteralToken
from Tokenizer.IntToken import IntToken
from Tokenizer.LeftCurlyBraceToken import LeftCurlyBraceToken
from Tokenizer.LeftParenToken import LeftParenToken
from Tokenizer.MethodToken import MethodToken
from Tokenizer.MultiplicationToken import MultiplicationToken
from Tokenizer.NewToken import NewToken
from Tokenizer.PrintlnToken import PrintlnToken
from Tokenizer.ReturnToken import ReturnToken
from Tokenizer.RightCurlyBraceToken import RightCurlyBraceToken
from Tokenizer.RightParenToken import RightParenToken
from Tokenizer.SemiColonToken import SemiColonToken
from Tokenizer.SingleEqualsToken import SingleEqualsToken
from Tokenizer.StringLiteralToken import StringLiteralToken
from Tokenizer.SubtractionToken import SubtractionToken
from Tokenizer.SuperToken import SuperToken
from Tokenizer.ThisToken import ThisToken
from Tokenizer.TrueToken import TrueToken
from Tokenizer.VoidToken import VoidToken
from Tokenizer.WhileToken import WhileToken
from Tokenizer.SymbolPair import SymbolPair
from Tokenizer.VarToken import VarToken
from Tokenizer.Token import Token
from Tokenizer._Lexer import Tokenizer
from Parser.TypesAndNames.MethodName import MethodName
from Parser.TypesAndNames.ClassName import ClassName
from Parser.PrimaryExp import IntegerLiteral
from Parser.CommaVardec import CommaVardec
from Parser.Constructor import Constructor
from Parser.TypesAndNames.Type import IntType
from Parser.TypesAndNames.Type import BooleanType
from Parser.TypesAndNames.Type import VoidType
from Parser.MethodDef import MethodDef
from Parser.PrimaryExp import Variable
from Parser.PrimaryExp import StringLiteral
from Parser.PrimaryExp import ThisExp
from Parser.PrimaryExp import TrueExp
from Parser.PrimaryExp import FalseExp
from Parser.PrimaryExp import PrintlnExp
from Parser.PrimaryExp import NewObjectExp
from Parser.ClassDef import ClassDef
from Parser.CommaExp import CommaExp
from Parser.CallExp import CallExp
from Parser.MultExp import MultiplicationExp
from Parser.MultExp import DivisionExp
from Parser.Program import Program
from Parser.Vardec import Vardec
from Parser.AddExp import AdditionExp
from Parser.AddExp import SubtractionExp
from Parser.Statement import Assignment
from Parser.Statement import WhileLoop
from Parser.Statement import Break
from Parser.Statement import Return
from Parser.Statement import IfOptionalElse
from Parser.Statement import Block

class Parser:
    tokens: list
    position: int

    # Constructor
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.position = 0
        
    # Get next token function
    def get_next_token(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]  # Assuming tokens is a list of token instances
        else:
            raise Exception(f"Error getting next token: end of input reached at position {self.position}")
            
        
    # Match token function
    def match(self, expected_token: Token):
        current_token = self.get_next_token()
        if isinstance(expected_token, type): # Check if expected_token is a type
            # match instance of current token to expected token type
            if isinstance(current_token, expected_token):
                if self.position != len(self.tokens) - 1:
                    self.position += 1
                return current_token
            else:           # expected identifier but found dot token
                raise ValueError(f"Syntax error: expected {expected_token}, but found {type(current_token).__name__}")
        else:
            # Match the current token to expected token instance
            if current_token == expected_token:
                if self.position != len(self.tokens) - 1:
                    self.position += 1
                return current_token
            else:
                raise ValueError(f"Syntax error: expected {expected_token}, but found {current_token}")
        
    # Parsing functions for each production rule
    def type_parse(self):
        token = self.get_next_token()
        match token:
            case IntToken():
                self.position += 1
                return IntType()
            case BooleanToken():
                self.position += 1
                return BooleanType()
            case VoidToken():
                self.position += 1
                return VoidType()
            case IdentifierToken() as identifier_token:
                self.position += 1
                return ClassName(identifier_token.name)
            case _:
                raise Exception(f"Error parsing type: {token} at position {self.position}")
                
        
    def comma_exp_parse(self):
        expressions = []
        while self.position < len(self.tokens):
            expression = self.exp_parse()
            expressions.append(expression)

            # Check if there's a comma after the expression
            if isinstance(self.tokens[self.position], CommaToken):
                self.match(CommaToken)  # Consume the comma token
                if self.position == len(self.tokens) - 1:
                    expression = self.exp_parse()
                    expressions.append(expression)
                    break
            else:
                break
                
        return CommaExp(expressions)

        
    def primary_exp_parse(self):
        token = self.get_next_token()
        if isinstance(token, IdentifierToken):
            self.match(IdentifierToken)
            return Variable(token.name)
        elif isinstance(token, StringLiteralToken): # get rid of this
            self.match(StringLiteralToken)  # Consume the token
            return StringLiteral(token.value)  # Return a StringLiteral object with the extracted value
        elif isinstance(token, IntegerLiteralToken):
            self.match(IntegerLiteralToken)  # Consume the token
            return IntegerLiteral(token.value) 
        elif isinstance(token, LeftParenToken):
            self.match(LeftParenToken)
            exp = self.exp_parse() 
            self.match(RightParenToken)
            return exp
        elif isinstance(token, ThisToken):
            self.match(ThisToken)
            return ThisExp()
        elif isinstance(token, TrueToken):
            self.match(TrueToken)
            return TrueExp()
        elif isinstance(token, FalseToken):
            self.match(FalseToken)
            return FalseExp()
        elif isinstance(token, PrintlnToken):
            self.match(PrintlnToken)
            self.match(LeftParenToken)
            exp = self.exp_parse()
            self.match(RightParenToken)
            return PrintlnExp(exp)
        elif isinstance(token, NewToken):       # problem here on new object expression
            self.match(NewToken)
            # need to add some way to check the name of the identifier in the parsing
            # "here's the identifier and it's name"
            classname_token = self.match(IdentifierToken)
            classname = ClassName(classname_token.name)
            self.match(LeftParenToken)
            variables = []
            if not isinstance(self.get_next_token(), RightParenToken):
                variables = self.comma_exp_parse()
            self.match(RightParenToken)
            return NewObjectExp(classname, variables) # added logic above
        else:
            raise ValueError(f"Unexpected token: {token}")
        
    def call_exp_parse(self):
        # Parse the primary expression
        exp = self.primary_exp_parse()
        
        while self.position < len(self.tokens):
            operator = self.get_next_token()
            if isinstance(operator, DotToken):
                # Consume the dot token
                self.position += 1

                # Parse the method name
                method = self.match(IdentifierToken)
                method_name = MethodName(method.name)
                
                # Parse the arguments
                self.match(LeftParenToken)
                args = self.comma_exp_parse()
                self.match(RightParenToken)
                
                # Create a CallExp node with the parsed expression, method name, and arguments
                exp = CallExp(exp, method_name, args)
            else:
                break
        return exp
        
    def mult_exp_parse(self):
        left_exp = self.call_exp_parse()

        while self.position < len(self.tokens):
            # Check if the next token is either '*'' or '/'
            operator = self.get_next_token()
            if isinstance(operator, MultiplicationToken) or isinstance(operator, DivisionToken):
                # Consume the operator token
                self.position += 1
                right_exp = self.call_exp_parse()

                if isinstance(operator, MultiplicationToken):
                    left_exp = MultiplicationExp(left_exp, "*", right_exp)
                else:  # operator == DivisionToken
                    left_exp = DivisionExp(left_exp, "/",  right_exp)
            else:
                break
        return left_exp

    def add_exp_parse(self):
        left_exp = self.mult_exp_parse()

        while self.position < len(self.tokens):
            # Check if the next token is either '+' or '-'
            operator = self.get_next_token()
            if isinstance(operator, AdditionToken) or isinstance(operator, SubtractionToken):
                # Consume the operator token
                self.position += 1
                right_exp = self.mult_exp_parse()

                if isinstance(operator, AdditionToken):
                    left_exp = AdditionExp(left_exp, "+", right_exp)
                else:  # operator == SubtractionToken
                    left_exp = SubtractionExp(left_exp, "-",  right_exp)
            else:
                break
        return left_exp
    
    def exp_parse(self):
        return self.add_exp_parse()

    def vardec_parse(self):
        var_type = self.type_parse()
        var_name = self.match(IdentifierToken)

        return Vardec(var_type, Variable(var_name.name, var_type))
    
    def assignment_parse(self):
        variable = self.match(IdentifierToken)
        self.match(SingleEqualsToken)

        expression = self.exp_parse()
        self.match(SemiColonToken)

        return Assignment(expression, Variable(variable.name))

    def while_parse(self):
        self.position += 1
        self.match(LeftParenToken)
        expression = self.exp_parse()
        self.match(RightParenToken)
        statement = self.statement_parse()

        return WhileLoop(expression, statement)
    
    def return_parse(self):
        self.position += 1 
        # can't use get next token, since if statement evaluates to false
        # when we return void, the length is 1, thus position is not < 1
        if isinstance(self.tokens[self.position], SemiColonToken):
            # Return statement without expression
            self.match(SemiColonToken)
            return Return(None)

        expression = self.exp_parse()
        self.match(SemiColonToken) 

        return Return(expression)

    def if_parse(self):
        self.position += 1

        self.match(LeftParenToken)

        expression = self.exp_parse()

        self.match(RightParenToken)

        statement = self.statement_parse()
        if isinstance(self.tokens[self.position], ElseToken):
            self.position += 1
            optional_statement = self.statement_parse()
            return IfOptionalElse(expression, statement, optional_statement)
        
        return IfOptionalElse(expression, statement, None)
    
    def block_parse(self):
        self.position += 1  # Move past the opening curly brace

        statements = []
        while not isinstance(self.get_next_token(), RightCurlyBraceToken):
            # Parse each statement within the block
            statement = self.statement_parse()
            statements.append(statement)

        self.match(RightCurlyBraceToken)  # Match the closing curly brace

        return Block(statements)


    def statement_parse(self):
         # Check the type of statement and parse accordingly
        if isinstance(self.get_next_token(), IdentifierToken) and not isinstance(self.tokens[self.position + 1], SingleEqualsToken):
            # Variable declaration statement with class name
            vardec = self.vardec_parse()
            self.match(SemiColonToken)  # Makes it a statement
            return vardec
        elif self.get_next_token() in [IntToken(), BooleanToken(), VoidToken()] and not isinstance(self.tokens[self.position + 1], SingleEqualsToken):
            # Variable declaration statement
            vardec = self.vardec_parse() # done
            self.match(SemiColonToken) # makes it a statement
            return vardec
        elif isinstance(self.get_next_token(), IdentifierToken):
            return self.assignment_parse() # done
        elif isinstance(self.get_next_token(), WhileToken):
            # While loop statement
            return self.while_parse()
        elif isinstance(self.get_next_token(), BreakToken):
            # Break statement
            self.match(BreakToken)
            self.match(SemiColonToken)
            return Break()
        elif isinstance(self.get_next_token(), ReturnToken):
            # Return statement
            return self.return_parse() # done
        elif isinstance(self.get_next_token(), IfToken):
            # If statement
            return self.if_parse() # done
        elif isinstance(self.get_next_token(), LeftCurlyBraceToken):
            # Block statement
            return self.block_parse() # done
        else:
            # If none of the above matches, raise an exception or handle accordingly
            raise ValueError(f"Unexpected token: {self.get_next_token()}")
        
    def comma_vardec_parse(self):
        var_decs = []

        while self.position < len(self.tokens):
            var_dec = self.vardec_parse()
            var_decs.append(var_dec)

            if isinstance(self.tokens[self.position], CommaToken):
                self.match(CommaToken)  # Consume the comma token
                if self.position == len(self.tokens) - 1:
                    var_dec = self.vardec_parse()
                    var_decs.append(var_dec)
                    break
            else:
                break

        return CommaVardec(var_decs)
        
    def method_def_parse(self):
        self.match(MethodToken)

        method = self.match(IdentifierToken)
        method_name = MethodName(method.name)

        self.match(LeftParenToken)

        parameters = []
        if not isinstance(self.get_next_token(), RightParenToken):
            parameters = self.comma_vardec_parse()
            
        self.match(RightParenToken)

        return_type = self.type_parse()

        self.match(LeftCurlyBraceToken)
        statements = []
        while not isinstance(self.get_next_token(), RightCurlyBraceToken):
            statement = self.statement_parse()
            statements.append(statement)
        self.match(RightCurlyBraceToken)

        return MethodDef(method_name, parameters, return_type, statements)

    def constructor_parse(self):
        self.match(InitToken)
        self.match(LeftParenToken)

        declarations = []
        if not isinstance(self.get_next_token(), RightParenToken):
            declarations = self.comma_vardec_parse()
        self.match(RightParenToken)
        self.match(LeftCurlyBraceToken)

        expressions = []
        # optional
        if isinstance(self.get_next_token(), SuperToken):
            self.match(SuperToken)
            self.match(LeftParenToken)
            if not isinstance(self.get_next_token(), RightParenToken):
                expressions = self.comma_exp_parse()
            
            self.match(RightParenToken)

            self.match(SemiColonToken)
        # optional


        statements = []
        while not isinstance(self.get_next_token(), RightCurlyBraceToken):
            # Parse each statement within the block
            statement = self.statement_parse()
            statements.append(statement)

        self.match(RightCurlyBraceToken)

        return Constructor(declarations, expressions, statements)

    

    #classdef ::= `class` classname [`extends` classname] `{`
    #  (vardec `;`)*
    #  constructor
    #  methoddef*
    #  `}`

    def class_def_parse(self):
        self.match(ClassToken)
        class_identifier = self.match(IdentifierToken)
        class_name = ClassName(class_identifier.name)
        superclass_name = None
        # needs an optional extends token
        if isinstance(self.get_next_token(), ExtendsToken):
            self.match(ExtendsToken)
            superclass_name_token = self.match(IdentifierToken)
            superclass_name = ClassName(superclass_name_token.name)

        self.match(LeftCurlyBraceToken)
        var_decs = []
        while not isinstance(self.get_next_token(), InitToken):
            # Parse variable declarations if encountered
            if self.get_next_token() in [IntToken(), BooleanToken(), VoidToken()]:
                var_decs.append(self.vardec_parse())
                self.match(SemiColonToken)
        # constructor
        constructor = self.constructor_parse()

        method_defs = []
        while not isinstance(self.get_next_token(), RightCurlyBraceToken):
            method_defs.append(self.method_def_parse())
        

        self.match(RightCurlyBraceToken)

        return ClassDef(class_name, superclass_name, var_decs, constructor, method_defs)

    # outer production rule is the program entry point
    def program_parse(self):
        class_defs = []
        while isinstance(self.get_next_token(), ClassToken):
            class_defs.append(self.class_def_parse())
        statements = []

        while self.position < len(self.tokens) - 1:
            statement = self.statement_parse()
            statements.append(statement)

        return Program(class_defs, statements)

    # ATTENTION!
    # self contains the tokens list and the position
    # you can call self.get_next_token() to get the next token
    # you can call self.match_token(token) to match a token

    # program ::= classdef* stmt+ 

    # classdef ::= 'class' classname ['extends' classname] '{' (vardec ';')* constructor methodddef* '}'

    # constructor ::= 'init' '(' comma_vardec ')' '{' ['super' '(' comma_exp ')' ';'] stmt* '}'

    # stmt ::= vardec ';' | var '=' exp ';' | 'while' '(' exp ')' stmt | etc....

    # exp ::= add_exp

    # add_exp ::= mult_exp (( '+' | '-' ) mult_exp)*

    # mult_exp ::= call_exp (( '*' | '/' ) call_exp)*

    # call_exp ::= primary_exp('.' methodname '(' comma_exp ')' )*

    # primary_exp ::= var | str | i | etc....

    # comma_exp ::= exp (',' exp)*

    #                     AST Example: Int x = 2 + 2
    #                          Program
    #                             |
    #                             |
    #                         Statement (var '=' exp)
    #                             |
    #                             |
    #                          add_exp
    #                            /  \
    #                           /    \
    #                    mult_exp     mult_exp
    #                        |            |
    #                        |            |
    #                    call_exp      call_exp
    #                        |            |
    #                        |            |
    #                  primary_exp   primary_exp
    #                        |            |
    #                        |            |
    #                       int          int