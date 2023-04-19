def calc_plus(a,b) -> int:
    return a + b

def calc_minus(a, b) -> int:
    return a - b


if __name__ == "__main__":
    a = int(input("[INFO] Input value with Enter: "))
    b = int(input("[INFO] Input value with Enter: "))

    switch_check = int(input("[INFO] Input '1 - plus, 2 - minus, 3 - multiplication, 4 - division -> "))

    if switch_check == 1:
        print("/n[INFO RESULT] -> " + calc_plus( a , b))
    elif switch_check == 2: 
        print("/n[INFO RESULT] -> " + calc_minus( a , b))
    