'''# Write a program that loads an integer from the keyboard and prints whether it is divisible by 3, 5, 7 and 11. 
# If program finds e.g. that it's divisible by 3, it should skip other checks. 
# It should work the same for all the cases.

a = int(input("Unesi a: "))

if a % 3 == 0:
    print("Broj je dijeljiv sa 3")
elif a % 5 == 0:
    print("Broj je dijeljiv sa 5")
elif a % 7 == 0:
    print("Broj je dijeljiv sa 7")

# Change the last program (01-exercises.py) in the way that it always checks all the conditions. 
# Meaning, if program finds e.g. that it's divisible by 3, it should check also if it's divisible by other numbers.

a = int(input("Unesi a: "))

if a % 3 == 0:
    print("Broj je dijeljiv sa 3")
if a % 5 == 0:
    print("Broj je dijeljiv sa 5")
if a % 7 == 0:
    print("Broj je dijeljiv sa 7")
# Write a program that loads three integers from the keyboard and prints the largest of them.

a = int(input("Unesi a: "))
b = int(input("Unesi b: "))
c = int(input("Unesi c: "))

# a = 2
# b = 10
# c = 4

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

# Write a program that loads a number from the keyboard and prints whether it is even or odd.

a = int(input("Unesi a: "))

if a % 2 != 0:
    print("Broj je neparan")
else:
    print("Broj je paran")'''

    ##DUG

# Write a program that loads two numbers (enumerated as 1 and 2) from the keyboard and if first one is greater prints 
# "Number 1 is greater", and vice versa. If they are the same print "Numbers are the same".
number_1 = int(input("Unesi 1 broj: "))
number_2 = int(input("Unesi 2 broj: "))
if number_1 > number_2:
    print('Broj jedan je veći od broja dva')
elif number_1 == number_2:
    print("Brojevi su isti")
else:
    print("Broj dva je veči od broja jedan")
# Write a program that asks for a command. If command is...

# "run", print output "Running...",
# "stop" print output "Done."
# "pause", "repeat" or "skip" print which command is executed (e.g. "Executing command: pause").
#  Use or operator here.
#  something else, print the command along with the information that is unknown (e.g. "Unknown command: qwe").

comand_1 = input("odabreri komandu (run, stop, pause, repeat, skip): ")

if comand_1 == 'run':
    print('Running')
elif comand_1 == 'stop':
    print("Done")
elif comand_1 == 'pause' or comand_1 =='repeat' or comand_1 =='skip':
    print("Done")
else:
    print("Krivi unos")



# Write a program that loads an integer from the keyboard and prints whether it is divisible by 3 or 7. 
# Otherwise it prints the message "The loaded number is divisible neither by 3 nor by 7".

a = int(input("Unesi a: "))

if a % 3 == 0:
    print("Broj je dijeljiv sa 3")
elif a % 7 == 0:
    print("Broj je dijeljiv sa 7")
else:
    print("Broj nije djeljiv ni s 3 ni s 7")