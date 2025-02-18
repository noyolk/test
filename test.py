import time

print("this is a github test file.")
time.sleep(3)
print("Why are they watching this?")
time.sleep(3)
print("I don't know.")
time.sleep(3)
print("...")
time.sleep(5)
print("ok")
time.sleep(2)
while True:
    a = input("If you're bored, would you like to introduce yourself? (y/n): ")
    if a == "y":
        print("Hello, I am noyolk")
        time.sleep(2)
        print("I live in Korea and I am 11 years old.")
        time.sleep(3)
        print("You're thinking about it now, right? Why are you watching this")
        time.sleep(3)
        print("I don't know.")
        time.sleep(3)
        print("I don't have any more words to write..")
        time.sleep(3)
        print("I don't have anything to do either. Bye")
        break
    elif a == "n":
        print("...")
        time.sleep(3)
        print("ok")
        time.sleep(2)
        print("good bye..")
        break
    else:
        print("...")
        time.sleep(3)
        print("Please enter y or n")
        time.sleep(2)
        continue
time.sleep(6)
print("Why do you keep watching this? Hurry up and go")
time.sleep(3)
print("I'm really going. Good bye~")