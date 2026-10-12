
# Grade Calculator
# Use if, elif, and else to determine a student's grade.

test_score = 85

if test_score >= 90:
    print("A")
elif test_score >= 80:
    print("B")
elif test_score >= 70:
    print("C")
elif test_score >= 60:
    print("D")
else:
    print("F")


#if checks the first condition.
#elif checks another condition only if the previous conditions were false.
#else acts as the catch-all when no preceding condition is true.
#Order matters: check the highest grade first so a higher score isn't assigned a lower grade.