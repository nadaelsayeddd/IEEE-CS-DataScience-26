first_num = float(input("Num1: "))
second_num = float(input("Num2: "))
operator = input("Operator: ")
if operator == '+':
    result = first_num + second_num
elif operator == '-':
    result = first_num - second_num
elif operator == '*':
    result = first_num * second_num
elif operator == '/':
    result = first_num / second_num
    
print(result)