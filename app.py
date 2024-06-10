from calc_function import do_addition , do_subtraction
def main():
    print("welcome to calculator")
    print("select function from given opt 1 and 2")
    user_input=input("select the function")
    a=int(input("value of A"))
    b=int(input("value of B"))
    if user_input=='1':
        result = do_addition(a,b)
    elif user_input=='2':
        result = do_subtraction(a,b) 
    print('Result:',result)
if __name__=="__man__":
    main()