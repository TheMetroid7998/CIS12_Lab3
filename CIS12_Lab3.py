#import lab_chat as lc

def input_confirmation():
    conf = input("Is this correct? Y/N: ").strip().upper()
    while True:
        if conf == 'N':
            return False
        elif conf == 'Y':
            print("Choice confirmed.")
            return True
        else: #conf != 'Y' and conf != 'N':
            print("That's not a valid input. Enter either 'Y' for yes or 'N' for no to confirm your choice.")
            conf = input("Is this correct? Y/N: ").strip().upper()

def get_username(message):
    usr = str(input(f"{message}").strip().upper())
    print(f"You entered {usr}.")
    return usr

def get_group(message):
    grp = str(input(f"{message}").strip().upper())
    print(f"You entered {grp}.")
    return grp

def get_message(message):
    msg = str(input(f"{message}").strip())
    if msg != 'exit_now':
        print(f"{usr}: {msg}") # would have used {usr}
        return msg
    elif msg == 'exit_now':
        print("You are about to leave this group. Are you sure?")
        while not input_confirmation():
            print("Cancellation Confirmed. (But not really because I can't code.)")
            return msg
    return msg

#def initialize_chat():

usr = get_username("Enter Username: ")
while not input_confirmation():
    usr = get_username("Enter Username: ")

grp = get_group("Enter the group you wish to join: ")
while not input_confirmation():
    grp = get_group("Enter the group you wish to join: ")

print(f"You have now entered group '{grp}'. Type anything to start chatting. Type 'exit_now' to leave the group.")

while True:
    get_message(f">")
    continue

#print("success! the program has not crashed. semantic errors may still remain.")