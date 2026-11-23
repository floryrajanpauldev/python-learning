"""
Dict - allowing to use key names rather than [0] and [1] index's 
Dictionaries are also mutable like list
"""

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

""" get_student can also be given as:
  return {"name": name, "house": house}
"""

if __name__ == "__main__":
    main()