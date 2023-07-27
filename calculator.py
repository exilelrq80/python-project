calculator = True
while  calculator == True:
    # 1- input first number 
    while True:
        try:
            first_number = float(input("enter first number: ")) 
            break
        except ValueError:
            print("invalid input. plesea enter numeric value")
     
    # 2- input operation 
    while True:
        try:
         operation = input("enter operation type: ")
         if operation in ("-" , "+" , "*" , "/"):
          break 
         else:
            raise ValueError
        except ValueError:
           print("invalid operation, pleasa enter + , - , * , /")
        
    # 3- input second number 
    while True:
      try:
       second_number = float(input("enter second number: "))
       if second_number == 0 and operation == "/": # لازم الشرطين يتحققون  "and"
           raise ZeroDivisionError
       break 
      except ValueError:
          print("invalid input. plesea enter numeric value")
      except ZeroDivisionError:
          print("cannot divide by zero, pleasa enter anthor numeric value")
      
    
    # 4- print the result 
    if operation == "+" :
        result = first_number + second_number
    elif operation == "-" :
        result = first_number - second_number
    elif operation == "*" :
        result = first_number * second_number
    elif operation == "/" :
         result = first_number /  second_number
    

    if result != None:
         print("Result is:", result)

    while True:
     repeat = input("do you went to  perform anther operation (y/n):").lower()
     if repeat == "y":
        print("start again")
        break
     elif repeat == "n":
       print("program exited")
       calculator = False
       break
     else:
        print("pleasa answer for Q by (y/n):")
