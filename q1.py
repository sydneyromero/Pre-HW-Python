def hello_name(user_name):
    """Return a user name, neatly formatted."""
    full_name = user_name 
    return full_name.title()
    
while True:
    print("\nPlease tell me your user name:")
    print("(enter 'q' at any time to quit)")
    
    u_name = input("User Name: ")
    if u_name == 'q':
        break


    formatted_name = hello_name(u_name,)
    print("\nHello, " + formatted_name + "!")