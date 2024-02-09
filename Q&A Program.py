print("Welcome to the game I made...")

print("Follow me @ Darth_Necro ")



playing = input("Would you like to start? ")
print(playing)

if playing.lower() != "yes":
    quit()

print("There is a max of 3 points ")
print("Let's begin.....")
score = 0

answer = input("What planet are you from? ")

if answer.lower() == "earth":
    print("Hello Fellow human ")
    score += 1
else:
    print("It's all good friend,", "Aliens are cool ASF.......")

answer = input("Who was Smitty WerbenJagerManJensen? ")


if answer.lower() == "number 1":
    print("Yes Mr. Krabs said he was indeed was #1 ")
    score += 1
else:
    print("Yo momma dont love you, and Yo daddy left.......")

answer = input("Do you watch Dragon Ball Z? ")

if answer.lower() == "yes":
    print( "You my friend are a LEGEND! ")
    score += 1
else:
    print("GET TF OUT OF HERE BYE! ")


print("Your score is: " + str(score))

