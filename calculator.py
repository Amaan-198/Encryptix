while True:
    print("======= Calculator =======")
    print()
    print("1. Addition\n2. Subtraction\n3.Multiplication\n4.Division\n5.Percentage")
    choice=int(input("\nEnter you choice(1-5): "))
    print("=================")
    print()
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    if choice==1:
        c=a+b
        print("Addition is", c)
    elif choice==2:
        c=a-b
        print("Difference is", c)
    elif choice==3:
        c=a*b
        print("Product is", c)
    elif choice==4:
        c=a/b
        print("Division of", a, "with", b, "is", c)
    elif choice==5:
        c=a*100/b
        print(f"Percentage of {a} with {b} = {c}%")
    i=input("Want to do again(y/n)?: ")
    if i=='y':
        continue
    else:
        break
