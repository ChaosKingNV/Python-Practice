print("what's your age?")
age = int(input())

canDrink = age > 17

if canDrink:
    print("you can drink")
    if age >50:
        print("you get discount")
elif not canDrink:
    print("no dirinks for you")

print("Thanks")
