users={
    "fay123":"secretpw",
    "shev789":"reallysecretpw",
    "ezra456":"obviouspw"
}
# Create a loop that does the following:
# If the user inputs “exit”, break out of the loop.
loggedin=[]
userinput=input("Do you want to login or exit? ")
if userinput=="login":
    name=input("Enter your username: ")
    if (name) in users.keys():
        pw=input("Enter your password: ")
        if users[name]==pw:
            print("You are now logged in.")
            loggedin.append(name)
        else:
            print("Incorrect password")
    else:
        signup=input("Would you like to sign up? (y/n)")
        if signup=="y":
            name=input("Create a username: ")
            if name in users: