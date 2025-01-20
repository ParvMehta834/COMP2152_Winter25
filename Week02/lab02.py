import random

# Step 1: Define an array called weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Step 2: Roll the dice (1-6) and save the result in weaponRoll
try:
    # Use random.randint to roll the dice between 1 and 6
    weaponRoll = random.randint(1, 6)  
    print(f"You rolled a {weaponRoll}.")

    # Step 3: Use weaponRoll as an index into the weapons array
    heroWeapon = weapons[weaponRoll - 1]  
    print(f"Your hero's weapon is: {heroWeapon}")

    # Step 4: Define conditions based on weaponRoll
    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is okay, but nothing special.")
    else:
        print("Wow! You got an awesome weapon, buddy!")

    # Step 5: Additional condition
    if heroWeapon != "Fist":
        print("Lucky you! You avoided rolling the Fist this time.")

except IndexError as e:
    print("Index Error occurred:", e)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
