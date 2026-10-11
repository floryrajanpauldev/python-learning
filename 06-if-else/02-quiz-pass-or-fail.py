# Challenge: Quiz Pass or Fail

#

# You're building the results screen for an online

# course quiz. A student needs at least 60 points to pass.

#

# 1. Ask the student for their score and convert it to an int.

# 2. If their score is 60 or higher, print that they passed.

# 3. Otherwise, print that they didn't pass this time.

# Get the student's score.

# input() returns a string, so convert it to an integer

# using int().

score = int(input("Please enter your quiz score: "))

print(score)

# Check whether the student scored 60 or higher.

if score >= 60:
    print("Congratulations!!! You passed!")
else:
    print("You may have to try again next time - Failed")

# Example:

#

# Please enter your quiz score: 75

# 75

# Congratulations!!! You passed!

#

#

# Please enter your quiz score: 45

# 45

# You may have to try again next time - Failed
