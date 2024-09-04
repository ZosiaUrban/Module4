n = "python"
p = "rules"
counter = 0
while counter < 5:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if n == username and p == password:
        print("Welcome")
        break
    else:
        counter += 1
        print("Incorrect username or password, please try again")

if counter == 5:
    print("access denied.")
