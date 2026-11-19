import math
operators = ["/", "*", "-", "+"]
signs = ["-", "+"]

def trig(expression, type):
    """the function that helps in solving trig only, this includes sin, cos, and tan. this function depends on the operations function
    for more flexibility"""

    if type == "sin":
        return round(math.sin(expression), 10)

def substitueConst(n):
    """
    this is a helper function that def constants will use.
    this is used by the developer only, that is why there is no debugging in this function.
    """
    if n == "e":
        return math.e
    else:
        return math.pi


def constants(expression):
    #TODO: make the function deal with things like 9e, 1/e, πe, and such
    """
    the function that calls the constants like pi and e
    
    the exact idea I am going to apply:
    For every π or e:

    Start of expression → valid constant
    Number on the left → insert *
    Constant on the left → insert *
    Operator on the left → leave it alone because the operator already separates the values

    So:

    9e   → 9*e
    2π   → 2*π
    πe   → π*e
    eπ   → e*π

    5+e  → 5+e
    8/π  → 8/π
    -e   → -e

    But:

    π3
    e5

    remain invalid because you do not create multiplication after a constant.
    """
    print(f"CONSTANTS START: {expression}")
    new_expression = ""
    FlagToSkipOneIteration = False
    for index, character in enumerate(expression):
        if FlagToSkipOneIteration:
            FlagToSkipOneIteration = False
            continue
        if character == "e" or character == "π":
            if index == 0:
                print(f"adding: {str(substitueConst(character))}")
                new_expression += str(substitueConst(character))
            elif expression[index-1].isdigit():
                print(f"adding: *{substitueConst(character)}")
                new_expression += f"*{substitueConst(character)}"
            elif expression[index-1] in ("e","π"):
                print(f"adding: {substitueConst(expression[index-1])}*{substitueConst(character)}")
                new_expression += f"{substitueConst(expression[index-1])}*{substitueConst(character)}"
                FlagToSkipOneIteration = True
                #skip one iteration cause the function will try to append the already appended 
                # e or pi to the expression, you know?
            elif expression[index-1] in operators:
                print(f"adding: {str(substitueConst(character))}")
                new_expression += str(substitueConst(character))
            
            else: raise SyntaxError("error in def constants")
        else:
            print(f"adding: {character}")
            new_expression += character

    print("new_expresion: ", new_expression)
    return new_expression
    

def logs():
    pass 
    """the funciton that solves log(x) and ln(x) only, this function depends on the operations function
    for more flexibility"""

def sqrt():
    pass
    """
    the function that returns the square root of the argument passed, this function depends on the operations function
    for more flexibility
    def exponentiation() could take this, since the root(n) = n^0.5
    """


def square():
    pass
    """
    the function that returns the squared value of the argument, this function depends on the operations function
    for more flexibility
    def exponentiation() could take this, since squaring n = n^2
    """

def exponentiation(expression):
    """
    the function that works like pow() in python, except that it should be able to use
    the operations function to allow flexibility

    the logic that is being followed on the recursion case:
    find the right-most ^, gather the first and second arg with their signs, the first arg stops on the index
    of the other ^ behind the right-most ^, replace by position, not value, and that is it, you replace by position
    here because replacing by value works on multiplication and division, and addition and subtraction, at least that
    is what I think of
    """
    print("EXPONENTIATION START: ", expression)
    expression = str(expression)

    operatorIndex = expression.rfind("^")
    print(f"operatorIndex = {operatorIndex}")
    operatorCount = expression.count("^")
    print(f"operatorCount = {operatorCount}")
    if operatorCount == 0:
        return expression
    if operatorCount == 1:
        print("about to float firstArg: ", expression[:operatorIndex])
        firstArg = float(expression[:operatorIndex])
        print("about to float secondArg: ", expression[operatorIndex+1:])
        secondArg = float(expression[operatorIndex+1:])
        print("operator check: ", expression[operatorIndex])
        operator = expression[operatorIndex]
        if operator == "^":
            return pow(firstArg, secondArg)
        else: raise SyntaxError("something weird happened in def exponentiation()")
    else:
        #essential prints to declare entering recursion, and things to debug
        print("\n--- exponentiation called ---")
        old_expression = expression
        print("expression:", expression)
        print("type:", type(expression))
        print("^ count:", expression.count("^"))
        operatorIndex = expression.rfind("^")
        otherOperatorIndex = expression.rfind("^", 0, operatorIndex)
        print("last ^ index: ",operatorIndex)
        print("before-last ^ index :",otherOperatorIndex)

        #recursion case
        print("about to float firstArg: ", expression[otherOperatorIndex+1:operatorIndex])
        firstArg = float(expression[otherOperatorIndex+1:operatorIndex])
        print("about to float secondArg: ", expression[operatorIndex+1:])
        secondArg = float(expression[operatorIndex+1:])
        print("operator check: ", expression[operatorIndex]) #just to see if everything is alright
        result = pow(firstArg, secondArg)

        #replacement
        lstOfExpression = []
        lstOfExpression.append(expression[:otherOperatorIndex+1])
        lstOfExpression.append(expression[otherOperatorIndex+1:])
        lstOfExpression[-1] = str(result)
        expression = "".join(lstOfExpression)

        return exponentiation(expression)



def DegreeConverter(expression, arg):
    """
    the function that converts the arg in the trig function only, to rad or deg
    this function is currently being used in the solve() function
    """
    #TODO: fix -0.0 display when testing with sin(2pi)
    if arg == "deg":
        res = float(expression) * (math.pi/180) 
        return res
    else: 
        res = float(expression)
        return res
    

def addAndSubtract(expression=str): #done
    """
    this is where I should recursively calculate added numbers, either they are positive 
    or negative, with no multiplication involved
    """
    dictOfOperations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
    }
    print("ENTER ADD/SUB:", expression)
    expression = str(expression)#the funciton gets the result of the expression, not the expression itself


    verifyLst = []
    x = ""
    flag = False
    oneNumber = False
    for i in expression:
        if i in [str(i) for i in range(10)] + ["."]:
            x += str(i)
            continue
        else:
            verifyLst.append(x)
            x = ""
    verifyLst.append(x)
    verifyLst = [item for item in verifyLst if item != ""]
    if len(verifyLst) == 2:
        flag = True
    elif len(verifyLst) == 1:
        flag = True
        oneNumber = True


    if flag: #base case
        if oneNumber:
            return expression
        if "+" in expression[1:]:
            theIndex = expression.find("+",1)
            print("ENTERED BASE CASE")
            print("expression:", expression)
            print("theIndex:", theIndex)
            print("firstArg text:", expression[:theIndex])
            print("secondArg text:", expression[theIndex+1:])
            if expression[:theIndex] == "": #this case will never be true at the base case
                firstArg = 0
            else:
                print(f"About to float firstArg: {expression[:theIndex]}")
                firstArg = float(expression[:theIndex])
            print(f"About to float secondArg: {expression[theIndex+1:]}")
            secondArg = float(expression[theIndex+1:])
            return dictOfOperations.get(expression[theIndex])(firstArg, secondArg)
        elif "-" in expression[1:]:
            theIndex = expression.find("-",1)
            print("ENTERED BASE CASE")
            print("expression:", expression)
            print("theIndex:", theIndex)
            print("firstArg text:", expression[:theIndex])
            print("secondArg text:", expression[theIndex+1:])
            operator = expression[theIndex]
            if expression[:theIndex] == "":
                firstArg = 0
            else:
                print(f"About to float firstArg: {expression[:theIndex]}")
                firstArg = float(expression[:theIndex])
            print(f"About to float secondArg: {expression[theIndex+1:]}")
            secondArg = float(expression[theIndex+1:])
            return dictOfOperations.get(operator)(firstArg, secondArg)
        

    else: #RECURSION IS HEREEEEEEEE
        print("\n--- addAndSubtract called ---")
        print("expression:", expression)
        print("type:", type(expression))
        print("plus count:", expression.count("+"))
        print("minus count:", expression.count("-"))
        print("first + index:", expression.find("+",1))
        print("first - index:", expression.find("-",1))


        plusIndex = expression.find("+",1)
        MinusIndex = expression.find("-",1)

        if plusIndex > -1 and MinusIndex > -1: #first case
            if plusIndex < MinusIndex:
                theIndex = plusIndex
            elif plusIndex > MinusIndex:
                theIndex = MinusIndex
        elif plusIndex == -1:
            theIndex = MinusIndex
        elif MinusIndex == -1:
            theIndex = plusIndex
        else:
            print("ERROR: Entered recursion when the experssion is just a number")
            raise SyntaxError

        operator = expression[theIndex]
        followingIndex = expression.find("+",theIndex+1)
        if followingIndex == -1:
            followingIndex = expression.find("-",theIndex+1) #  SEE HERE
            thePlusIndex = expression.find("+", theIndex + 1)
            print("thePlusIndex =", thePlusIndex)
            theMinusIndex = expression.find("-", theIndex + 1)
            print("theMinusIndex =", theMinusIndex)
        elif expression.find("-",theIndex+1) != -1:
            if followingIndex > expression.find("-",theIndex+1):
                followingIndex = expression.find("-",theIndex+1)
                thePlusIndex = expression.find("+", theIndex + 1)
                print("thePlusIndex =", thePlusIndex)

                theMinusIndex = expression.find("-", theIndex + 1)
                print("theMinusIndex =", theMinusIndex)
        print("theIndex =", theIndex)
        print("followingIndex =", followingIndex)
        print("firstArg text =", expression[:theIndex])
        print("secondArg text =", expression[theIndex+1:followingIndex])
        if expression[:theIndex] == "":
            firstArg = 0
        else:
            print("expression =", expression)
            print("theIndex =", theIndex)
            print("followingIndex =", followingIndex)
            print("firstArg slice =", expression[:theIndex])
            print("secondArg slice =", expression[theIndex+1:followingIndex])
            firstArg = float(expression[:theIndex])
        print("expression =", expression)
        print("theIndex =", theIndex)
        print("followingIndex =", followingIndex)
        print("firstArg slice =", expression[:theIndex])
        print("secondArg slice =", expression[theIndex+1:followingIndex])
        secondArg = float(expression[theIndex+1:followingIndex])
        
        expression = str(dictOfOperations.get(operator)(firstArg, secondArg)) + expression[followingIndex:]
        print("followingIndex:", followingIndex)
        print("new expression before recursion:", expression)
        return addAndSubtract(expression)
    

def multiplyAndDivide(expression=str): 
    
    """this is where I should recursively calculate multiplied numbers, either they are positive 
    or negative, while making the function know the sign of the arguments"""
    dictOfOperations = {
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    expression = str(expression)#the funciton gets the result of the expression, not the expression itself


    verifyLst = []
    x = ""
    flag = False
    oneNumber = False
    for i in expression:
        if i in [str(i) for i in range(10)] + ["."]:
            x += str(i)
            continue
        else:
            verifyLst.append(x)
            x = ""
    verifyLst.append(x)
    verifyLst = [item for item in verifyLst if item != ""]
    if len(verifyLst) == 2:
        flag = True
    elif len(verifyLst) == 1:
        flag = True
        oneNumber = True


    if flag: #base case
        if oneNumber:
            return expression
        elif "*" in expression:
            theIndex = expression.find("*")
            print(f"About to float firstArg: {expression[:theIndex]}")
            firstArg = float(expression[:theIndex])
            print(f"About to float secondArg: {expression[theIndex+1:]}")
            secondArg = float(expression[theIndex+1:])
            print(
                f"""firstArg: {firstArg}
secondArg: {secondArg}"""
            )
            return dictOfOperations.get(expression[theIndex])(firstArg, secondArg)
        elif "/" in expression:
            theIndex = expression.find("/")
            operator = expression[theIndex]
            print(f"About to float firstArg: {expression[:theIndex]}")
            firstArg = float(expression[:theIndex])
            print(f"About to float secondArg: {expression[theIndex+1:]}")
            secondArg = float(expression[theIndex+1:])
            print(
                f"""firstArg: {firstArg}
secondArg: {secondArg}"""
            )
            return dictOfOperations.get(operator)(firstArg, secondArg)
        

    else: #RECURSION IS HEREEEEEEEE
        print("\n--- multiplyAndDivide called ---")
        print("expression:", repr(expression))
        print("type:", type(expression))
        print("multiply count:", expression.count("*"))
        print("divide count:", expression.count("/"))
        print("first * index:", expression.find("*"))
        print("first / index:", expression.find("/"))
        old_expression = expression
        multiplyIndex = expression.find("*")
        divideIndex = expression.find("/")

        if multiplyIndex != -1 and divideIndex != -1:
            if divideIndex > multiplyIndex:
                theIndex = multiplyIndex
            else:
                theIndex = divideIndex
        elif multiplyIndex == -1:
            theIndex = divideIndex
        else:
            theIndex = multiplyIndex

        operator = expression[theIndex]
        followingIndex = expression.find("*",theIndex+1)
        if followingIndex == -1:
            followingIndex = expression.find("/",theIndex+1) #  SEE HERE
            theMultiplyIndex = expression.find("*", theIndex + 1)
            print("theMultiplyIndex =", theMultiplyIndex)
            theDivideIndex = expression.find("/", theIndex + 1)
            print("theDivideIndex =", theDivideIndex)
        elif expression.find("/",theIndex+1) != -1:
            if followingIndex > expression.find("/",theIndex+1):
                followingIndex = expression.find("/",theIndex+1)
                theMultiplyIndex = expression.find("*", theIndex + 1)
                print("theMultiplyIndex =", theMultiplyIndex)

                theDivideIndex = expression.find("/", theIndex + 1)
                print("theDivideIndex =", theDivideIndex)
        print("theIndex =", theIndex)
        print("followingIndex =", followingIndex)
        print("firstArg text =", expression[:theIndex])
        print("secondArg text =", expression[theIndex+1:followingIndex])
        if expression[:theIndex] == "":
            #error
            raise ValueError
        else:
            print("expression =", expression)
            print("theIndex =", theIndex)
            print("followingIndex =", followingIndex)
            print("firstArg slice =", expression[:theIndex])
            print("secondArg slice =", expression[theIndex+1:followingIndex])
            firstArg = float(expression[:theIndex])
        print("expression =", expression)
        print("theIndex =", theIndex)
        print("followingIndex =", followingIndex)
        print("firstArg slice =", expression[:theIndex])
        print("secondArg slice =", expression[theIndex+1:followingIndex])
        if followingIndex == -1:
            secondArg = float(expression[theIndex+1:])
        else:
            secondArg = float(expression[theIndex+1:followingIndex])
        expression = str(dictOfOperations.get(operator)(firstArg, secondArg)) + expression[followingIndex:]
        print("followingIndex:", followingIndex)
        print("new expression before recursion:", expression)
        if expression == old_expression:
            raise ValueError(
                f"addAndSubtract made no progress: {expression}"
            )
        else:
            return multiplyAndDivide(expression)



def operations(expression=str): 
    """
    trying to handle all the operations here, 
    still needing assisting functions for order and multiple numbers
    """

    print("OPERATIONS START:", expression, type(expression))
    expression = str(expression)
    while True:
        FlagToContinueOuterLoop = False
        FlagToContinue = False
        txt = ""
        counter = 0 #for detecting infinite loop and stopping it
        if "/" not in expression and "*" not in expression and "^" not in expression:
            return addAndSubtract(expression)
        else:
            # EXPONENTIATION LOOP
            #TODO: make: chained exponentiation, repeated exponent chunks, negative exponent edge cases, bracketed exponent chunks work
            NoExponent = True
            while NoExponent:
                FlagToContinueOuterLoop = False
                FlagToContinue = False
                FlagToStartFromBeginning = False
                txt = ""
                if "^" not in expression:
                    print("EXITED EXPONENTIATION LOOP")
                    print("expression:", expression)
                    print("FlagToContinue:", FlagToContinue)
                    print("FlagToContinueOuterLoop:", FlagToContinueOuterLoop)
                    print("txt:", repr(txt))
                    FlagToContinueOuterLoop = False
                    FlagToContinue = False 
                    NoExponent = False 
                    break
                else:
                    #declaration of nearest index
                    counter += 1
                    print("EXPONENT LOOP:", counter, expression)
                    if counter > 20:
                        print("STOPPED: infinite loop suspected")
                        break
                    
                    #your logic is missing something, in an expression like: 5+5^2^2, your logic is depending on /
                    #and / to find if the exponentiation expression is at the start or not, and treats the + and -
                    # as signs, if there is no / or *, then the + and - become operations, but you set your function
                    # so that if there is no * or /, the expression is at the start, without checking the + or -.
                    #other than that, your finding of the expression and txt adding is great!
                    #TODO: fix that issue
                    exponentOperatorIndex = expression.find("^")
                    nearestMultiplyIndex = expression.rfind("*", 0, exponentOperatorIndex)
                    nearestDivideIndex = expression.rfind("/", 0, exponentOperatorIndex)
                    if nearestMultiplyIndex != -1 and nearestDivideIndex != -1:
                        if nearestMultiplyIndex > nearestDivideIndex:
                            nearestOperatorIndex = nearestMultiplyIndex
                        elif nearestMultiplyIndex < nearestDivideIndex:
                            nearestOperatorIndex = nearestDivideIndex
                    else:
                        if nearestMultiplyIndex > -1:
                            nearestOperatorIndex = nearestMultiplyIndex
                        elif nearestDivideIndex > -1:
                            nearestOperatorIndex = nearestDivideIndex
                        else:
                            nearestOperatorIndex= 0
                    
                    #declaration of the starting flag
                    if nearestOperatorIndex == 0:
                        FlagToStartFromBeginning = True
                    else:
                        FlagToStartFromBeginning = False

                    print("FlagToStartFromBeginning", FlagToStartFromBeginning)

                    if not FlagToStartFromBeginning:
                        print("entered the branch where expression is in middle")
                        for index, character in enumerate(expression[nearestOperatorIndex+1:],start=nearestOperatorIndex+1):
                            if expression[0] in signs:
                                txt += character
                                print("LINE 527: txt = ", txt)
                                continue
                            if character not in operators:
                                txt += character
                                print("LINE 531: txt = ", txt)
                                continue
                            if character == expression[-1]:
                                expression = expression.replace(txt, str(exponentiation(txt)), 1)
                                FlagToContinue = True
                                break
                            else:
                                if expression[index-1] == "^":
                                    txt += expression[index-1]
                                    print("LINE 540: txt = ", txt)
                                else:
                                    expression = expression.replace(txt, str(exponentiation(txt)), 1)
                                    FlagToContinue = True
                                    break
                    else: 
                        print("entered the starting branch")
                        for index, character in enumerate(expression):
                            if expression[0] in signs:
                                txt += character
                                print("txt = ", txt)
                                continue
                            if character not in operators:
                                txt += character
                                print("txt = ", txt)
                                continue
                            if character == expression[-1]:
                                expression = expression.replace(txt, str(exponentiation(txt)), 1)
                                FlagToContinue = True
                                break
                            else:
                                if expression[index-1] == "^":
                                    txt += expression[index-1]
                                    print("txt = ", txt)
                                else:
                                    expression = expression.replace(txt, str(exponentiation(txt)), 1)
                                    FlagToContinue = True
                                    break
                    
                    if FlagToContinue:
                        continue
                    else:
                        if "^" in expression and txt != "":
                            expression = expression.replace(txt, str(exponentiation(txt)), 1)


            # MULTIPLICATION AND DIVISION LOOP
            NoMultiply = True
            counter = 0
            FlagToContinueOuterLoop = False
            FlagToContinue = False
            while NoMultiply: 
                txt = ""
                old_expression = expression
                if "*"  not in expression and "/" not in expression: #break the multiplication while loop
                    print("EXITED MULTIPLICATION LOOP")
                    print("expression:", expression)
                    print("FlagToContinue:", FlagToContinue)
                    print("FlagToContinueOuterLoop:", FlagToContinueOuterLoop)
                    print("txt:", repr(txt))
                    NoMultiply = False
                    FlagToContinueOuterLoop = False
                    FlagToContinue = False 
                    break

                else:
                    FlagToContinueOuterLoop = False
                    FlagToContinue = False
                    counter += 1
                    print("MULTIPLY LOOP:", counter, expression)
                    if counter > 20:
                        print("STOPPED: infinite loop suspected")
                        break
                    #first: multiplication
                    multiplyIndex = expression.find("*")
                    divideIndex = expression.find("/")
                    if multiplyIndex != -1 and divideIndex != -1:
                        if multiplyIndex > divideIndex:
                            theIndex = divideIndex
                        else:
                            theIndex = multiplyIndex
                    else:
                        if multiplyIndex == -1:
                            theIndex = divideIndex
                        else:
                            theIndex = multiplyIndex

                    FlagToStartFromBeginning = False

                    StartingPlusIndex = expression.rfind("+",0,theIndex)
                    StartingMinusIndex = expression.rfind("-",0,theIndex)
                    #StartingIndex declaration
                    if StartingPlusIndex > StartingMinusIndex:
                        StartingIndex = StartingPlusIndex
                    elif StartingPlusIndex < StartingMinusIndex:
                        StartingIndex = StartingMinusIndex
                    else:
                        FlagToStartFromBeginning = True


                    txt = ""
                    FlagToBreak = False
                    print("FlagToStartFromBeginning =", FlagToStartFromBeginning)



                    if not FlagToStartFromBeginning:
                        for i in expression[StartingIndex:]:
                            print("i =", repr(i))
                            if i == expression[StartingIndex:][0]:
                                print("i =", repr(i))
                                txt += i
                                print("txt =", txt)
                                continue
                            elif i == "*" or i == "/":
                                print("Branch entered")
                                y = expression.find(i,StartingIndex+1)
                                print("i =", repr(i))
                                txt += i
                                print("txt =", txt)
                                if expression[y+1] == "-":
                                    txt += "-"
                                    print("txt =", txt)
                                    for index, character in enumerate(expression[y+2:], start=y+2):
                                        if character == "-" or character == "+":
                                            if expression[index-1] == "*" or expression[index-1] == "/":
                                                txt += character
                                                continue
                                            else:
                                                print("txt =", txt)
                                                print("old expression, "+  expression)
                                                result = multiplyAndDivide(txt)
                                                if float(result) >= 0:
                                                    result = "+" + str(result)
                                                else:
                                                    pass
                                                expression = expression.replace(txt,str(result), 1)
                                                expression = expression.replace("+-", "-")
                                                expression = expression.replace("-+", "-")
                                                expression = expression.replace("--", "+")
                                                expression = expression.replace("++", "+")
                                                print("new expression, " + expression)
                                                txt = ""
                                                print("SETTING STOP OUTER NOW")
                                                FlagToBreak = True
                                                FlagToContinue = True
                                                break
                                        else:
                                            txt += character
                                            print("txt =", txt)
                                elif expression[y+1] == "+":
                                    txt += "+"
                                    print("txt =", txt)
                                    for index, character in enumerate(expression[y+2:], start=y+2):
                                        if character == "-" or character == "+":
                                            if expression[index-1] == "*" or expression[index-1] == "/":
                                                txt += character
                                                continue
                                            else:
                                                print("txt =", txt)
                                                print("old expression, "+  expression)
                                                result = multiplyAndDivide(txt)
                                                if float(result) >= 0:
                                                    result = "+" + str(result)
                                                else:
                                                    pass
                                                expression = expression.replace(txt,str(result), 1)
                                                expression = expression.replace("+-", "-")
                                                expression = expression.replace("-+", "-")
                                                expression = expression.replace("--", "+")
                                                expression = expression.replace("++", "+")
                                                print("new expression, " + expression)
                                                txt = ""
                                                print("SETTING STOP OUTER NOW")
                                                FlagToBreak = True
                                                FlagToContinue = True
                                                break
                                        else:
                                            txt += character
                                            print("txt =", txt)
                                else: 
                                    #keep adding the multiplication expression to txt
                                    #untill it ends or there is an operation of - or + after it 
                                    for index, character in enumerate(expression[y+1:], start=y+1):
                                        if character == "-" or character == "+":
                                            if expression[index-1] == "*" or expression[index-1] == "/":
                                                txt += character
                                                continue
                                            else:
                                                print("txt =", txt)
                                                print("old expression, "+  expression)
                                                result = multiplyAndDivide(txt)
                                                if float(result) >= 0:
                                                    result = "+" + str(result)
                                                else:
                                                    pass
                                                expression = expression.replace(txt,str(result), 1)
                                                expression = expression.replace("+-", "-")
                                                expression = expression.replace("-+", "-")
                                                expression = expression.replace("--", "+")
                                                expression = expression.replace("++", "+")
                                                print("new expression, " + expression)
                                                txt = ""
                                                print("SETTING STOP OUTER NOW")
                                                FlagToBreak = True
                                                FlagToContinue = True
                                                break
                                        if character == expression[y+1:][-1]: #and "+" not in expression[y+1:] and "-" not in expression[y+1:]:
                                            #this condition prevents appending extra * by raising a flag to break the outer loop
                                            txt += character
                                            print("txt =", txt)
                                            FlagToBreak = True
                                        else:
                                            txt += character
                                            print("txt =", txt)
                                print("CHECKING STOP OUTER:", FlagToBreak)
                            if FlagToBreak == True:
                                print("Breaking The for loop...")
                                break
                            if i not in ["+", "-"]:
                                print("i =", repr(i))
                                txt += i
                                print("txt =", txt)
                            else:
                                print("Entered the else statement of the for loop (FlagToStart = False)")
                                old_expression = expression
                                result = multiplyAndDivide(txt)
                                if float(result) >= 0:
                                    result = "+" + str(result)
                                else:
                                    pass
                                expression = expression.replace(txt,str(result), 1)
                                expression = expression.replace("+-", "-")
                                expression = expression.replace("-+", "-")
                                expression = expression.replace("--", "+")
                                expression = expression.replace("++", "+")
                                print("txt:", txt)
                                print("old:", old_expression)
                                print("new:", expression)
                                txt = ""
                                FlagToContinue = True
                                break
                    else: 
                        # done
                        for i in expression: 
                            #making txt, didn't pass it to multiplyanddivide in this for loop
                            print("i =", repr(i))
                            if i == "*" or i == "/":
                                print("Branch entered")
                                y = expression.find(i)
                                txt += i
                                if expression[y+1] == "-":
                                    txt += "-"
                                    print("txt =", txt)
                                    for index, character in enumerate(expression[y+2:], start=y+2):
                                        if character == "-" or character == "+":
                                            if expression[index-1] == "*" or expression[index-1] == "/":
                                                txt += character
                                                continue
                                            else:
                                                print("txt =", txt)
                                                print("old expression, "+  expression)
                                                result = multiplyAndDivide(txt)
                                                if float(result) >= 0:
                                                    result = "+" + str(result)
                                                else:
                                                    pass
                                                expression = expression.replace(txt,str(result), 1)
                                                expression = expression.replace("+-", "-")
                                                expression = expression.replace("-+", "-")
                                                expression = expression.replace("--", "+")
                                                expression = expression.replace("++", "+")
                                                print("new expression, " + expression)
                                                txt = ""
                                                print("SETTING STOP OUTER NOW")
                                                FlagToBreak = True
                                                FlagToContinue = True
                                                break
                                        else:
                                            txt += character
                                            print("txt =", txt)
                                elif expression[y+1] == "+":
                                    txt += "+"
                                    print("txt =", txt)
                                    for index, character in enumerate(expression[y+2:], start=y+2):
                                        if character == "-" or character == "+":
                                            if expression[index-1] == "*" or expression[index-1] == "/":
                                                txt += character
                                                continue
                                            else:
                                                print("txt =", txt)
                                                print("old expression, "+  expression)
                                                result = multiplyAndDivide(txt)
                                                if float(result) >= 0:
                                                    result = "+" + str(result)
                                                else:
                                                    pass
                                                expression = expression.replace(txt,str(result), 1)
                                                expression = expression.replace("+-", "-")
                                                expression = expression.replace("-+", "-")
                                                expression = expression.replace("--", "+")
                                                expression = expression.replace("++", "+")
                                                print("new expression, " + expression)
                                                txt = ""
                                                print("SETTING STOP OUTER NOW")
                                                FlagToBreak = True
                                                FlagToContinue = True
                                                break
                                        else:
                                            txt += character
                                            print("txt =", txt)
                                else: 
                                    #keep adding the multiplication expression to txt
                                    #untill it ends or there is an operation of - or + after it 
                                    for index, character in enumerate(expression[y+1:], start=y+1):
                                        if character == "-" or character == "+":
                                            if expression[index-1] == "*" or expression[index-1] == "/":
                                                txt += character
                                                continue
                                            else:
                                                print("txt =", txt)
                                                print("old expression, "+  expression)
                                                result = multiplyAndDivide(txt)
                                                if float(result) >= 0:
                                                    result = "+" + str(result)
                                                else:
                                                    pass
                                                expression = expression.replace(txt,str(result), 1)
                                                expression = expression.replace("+-", "-")
                                                expression = expression.replace("-+", "-")
                                                expression = expression.replace("--", "+")
                                                expression = expression.replace("++", "+")
                                                print("new expression, " + expression)
                                                txt = ""
                                                print("SETTING STOP OUTER NOW")
                                                FlagToBreak = True
                                                FlagToContinue = True
                                                break
                                        if character == expression[y+1:][-1]: #and "+" not in expression[y+1:] and "-" not in expression[y+1:]:
                                            #this condition prevents appending extra * by raising a flag to break the outer loop
                                            txt += character
                                            print("txt =", txt)
                                            FlagToBreak = True
                                        else:
                                            txt += character
                                            print("txt =", txt)
                                print("CHECKING STOP OUTER: ", FlagToBreak)
                            if FlagToBreak == True:
                                print("Breaking The For loop (multiplication expression is at front)")
                                break
                            else: 
                                #error here, enters else statment after replacement
                                #error fixed by adding break at end of the statement
                                print("entered the else statement of the for loop")
                                old_expression = expression
                                txt += i
                                print("txt:", repr(txt))

                print(f"AFTER FOR, txt = {repr(txt)}")
                print("FlagToContinue =", FlagToContinue)
                print("FlagToContinueOuterLoop =", FlagToContinueOuterLoop)
                if FlagToContinue:
                    FlagToContinueOuterLoop = True
                else:
                    print("BEFORE EXTRA IF")
                    print("expression now:", expression)
                    print("txt now:", txt)
                    print("has star:", "*" in expression)
                    print("ABOUT TO REPLACE SECOND CHUNK")
                    print("txt:", repr(txt))
                    print("txt in expression:", txt in expression)
                    print("expression:", expression)
                    if "*" in expression or "/" in expression: 
                        old_expression = expression
                        result = multiplyAndDivide(txt)
                        if result > 0:
                            result = "+" + str(result)
                        else:
                            pass
                        expression = expression.replace(txt,str(result), 1)
                        expression = expression.replace("+-", "-")
                        expression = expression.replace("-+", "-")
                        expression = expression.replace("--", "+")
                        expression = expression.replace("++", "+")
                        print("txt:", txt)
                        print("old:", old_expression)
                        print("new:", expression)
                        txt = ""
                        FlagToContinue = True
                if FlagToContinue:
                    FlagToContinueOuterLoop = True
            if FlagToContinueOuterLoop == True:
                continue




            print(f"expression before passing to addAndSubtract: {expression}")
            return addAndSubtract(expression)






    if "+" in expression or "-" in expression:
        pass 
        #return addAndSubtract(expression)
    

    if "^" in expression:
        pass
        #start
        # for i in operators:
        #     if expression.rfind(i,expression.rfind("^")+1) == -1:
        #         pass
        #     else:
        #         closestOperator.append(expression.rfind(i,expression.find("^")+1))
        
        # if closestOperator == []:
        #     start = 0
        #     closestOperator.clear()
        # else:
        #     start =  max(closestOperator)
        #     closestOperator.clear()

        # #end
        # for i in operators:
        #     if expression.find(i,expression.find("^")+1) == -1:
        #         pass
        #     else:
        #         closestOperator.append(expression.find(i,expression.find("^")+1))
        # if closestOperator == []:
        #     Modified_expression =expression[start+1:]
        #     closestOperator.clear()
        # else:
        #     end = min(closestOperator)
        #     Modified_expression = expression[start+1:end]
        #     closestOperator.clear()
    
    


def solve(expression, y):
    flag = True
    firstArg = 0
    arg = []

    try:
        for i in range(len(expression)):
            if expression[:3]in["sin", "cos", "tan", "log"]:#trig functions, ln/log, and the other functions like it
                if "π" in expression[4:-1] or "e" in expression[4:-1]:
                    if expression[-1] == ")":
                        expression = expression[:4] + str(operations(constants(expression[4:-1]))) + expression[-1]
                    else:
                        raise ValueError

                expression = expression[:4] + str(operations(expression[4:-1])) + expression[-1]
                

                if expression[:3] == "sin" and type(float(expression[4:-1])) == float:
                    if expression[-1] == ")":
                        result = DegreeConverter(expression[4:-1],y)
                        return trig(result, "sin")
                    else:
                        return "SyntaxErr: close bracket"

                elif expression[:3] == "cos" and type(float(expression[4:-1])) == float:
                    if expression[-1] == ")":
                        if y == "deg":
                            res = float(expression[4:-1]) * (math.pi / 180)
                        else:
                            res = float(expression[4:-1])
                        return round(math.cos(res), 10)
                    else:
                        return "SyntaxErr: close bracket"

                elif expression[:3] == "tan" and type(float(expression[4:-1])) == float:
                    if expression[-1] == ")":
                        if y == "deg":
                            res = float(expression[4:-1]) * (math.pi / 180)
                        else:
                            res = float(expression[4:-1])
                        return round(math.tan(res), 10)
                    else:
                        return "SyntaxErr: close bracket"

                elif expression[:3] == "log" and type(float(expression[4:-1])) == float:
                    if expression[-1] == ")":
                        return round(math.log10(float(expression[4:-1])), 10)
                    else:
                        return "SyntaxErr: close bracket"

            elif expression[:2] == "ln" and type(float(expression[3:-1])) == float:
                if expression[-1] == ")":
                    return round(math.log(float(expression[3:-1])), 10)
                else:
                    return "SyntaxErr: close bracket"
            #end of trig/ln/log block

            return operations(str(constants(expression))) #.lstrip("+") #the stripping is not intended, 
            # this is my first action that I took when I saw that some expressions give away the signs.
            # when I come to this project to finish it (someday), I would take care of that issue

    except ValueError as e:
        print("ERROR {ValueError}")
        print("last expression:", expression)
        print("actual error:", e)
        return "SyntaxErr"
    except SyntaxError as e:
        print("actual error:", e)
        return "SyntaxErr"
    except AttributeError as e:
        print("Error {AttributeError}")
        print("Error details: ", e)
        print("this is what I was talking about when I saw the output of operations() when I was just checking in on the project, the lstrip--which was just intended to take away the + sign--was used on a NoneType (return to L1033)")
    except OverflowError as e:
        print("Error {OverflowError}")
        print("Error details: ", e)
        print("the number was just too large it crashed out")
        return "The number is too big bro I can't load it :("
    except Exception as e:
        print("Error (A general error this time)")
        print("Actual Error: ", e)
        return "Ask Chatgpt bro idk"
    return "if you know you know"


#new things learned: 
# recursion
# debugging using print statement
# example:
# print("inside before operations:", inside)
#example:
    # operation_result = operations(inside)
    # print("operations result:", operation_result)

    # expression = expression[:4] + str(operations(expression[4:-1])) + expression[-1]
    # print("new expression:", expression)

# the .replace() function needs a str argument ,you cannot pass in any other datatype

# when the program freezes, know that there is a loop repeating infintely somewhere

# arguments you can pass in .find() or .rfind():
# expression.find(expressionToFind=str,start=int,end=int)
# OR  expression.rfind(expressionToFind=str,start=int,end=int)
# the start represents where to start the search, the end represents where you limit the search in the expression
# if you still understand, start and end work in this way:
# expression[start:end].find("expressionToFind")
# OR expression[start:end].rfind("expressionToFind")
# NOTE: .find() can take keyword arguments, but .rfind() takes positional arguments
# so trying to put keyword arguments in .rfind() will result in a type error

# the funciton repr() is good for debugging, it allows you to see the char in 'quotes'

# how if branches are read in python:
# take care that python reads the elif as a sub-branch to the original if statement, meaning that python
# will read from the original if and will go down till there is an elif that has a condition satisified, 
# and will go from the top again, this means that the other elif(s) won't get a chance to be checked,
# which means that any condition that is sub-branched (in an elif) to an original if won't be checked 
# instantly, this is an example that applies this knowledge: 
# go to the multiplication loop, the for loop which gathers txt:

# for i in expression: 
#     #making txt, didn't pass it to multiplyanddivide in this for loop
#     print("i =", repr(i))
#     if i == "*": (BRANCH ONE)
#         print("Branch entered")
#         y = expression.find(i)
#         txt += i
#         if expression[y+1] == "-":
#             txt += "-"
#             for n in expression[y+2:]:
#                 if n == "-" or n == "+":
#                     print("txt =", txt)
#                     print("old expression, "+  expression)
#                     expression = expression.replace(txt, str(multiplyAndDivide(txt)), 1)
#                     print("new expression, " + expression)
#                     txt = ""
#                     FlagToBreak = True
#                     FlagToContinue = True
# #                     break
#                 else:
#                     txt += n
#         elif expression[y+1] == "+":
#             txt += "+"
#             for n in expression[y+2:]:
#                 if n == "-" or n == "+":
#                     print("txt =", txt)
#                     print("old expression, "+  expression)
#                     expression = expression.replace(txt, str(multiplyAndDivide(txt)), 1)
#                     print("new expression, " + expression)
#                     txt = ""
#                     FlagToBreak = True
#                     FlagToContinue = True
#                     break
#                 else:
#                     txt += n
#         else: 
#             #keep adding the multiplication expression to txt
#             #untill it ends or there is an operation of - or + after it 
#             for n in expression[y+1:]:
#                 if n == "-" or n == "+":
#                     print("txt =", txt)
#                     print("old expression, "+  expression)
#                     expression = expression.replace(txt, str(multiplyAndDivide(txt)), 1)
#                     print("new expression, " + expression)
#                     txt = ""
#                     FlagToBreak = True
#                     FlagToContinue = True
#                     break
#                 elif n == expression[y+1:][-1]: 
#                     #this condition prevents appending extra * by raising a flag to break the outer loop
#                     txt += n
#                     FlagToBreak = True
#                 else:
#                     txt += n
#     elif FlagToBreak == True: (BRANCH TWO)
#         print("Breaking The For loop (multiplication expression is at front)")
#         break
#     else: 
#         #error here, enters else statment after replacement
#         #error fixed by adding break at end of the statement
#         print("entered the else statement of the for loop")
#         old_expression = expression
#         txt += i
#         print("txt:", repr(txt))

#this situation explains everything, when branch one is met, it goes into a for loop that is nested inside
#it, and in the inside loop, we are signaling to break the outside for loop, and we want it to be broken 
#immediatly, but notice (branch two) is using an elif statement, which doesn't make it an independent branch
#therefore, when the inner loop is broken, python will make another iteration from the top of the outer loop
#and then go down to the elif statement to execute it, which is slow and has risks (for example what if
# in the design there were other conditions preceding (branch two)?).
# the best fix is to turn (branch two) into an independent branch so that when python finishes the inner
# for loop, it reads the indepenent branch two immediatly, which breaks the outer for loop in an instant.

# flags set to false for a while loop:
# look at this code:
# flag = True
# while flag:
#     flag = False
#     print("hello")
# what do you think the output will be?
# the output won't be what you used to think, it won't stop at flag = False and not print
# the output is: hello
# this is beause when we set the bolean that is in the while loop to be False, the loop doesn't break immediatly
# instead, the loop continues the iteration until it ends, and the next iteration isn't done cause then the setting 
# of the bolean will take effect
# real example in the project:
# NoMultiply = True
# while NoMultiply: 
#     txt = ""
#     old_expression = expression
#     if "*"  not in expression and "/" not in expression: #break the multiplication while loop
#         print("EXITED MULTIPLICATION LOOP")
#         print("expression:", expression)
#         print("FlagToContinue:", FlagToContinue)
#         print("FlagToContinueOuterLoop:", FlagToContinueOuterLoop)
#         print("txt:", repr(txt))
#         NoMultiply = False
#         FlagToContinueOuterLoop = False
#         FlagToContinue = False 
#         break
#     else:
#         #gathering the apparent multplication expression and passing it to divideAndMultiply()

#if we want the multplication loop to be broken immediatly, making NoMultiply = False won't guarantee that
# this is because python will continue the iteration and breaks the loop the next iteration
# we need to break immediatly, so we used break after making NoMultiply = False

# enumerate() function


#prototype for operator precedence
# MultiplyOperatorIndex = expression.find("*")
#             MultiplyOperatorIndex_fromBehind = expression.find("*", )
#             DivideOperatorIndex = expression.find("/")
#             if DivideOperatorIndex == -1:
#                 plus = expression.rfind("+", MultiplyOperatorIndex)
#                 plusFromBehind = expression.find("+")
#                 minus = expression.rfind("-", MultiplyOperatorIndex)
#                 minusFromBehind = expression.rfind("-")



# prototype 2 for operator precedence:
# noMultiplyorDivide = False
#         while noMultiplyorDivide:
#             flag = True
#             OperatorIndex = [].
#             OperatorIndex.append(expression.find("*"))
#             for i in range(len(OperatorIndex)):
#                 if OperatorIndex[-1] == expression.find("*",OperatorIndex[-1])-2:
#                     OperatorIndex.append(expression.find("*",OperatorIndex[-1]))
#                 else: 
#                     # TODO: finish operator precedene
#                     # it should be able to calculate
#                     # 5*5*5*10+5-5-5+5*5*5*5+5+5


# prototype for fixing expression.find("-") = -1 or expression.find("+") = -1
# if plusIndex != -1: 
        #     theIndex = plusIndex
        # else:
        #     if MinusIndex == -1:
        #         print("ERROR: Entered recursion when the experssion is just a number")
        #     else:
        #         theIndex == MinusIndex

#old instance of def solve()
# else:
#                     # DIVISION LOOP
#                     NoDivide = True
#                     while NoDivide:
#                         print("entered division loop (that part in which we don't compute dividing)")
#                         FlagToContinueOuterLoop = False
#                         FlagToContinue = False
#                         txt = ""
#                         if "/"  not in expression:
#                             NoDivide = False
#                             break
#                     else:
#                         print("entered the technical part of the division loop")
#                         FlagToContinueOuterLoop = False
#                         FlagToContinue = False
#                         txt = ""
#                         theIndex = expression.find("/")
#                         #for the FOR LOOP
#                         x = 0
#                         FlagToStartFromBeginning = False
#                         for i in ["+", "-"]:
#                             StartingIndex = expression.rfind(i,0,theIndex)
#                             if StartingIndex == -1:
#                                 x +=1
#                                 continue
#                             elif x == 2:
#                                 FlagToStartFromBeginning = True
#                                 break
                        
#                         txt = ""
                        
#                         print("FlagToStartFromBeginning =", FlagToStartFromBeginning)
#                         if not FlagToStartFromBeginning:
#                             for i in expression[StartingIndex+1:]:
#                                 if i == "*":
#                                     y = expression.find(i,StartingIndex+1)
#                                     txt += i
#                                     if expression[y+1] == "-":
#                                         txt += "-"
#                                         for n in expression[expression.find(i,StartingIndex+1)+1:]:
#                                             if n == "-" or n == "+":
#                                                 break
#                                             else:
#                                                 txt += n
#                                 if i not in ["+", "-"]:
#                                     txt += i
#                                 else:
#                                     old_expression = expression
#                                     expression = expression.replace(txt, str(multiplyAndDivide(txt)), 1)
#                                     print("txt:", txt)
#                                     print("old:", old_expression)
#                                     print("new:", expression)
#                                     txt = ""
#                         else:
#                             for i in expression:
#                                 if i == "*":
#                                     print("Branch entered")
#                                     y = expression.find(i)
#                                     txt += i
#                                     if expression[y+1] == "-":
#                                         txt += "-"
#                                         for n in expression[y+2:]:
#                                             if n == "-" or n == "+":
#                                                 print("txt =", txt)
#                                                 break
#                                             else:
#                                                 txt += n
#                                 if i not in ["+", "-"]:
#                                     txt += i
#                                 else:
#                                     old_expression = expression
#                                     expression = expression.replace(txt, str(multiplyAndDivide(txt)), 1)
#                                     print("txt:", txt)
#                                     print("old:", old_expression)
#                                     print("new:", expression)
#                                     txt = ""
#                                     break
                        
#                         if "/" in expression: 
#                             old_expression = expression
#                             expression = expression.replace(txt, str(multiplyAndDivide(txt)), 1)
#                             print("txt:", txt)
#                             print("old:", old_expression)
#                             print("new:", expression)
#                             txt = ""

# if flag == False:
            #     pass
            # elif expression[i] in operators:
            #     firstArg = float(expression[:i])
            #     arg.append(expression[i])
            #     flag = False
            #     continue

            # if expression[i] in ["-", "+"]:
            #     arg.append(expression)

            # elif expression[i] in ["*", "/"]:
            #     raise ValueError