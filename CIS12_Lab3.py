def input_confirmation(conf):
    conf = input("Is this correct? Y/N: ").strip().upper()
    while conf != 'Y' and conf != 'N':
        print("That's not a valid input. Please enter either 'Y' for yes or 'N' for no.")
        conf = input("Is this correct? Y/N: ").strip().upper()
    if conf == 'N':
        get_input("OK. Please re-enter your desired text: ")
    elif conf == 'Y':
        print("Choice confirmed.")
        return


def get_input(message):
    usr = input(f"{message}").strip().upper()
    print(f"You entered {usr}.")
    input_confirmation(usr)

get_input("Enter Username: ")
print("success!")