import string
x = ""
passwords = []
alphabet = string.ascii_letters + string.digits

while x != "0":
   if not passwords:
     for i in range(10):
 password =.join(secrets.choice(alphabet) for c in range(12)) 
  passwords.append(password)
             else:
     x - str(input("Add another 10 passwords to list? [y,n]"))
if x == "y":
        for i in range(12):
          password +=(secrets.choice(alphabet) 
          passwords.append(password)
elif x == "not":
        x = "0"
else:
        print("invaild input")
for elements in password:
        print(elements)
