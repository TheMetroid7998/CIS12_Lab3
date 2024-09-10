print ("""
CIS-12 Chapter 3 Exercises
I don't know how to do the exception reporting mode in Python.
""")

def cont_conf(message):
    confirm = input(f"""{message}
""").strip().upper()
    return

def cont():
    if cont_conf("Press any key to continue: "):
        return

print ("Exercise 1")

def print_repeat(string, times):
    for _ in range(times):
            print(string)

print_repeat("cat", 2)
cont()

print ("""Exercise 2
I had to "cheat" and look at your example to get an idea what to do.
There is a better solution from the in-class section, but the code listed is my own code inspired by yours.
""")
def print_right(text, offset=40):
    offset = 40 - len(text)
    spaces = " "
    for s in range(offset):
        print(offset*spaces, text)
        break
print("""Alternate solution from class:
def print_right(text, offset=40):
    offset = 40 - len(text)
    spaces = ' '*offset
    print(spaces, text)
""")

print_right("Monty")
print_right("Python's")
print_right("Flying Circus")
cont()

print ("""Exercise 3""")

def triangle(string, height):
        for h in range(height):
            print(string*(h+1))

s_inp = str(input("Enter the character you want to draw: ")).strip().upper()
h_inp = int(input("Enter the height of your drawing: ").strip())
triangle(s_inp, h_inp)
cont()

print ("""
Exercise 4
Based off of the code/concepts from Exercise 3
""")

def rectangle(string, width, height):
    for r in range(height):
        print(string*width)

s_inp = str(input("Enter the character you want to draw: ")).strip().upper()
h_inp = int(input("Enter the height of your drawing: ").strip())
w_inp = int(input("Enter the width of your drawing: ").strip())
rectangle(s_inp, w_inp, h_inp)
cont()

print ("""Exercise 5""")

def bottle_verse(bottles):
    for n in range(bottles, 0, -1):
        print(f"""
    {n} bottle{' ' if n ==1 else 's '}of beer on the wall
    {n} bottle{' ' if n ==1 else 's '}of beer
    Take one down, pass it around
    {n-1} bottle{' ' if n ==1 else 's '}of beer on the wall
    """)

b_inp = int(input(f"""
How much do you want to day drink today?
""").strip())
bottle_verse(b_inp)
if b_inp > 5:
    print("Please go see a doctor.")
else:
    print("Another day of indulgence...")

cont()