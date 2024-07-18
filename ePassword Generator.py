import random
import string
while True:
    print("\n======= Password Generator =======")
    len=int(input("\nEnter the length of the desired password: "))
    com=input("Enter the desired complexity (low/medium/high): ")
    if com=="low":
        a=random.choices(string.ascii_letters, k=len)
        a=''.join(a)
        print(f'The generated password is--> "{a}"')
    if com=="medium":
        a=random.choices(string.digits+string.ascii_letters, k=len)
        a=''.join(a)
        print(f'The generated password is--> "{a}"')
    if com=="high":
        a=random.choices(string.punctuation+string.ascii_letters+string.digits, k=len)
        a=''.join(a)
        print(f'The generated password is--> "{a}"')
    b=input("Generate another?(y/n):")
    if b=='y':
        continue
    else:
        break    


