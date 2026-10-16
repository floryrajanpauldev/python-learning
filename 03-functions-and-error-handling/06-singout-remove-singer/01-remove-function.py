contacts = ["Freda", "Homer", "Chance"]
contacts.remove("Homer")
print(contacts)

#if you try to remove something that does not exist in the list then we get an error. 
#so we should first check if the name exists in the list and only then remove it else say the user is not in the list. 

contacts = ["Freda", "Homer", "Chance"]

def remove_contacts(contacts, name):
  for contact in contacts:
    if contact == name:
      contacts.remove(contact)
      print(f"Removed {name}.")
      return # return will exit if the condition matches and will prevent other code from running
  print(f"{name} isn't in your contacts.")

remove_contacts(contacts, "Homer")
remove_contacts(contacts, "Elisa")
