import random
import string

#############
# https://github.com/BlueStrawBerrys
############


print("1. @hotmail.com")
print("2. @att.net")
print("3. @yahoo.com")
print("4. @gmail.com")
print("5. custom domain")

a = input("Select: ")

if a == "1":
    print("make sure u cleared output.txt")
    z = open("output.txt", "w")
    while True:
        code = "" + ('').join(
                random.choices(string.ascii_letters + string.digits, k=4))
        z.write(code + "@hotmail.com\n")
        print(code + "@hotmail.com")

if a == "2":
    print("make sure u cleared output.txt")
    z = open("output.txt", "w")
    while True:
        code = "" + ('').join(
                random.choices(string.ascii_letters + string.digits, k=4))
        z.write(code + "@att.net\n")
        print(code + "@att.com")

if a == "3":
    print("make sure u cleared output.txt")
    z = open("output.txt", "w")
    while True:
        code = "" + ('').join(
                random.choices(string.ascii_letters + string.digits, k=4))
        z.write(code + "@yahoo.com\n")
        print(code + "@yahoo.com")

if a == "4":
    print("make sure u cleared output.txt")
    z = open("output.txt", "w")
    while True:
        code = "" + ('').join(
                random.choices(string.ascii_letters + string.digits, k=4))
        z.write(code + "@gmail.com\n")
        print(code + "@gmail.com")

if a == "5":
    print("make sure u cleared output.txt")
    aaf = input("enter domain with @: ")
    z = open("output.txt", "w")
    while True:
        code = "" + ('').join(
                random.choices(string.ascii_letters + string.digits, k=4))
        z.write(code + aaf + "\n")
        print(code + aaf + "\n")