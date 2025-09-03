# Python-OOP-Challenge
Pet Class
This is a simple Python class named Pet that simulates the basic life of a pet. You can create a pet, feed it, put it to sleep, and play with it to manage its hunger, energy, and happiness levels.

Features
__init__(self, name): Creates a new pet with a given name. The pet starts with a full belly, high energy, and a default level of happiness. It also has a list to store tricks it can learn.

eat(): Decreases the pet's hunger and increases its happiness. It won't overfeed the pet if it's already full.

sleep(): Increases the pet's energy, helping it recharge.

play(): Decreases the pet's energy and increases its happiness and hunger. If the pet is too tired, it won't be able to play.

get_status(): Prints a summary of the pet's current hunger, energy, and happiness levels.

train(trick): Adds a new trick to the pet's list of tricks.

show_tricks(): Displays all the tricks the pet has learned.

How to Use
First, make sure you have the Pet class code saved in a file (e.g., pet_class.py).

You can then create an instance of the Pet class and interact with it. Here is an example:

# Create a new pet named "Buddy"
my_pet = Pet("Buddy")

# Check Buddy's initial status
my_pet.get_status()

# Feed and play with Buddy
my_pet.eat()
my_pet.play()

# Let Buddy sleep
my_pet.sleep()

# Teach Buddy a new trick
my_pet.train("roll over")
my_pet.show_tricks()

# Check the final status
my_pet.get_status()
