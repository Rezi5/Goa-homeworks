#https://www.codewars.com/kata/5810085c533d69f4980001cf/train/python
def calculator(x, y, op):
    if (str(x).isdigit() or isinstance(x, float)) and (str(y).isdigit() or isinstance(y, float)):
        x, y = float(x), float(y) 
    else:
        return "unknown value" 
    
    
    
    if op == "+":
        return x + y
    elif op == "-":
        return x - y