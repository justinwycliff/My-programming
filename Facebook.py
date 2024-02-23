#logging into my facebook account
email_address = "justin12@gmail.com"
password = "12345678"

user_email = input("enter email adress")

user_password = input("enter password")

if (email_address == user_email and password == user_password ):
    print("logged in")

elif (len(user_password) < 8) :
    print("your password must be at least 8 character long")

else :
    print("invalid credentials")
