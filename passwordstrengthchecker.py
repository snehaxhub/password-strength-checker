password = input("Enter your password: ")
print("Your password is:", password)

while password == "":
    password = print("are you blind?")
    password = input("Enter your password: ")
    
score = 0

if len(password)>= 8:
    score += 1
    
uppercase = False
lowercase = False
digits = False
specialchar = False

for char in password:
    if char.isupper():
        uppercase = True
    elif char.islower():
        lowercase = True
    elif char.isdigit():
        digits = True
    else:
        specialchar = True
        
score += uppercase + lowercase + digits + specialchar        

if score ==2:
    print("Password strength: Weak.\n Make sure it satisfies the criteria :\n lengtth of atleast 8 chars \n contains uppercase letters \n contains lowercase letter \n contains digits \n conatains special chars (@,#,&,*,$,^,%, etc)")
elif score ==3:
    print("Password strength: Medium.\n Halfway there!!\n Make sure it satisfies the criteria : \n lengtth of atleast 8 chars \n contains uppercase letters \n contains lowercase letter \n contains digits \n conatains special chars (@,#,&,*,$,^,%, etc)")
elif score ==5:
    print("Password strength: Strong. \n Excellent.")
else:
    print("Password strength: Very Weak. \n Try again with a stronger password that satisfies the criteria : lengtth of atleast 8 chars \n contains uppercase letters \n contains lowercase letter \n contains digits \n conatains special chars (@,#,&,*,$,^,%, etc)")