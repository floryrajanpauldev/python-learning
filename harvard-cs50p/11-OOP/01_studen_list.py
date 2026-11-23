"""
But lists are mutable - [name, house] 
"""

def main():
    student = get_student()
    # Lists are mutable - you can change the values
    if(student[0] == "Padma"):
        student[1] = "Ravenclaw"  #value of house can be changed in list

    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house] #List

if __name__ == "__main__":
    main()