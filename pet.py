class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0  # Starts full
        self.energy = 10  # Starts fully rested
        self.happiness = 5  # Default happiness level
        self.tricks = []  # List to store learned tricks

    def eat(self):
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 3)
            self.happiness += 1
            print(f"{self.name} has eaten. Hunger level is now {self.hunger}. Happiness increased to {self.happiness}.")
        else:
            print(f"{self.name} is already full!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} has slept. Energy level is now {self.energy}.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness += 2
            self.hunger += 1
            print(f"{self.name} played! Energy level is now {self.energy}, happiness increased to {self.happiness}, and hunger level is now {self.hunger}.")
        else:
            print(f"{self.name} is too tired to play!")

    def get_status(self):
        print(f"Status of {self.name}:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

# Example usage:
my_pet = Pet("Buddy")
my_pet.get_status()
my_pet.eat()
my_pet.play()
my_pet.sleep()
my_pet.train("roll over")
my_pet.show_tricks()
my_pet.get_status()