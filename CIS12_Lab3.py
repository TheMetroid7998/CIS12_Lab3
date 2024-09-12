def input_confirmation(conf):
    conf = input("Is this correct? Y/N: ").strip().upper()
    while conf != 'Y' and conf != 'N':
        print("That's not a valid input. Enter either 'Y' for yes or 'N' for no to confirm your choice.")
        conf = input("Is this correct? Y/N: ").strip().upper()
    if conf == 'N':
        get_input("OK. Please re-enter your desired text or press Enter to continue: ")
    elif conf == 'Y':
        print("Choice confirmed.")
        return

def get_input(message):
    global usr
    usr = input(f"{message}").strip().upper()
    print(f"You entered {usr}.")
    input_confirmation(usr)

def get_group(message):
    global grp
    grp = input(f"{message}").strip().upper()
    print(f"You entered {grp}.")
    input_confirmation(grp)

def get_message(message):
    msg = input(f"{message}").strip()
    if msg != 'exit_now':
        print(f"{usr}: {msg}")
        return
    elif msg == 'exit_now':
        print("""
You are about to leave this group. Are you sure?
If this was done accidentally, input 'N', press Enter, and input 'Y' to return to the chat.
""")
        input_confirmation(msg)

get_input("Enter Username: ")
get_group("Enter the group you wish to join: ")
print(f"You have now entered group '{grp}'. Type anything to start chatting. Type 'exit_now' to leave the group.")

while True:
    get_message(">")
    continue

print("success! the program has not crashed. semantic errors may still remain.")