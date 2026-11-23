# Goal is to prompt users for theri twitter profile and extract the username from the twitter url

url = input("Enter your twitter profile: ").strip()

# here we'll try to ignore all that comes before the username 
# the twitter url looks like - https://twitter.com/username
#the username always comes to the end

username = url.replace("https://twitter.com/", "")
print(f"Username is : {username}")


#replace may not work, if the url is not give exactly the way we are trying to replace
e 