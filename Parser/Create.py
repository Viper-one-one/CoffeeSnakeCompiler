files = ["AccessExp.py",
"AccessLhs.py",
"AccessThisLhs.py",
"AssignStmt.py",
"BinaryOpExp.py",
"BoolType.py",
"BooleanLiteralExp.py",
"CallExp.py",
"ClassDef.py",
"ClassName.py",
"ClassType.py",
"ConsDef.py",
"Disjunct.py",
"Exp.py",
"IfStmt.py",
"IntLiteralExp.py",
"IntType.py",
"LessThanOp.py",
"Lhs.py",
"LogicalAndOp.py",
"LogicalOrOp.py",
"MethodDef.py",
"MethodName.py",
"MultOp.py",
"NewExp.py",
"Op.py",
"Param.py",
"ParseException.py",
"ParseResult.py",
"Parser.py",
"PlusOp.py",
"PrintStmt.py",
"PrognStmt.py",
"Program.py",
"ReturnStmt.py",
"Stmt.py",
"ThisExp.py",
"Type.py",
"VardecStmt.py",
"Variable.py",
"VariableExp.py",
"VariableLhs.py",
"WhileStmt.py"]

for filename in files:
    # Define the filename

    # Create and open the file in write mode ('w')
    with open(filename, 'w') as file:
        # Write some content to the file (optional)
        file.write("")

    print(f"File '{filename}' created.")