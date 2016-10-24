#import:

import random

import math

import time

#establishing vars:

p_health = 100

d_health = 200

s_health = 100

battle = 1

#program start:

player_name = input("What is your name hero? ")

print(player_name + " travels into the lair of the dragon seeking riches and fame.")

time.sleep(1.5)

print("You find the dragon sleeping and wake it with a fierce battle cry.")

time.sleep(1)

controls = input("Would you like to see the controls? y/n ")

if controls == "y":

    print("Controls:")   

    time.sleep(1)

    print("-attack- to deal damage to the dragon")

    time.sleep(1)

    print("-block- to block attacks")

    time.sleep(1)
    
    print("but be careful, your shield has health")

    time.sleep(1)

    print("-heal- to heal your self")

    time.sleep(1)

    print("Good luck.")

    time.sleep(1)

else:

    time.sleep(1)

    print("Good luck.")

    time.sleep(1)

while battle == 1:

    print("Health: " + str(p_health))
    time.sleep(0.5)
    print("Dragon: " + str(d_health))
    time.sleep(0.5)
    print("Shield: " + str(s_health))
    time.sleep(0.5)
    c = input("What would you like to do: ")
    time.sleep(0.5)
    if c == "attack":

        damage = random.gauss(15, 2)

        print("You attacked for " + str(damage) + " damage.")

        d_health = d_health - damage

        time.sleep(0.5)

        d = random.gauss(15, 2)

        p_health = p_health - d

        print("The dragon attacked for " + str(d) + " damage.")

    elif c == "block":

        if s_health > 0:

            d = random.gauss(15, 2)

            s_health = s_health - d

            print("The dragon attacked for " + str(d) + " damage, but it was blocked.")

        else:

            print("Your shield is broken.")

            time.sleep(1)

    elif c == "heal":

        if p_health < 100:

            heal = random.gauss(15, 2)

            p_health = p_health + heal

            print("You healed for " + str(heal) + ".")

            d = random.gauss(10, 2)

            p_health = p_health - d

            time.sleep(1)

            print("The dragon attacked for " + str(d) + " damage.")

        else:

            print("You have full health and cannot heal.")

    else:

        print("Sorry, " + player_name + ", I did not understand that.")

    if p_health <= 0:

        battle = 0

    elif d_health <= 0:

        battle = 2

if battle == 0:

    print(player_name + " died, try again.")

elif battle == 2:

    print(player_name + " defeated the dragon, but died of TB two weeks later.")
