msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
memory = "0"
result = 0


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def add(x, y):
    return float(x) + float(y)


def subtract(x, y):
    return float(x) - float(y)


def multiply(x, y):
    return float(x) * float(y)


def divide(x, y):
    return float(x) / float(y)


def check_if_integer(arg1):
    if -10.0 < float(arg1) < 10.0:
        if "." in str(arg1):
            new_arg = ""
            index = str(arg1).index(".")
            for i in range(index + 1, len(str(arg1))):
                new_arg = str(new_arg) + str(arg1)[i]
            if float(new_arg) > 0.0:
                return False
            else:
                return True
        else:
            return True
    else:
        return False


def start():
    print(msg_0)
    calc = input()
    split_calc(calc)


def split_calc(message):
    global memory
    message = message.split()
    x = message[0]
    operator = message[1]
    y = message[2]
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    check_if_numbers(x, operator, y)


def check_if_numbers(arg1, operator, arg2):
    if not str(arg1).isnumeric() and not isfloat(str(arg1)) or not str(arg2).isnumeric() and not isfloat(str(arg2)):
        print(msg_1)
        start()
    else:
        check_operator(arg1, operator, arg2)


def check_operator(x, operator, y):
    check_if_lazy(x, operator, y)
    global result
    if operator == "+":
        result = add(x, y)
    elif operator == "-":
        result = subtract(x, y)
    elif operator == "*":
        result = multiply(x, y)
    elif operator == "/":
        if int(y) == 0:
            print(msg_3)
            start()
        else:
            result = divide(x, y)
    else:
        print(msg_2)
        start()

    print(result)
    save_result(result)


def check_if_lazy(arg1, operator, arg2):
    msg = ""
    if check_if_integer(arg1) and check_if_integer(arg2):
        msg = msg + msg_6
    if (float(arg1) == 1.0 or float(arg2) == 1.0) and operator == "*":
        msg = msg + msg_7
    if (float(arg1) == 0.0 or float(arg2) == 0.0) and operator in ("*", "+", "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def save_result(result):
    global memory
    print(msg_4)
    if input() == "y":
        if check_if_integer(result):
            print(msg_10)
            if input() == "y":
                print(msg_11)
                if input() == "y":
                    print(msg_12)
                    if input() == "y":
                        memory = result
                    else:
                        memory = memory
                else:
                    memory = memory
            else:
                memory = memory
        else:
            memory = result
    print(msg_5)
    if input() == "y":
        start()
    else:
        exit()



start()
