import string

import random

length =int(input("Enter something: "))

choice=int(input("enter choice: "))
if choice==1:
    pool= string.ascii_uppercase
elif choice==2:
    pool= string.digits
elif choice==3:
    pool= string.punctuation
else:
    print("Invalid choice")
    exit()
password = "".join(random.choice(pool) for i in range(length))
print("Generated password", password)
