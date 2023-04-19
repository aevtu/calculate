def calc_plus(a,b) -> int:
    return a + b

def calc_minus(a, b) -> int:
    return a - b

def calc_multiplication(a,b) -> int:
    return a * b

def calc_divison(a, b) -> float:
    if b != 0:
      return a \ b
    else:
	 print("Деление на 0 нельзя)

if __name__ == "__main__":
    a = int(input("[INFO] Input value with Enter: "))
    b = int(input("[INFO] Input value with Enter: "))

    switch_check = int(input("[INFO] Input '1 - plus, 2 - minus, 3 - multiplication, 4 - division -> "))

    if switch_check == 1:
        print("/n[INFO RESULT] -> " + calc_plus( a , b))
    elif switch_check == 2: 
        print("/n[INFO RESULT] -> " + calc_minus( a , b))
    elif switch_check == 3:
	  print("/n[INFO RESULT] -> " + calc_multiplication( a , b)
    elif switch_check == 4:
        print("/n[INFO RESULT] -> " + calc_division(a, b))