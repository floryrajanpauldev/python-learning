name = input("What's your name? ")
address = input("What's your address? ")

with open("names-a-csv.csv", "a") as file:
    file.write(f"{name},{address}\n")    
