guests = ['Gingy', 'Faus', 'Emmy', 'Feral', 'Dunc']
print(guests)

#Gingy, Faus, Emmy, Feral, and Dunc will be invited
dinner_invitation1 = (f"Greetings, {guests[0]} meow meow")
dinner_invitation2 = (f"Greetings, {guests[1]} I would like to invite you to a dinner party I am hosting!")
dinner_invitation3 = (f"Greetings, {guests[2]} I would like to invite you to a dinner party I am hosting!")
dinner_invitation4 = (f"Greetings, {guests[3]} I would like to invite you to a dinner party I am hosting!")
dinner_invitation5 = (f"\nSadly, {guests[4]} will be busy and can't attend the dinner party")

print(dinner_invitation1)
print(dinner_invitation2)
print(dinner_invitation3)
print(dinner_invitation4)
print(dinner_invitation5)

#Dunc can't make it
del guests[4]
guests.insert(4,'Zianne')

#Zianne will replace Dunc (Gingy, Faus, Emmy, Feral, and Zianne will be invited)
dinner_invitation1 = (f"\nGreetings, {guests[0]} meow meow")
dinner_invitation2 = (f"Greetings, {guests[1]} I would like to invite you to a dinner party I am hosting!")
dinner_invitation3 = (f"Greetings, {guests[2]} I would like to invite you to a dinner party I am hosting!")
dinner_invitation4 = (f"Greetings, {guests[3]} I would like to invite you to a dinner party I am hosting!")
dinner_invitation5 = (f"Greetings, {guests[4]} I would like to invite you to a dinner party I am hosting!")
print(dinner_invitation1)
print(dinner_invitation2)
print(dinner_invitation3)
print(dinner_invitation4)
print(dinner_invitation5)

#New dinner table won’t arrive in time for the dinner
print(f"\nI humbly apologize, {guests[0]} meow meow meow")
guests.pop()
print(f"I humbly apologize, {guests[1]} there is no room in the dinner table please accept my apology")
guests.pop()
print(f"I humbly apologize, {guests[2]} there is no room in the dinner table please accept my apology")
guests.pop()

#Feral and Zianne is still invited
guests = ['Feral', 'Zianne']
print(f"\nHello! {guests[0]} you are still invited to the dinner party!")
print(f"Hello! {guests[1]} you are still invited to the dinner party!")

#Remove the last two names from your list
del(guests[0])
del(guests[0])

#Print your list to make sure you actually have an empty list at the end of your program.
print(guests)

