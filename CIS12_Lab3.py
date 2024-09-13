import lab_chat as lc

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
    return msg

def initialize_chat():
    usr = get_username("Enter Username: ")
    while not input_confirmation():
        usr = get_username("Enter Username: ")
    grp = get_group("Enter the group you wish to join: ")
    while not input_confirmation():
        grp = get_group("Enter the group you wish to join: ")
    print(f"You will be added to '{grp}'. Type to start chatting. Type '$$STOP' to leave the group.")
    node = lc.get_peer_node(usr)
    lc.join_group(node, grp)
    return lc.get_channel(node, grp)

def start_chat():
    channel = initialize_chat()
    while True:
        try:
            msg = get_message(f">")
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")

start_chat()