"""
Use tuple when you don't want to change the values in a variable
Tuples are immutable - you cannot change the values - (name, house)
"""

def main():
    student = get_student()
    # Tuples are immutable - you cannot change the values
    #if(student[0] == "Padma"):
    #   student[1] = "Ravenclaw" #TypeError: 'tuple' object does not support item assignment
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house) #tuple
  
if __name__ == "__main__":
    main()