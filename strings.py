email = "Welcome to Python 101: Strings"

while True:
    user_input = input("Enter your End Point or 'q' to quit: ")
    end_point = email.find(user_input)
    if user_input == 'q':
        break
    else:
        print(email[0:end_point])

    modification = input("DO YOU WANT TO MODIFY YOUR STRING: ")
    if modification == "Yes":
        print("1 Welcome Ring to Tyler")
    elif modification == "q":
        break
