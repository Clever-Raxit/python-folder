import pygame
#--------
print("--------")
print("[Note: if you wanna to play a guess game then first specify your name.]")
print("")
name=input("Name: ")
print("")
print("")

if name.upper() == "Raxit":
    print("Welcome to your Game Mr. Raxit")
elif name.lower() =="raxit":
    print("Welcome to your Game Mr. Raxit")

else:
    print("Hello "+name)
print("")
print("[Note:please enter your guess in lower case.pl..]")
print("")
print("[Hint: The secrete word is fruit.]")

secrete_word="orange"
guess=""
guess_count=0
guess_limit=3
out_of_guessess=False

while guess != secrete_word and not(out_of_guessess):
    if guess_count < guess_limit:
        print("")
        guess=input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guessess=True
print("")

if out_of_guessess:
    print("Out of guessess, YOU LOSE!")
else:
    print("YOU WIN! That's a win you are now choosed to next level.")