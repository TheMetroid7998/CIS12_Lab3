import lab_chat as lc

def input_confirmation(conf):
    conf = input("Is this correct? Y/N: ").strip().upper()
    while True:
        if conf == 'N':
            get_input("OK. Please re-enter your desired text or press Enter to continue: ")
        elif conf == 'Y':
            print("Choice confirmed.")
            return
        else: #conf != 'Y' and conf != 'N':
            print("That's not a valid input. Enter either 'Y' for yes or 'N' for no to confirm your choice.")
            conf = input("Is this correct? Y/N: ").strip().upper()
            return conf

def get_input(message):
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
        print(f"{usr}: {msg}")
        return msg
    elif msg == 'exit_now':
        print("""
You are about to leave this group. Are you sure?
If this was done accidentally, input 'N', press Enter, and input 'Y' to return to the chat.
""")
    return msg

# actual code starts here

get_input("Enter Username: ")
input_confirmation(get_input)

get_group("Enter the group you wish to join: ")
input_confirmation(get_group)
print(f"You have now entered group '{grp}'. Type anything to start chatting. Type 'exit_now' to leave the group.")

while True:
    get_message(">")
    continue

print("success! the program has not crashed. semantic errors may still remain.")