num = []
while True:
    i = input("Enter a number (or press Enter to stop): ")
    if i == "":
        print("Quitting the program")
        break
    num.append(int(i))
if num:
    print(min(num), "is the least number")
    print(max(num), "is the most number")
