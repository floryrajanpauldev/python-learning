# Goal is to prompt users for theri twitter profile and extract the username from the twitter url
import re

url = input("Enter your twitter profile: ").strip()

# we tried replace(), but now let's try removeprefix() - which does not wor
#username = url.removeprefix("https://twitter.com/")

# Using re.sub (pattern, repl, string count flags=0)

username = re.sub(r"^https://twitter\.com/", "", url)
print(f"Username is : {username}")

"""
what if user types http:// or "My username is https://twitter...."
to fix that we can use ? after the "s" which means s may or maynot be occured
we are entering \. to ignore . and take the literal . 
same thing for www using ? and group - ( )
we are also making https:// optional using group ( ) and ? 

$ sign at the end
"""

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/$", "", url)
print(f"Username is : {username}")