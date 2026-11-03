def main():
    user_color = input("What's your favorite color? Your options are red, green, or blue: ").lower()
    match user_color:
        case "red":
            print("Red is a great color!")
        case "green":
            print("Green is a great color!")
        case "blue":
            print("Blue is a great color!")
        case _:
            print("That's an interesting color!") # underscore is a catch-all for any other input that doesn't match the previous cases

main()