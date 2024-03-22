# ClassToken, Left/RightCurlyBrace, SemiColon,
class TestClass {
  # InitToken, Var, SingleEquals, Println, IntegerLiteral
  init() {
    var a = 10;
    println("Variable 'a' initialized with value: " + a);
  }

  # AdditionToken, MethodToken, Left/RightParen, and ReturnToken
  method add(a, b) Int {
    return a + b;
  }

  # Subtraction
  method subtract(a, b) Int {
    return a - b;
  }

  # MultiplicationToken
  method multiply(a, b) Int {
    return a * b;
  }

  # DivisionToken
  method divide(a, b) Int {
    return a / b;
  }

  # Booleantoken, If, Else
  method isEqual(a, b) Boolean {
    if (a == b) {
      println("Values are equal");
      return true;
    } else {
      println("Values are not equal");
      return false;
    }
  }

  # True, False
  method isGreater(a, b) Boolean {
    if (a > b) {
      println(a + " is greater than " + b);
      return true;
    } else {
      println(a + " is not greater than " + b);
      return false;
    }
  }

  # While, Break
  method whileLoop() {
    var i = 0;
    while (i < 5) {
      println("Value of i: " + i);
      i = i + 1;
      if(i == 3) {
        break;
      }
    }
  }

  method ifElse(a) {
    if (a > 0) {
      println("Value of a is positive");
    } else if (a < 0) {
      println("Value of a is negative");
    } else {
      println("Value of a is zero");
    }
  }

  # Super, Void
  method superMethod() Void {
    super.methodToOvverride();
    println("This is the super method");
  }

  method main() {
    var a = 10;
    var b = 5;
    var result;

    result = this.add(a, b);
    println("Addition result: " + result);

    result = this.subtract(a, b);
    println("Subtraction result: " + result);

    result = this.multiply(a, b);
    println("Multiplication result: " + result);

    result = this.divide(a, b);
    println("Division result: " + result);

    # Comma
    var isEqual = this.isEqual(a, b);
    var isGreater = this.isGreater(a, b);

    # This, Dot
    this.whileLoop();

    this.ifElse(a);

    this.superMethod();
  }
}

class SubTestClass extends TestClass {
  methodToOverride() {
    println("This is the overridden method");
  }

  method main() {
    super.main();
    println("Executing main methods through SubTestClass");
  }
}

# Execution code, extending the main class but still showcasing it throw SubTestClass
# NewToken
var test = new SubTestClass();
test.main();
