from abc import ABC, abstractmethod

# 1 & 4. ABSTRACTION & INHERITANCE: 
# Animal inherits from ABC (Abstract Base Class). 
# This means you cannot create a generic "Animal" directly; you MUST create a specific animal.
class Animal(ABC):
    def __init__(self, diet: str, kingdom: str, animal_type: str, name: str):
        # 2. ENCAPSULATION: We use an underscore to hide these internal variables.
        self._diet = diet
        self._kingdom = kingdom
        self._type = animal_type
        self._name = name
        
    # ENCAPSULATION: We expose the hidden _name variable safely using a property.
    @property
    def name(self) -> str:
        return self._name

    def eat(self) -> None:
        # Standard method available to all child classes
        print(f"{self.name} the {self._type} is eating its {self._diet} diet.")

    # 4. ABSTRACTION: @abstractmethod forces every child class to create its own make_sound method.
    @abstractmethod
    def make_sound(self) -> None:
        pass

    # A "dunder" method that controls what prints when you print the object itself
    def __str__(self) -> str:
        return f"[{self._kingdom}] {self._type} named {self.name}"


# 1. INHERITANCE: Dog inherits from Animal
class Dog(Animal):
    def __init__(self, name: str = "Duggu"):
        # Passing specific Dog traits up to the Animal blueprint
        super().__init__(diet="Omnivore", kingdom="Mammal", animal_type="Dog", name=name)
    
    # 3. POLYMORPHISM: Dog's specific implementation of the abstract method
    def make_sound(self) -> None:
        print(f"{self.name} says: Woof! Woof!")


# 1. INHERITANCE: Cat inherits from Animal
class Cat(Animal):
    def __init__(self, name: str = "Kuttu"):
        # Note: Cats are actually Obligate Carnivores, so let's update their diet!
        super().__init__(diet="Carnivore", kingdom="Mammal", animal_type="Cat", name=name)
        self._habit = "Sleeping in boxes" 
        
    # 3. POLYMORPHISM: Cat's specific implementation of the abstract method
    def make_sound(self) -> None:
        print(f"{self.name} says: Meow!")
        
    # ENCAPSULATION: Getter and Setter for habit
    @property
    def habit(self) -> str:
        return self._habit
        
    @habit.setter
    def habit(self, new_habit: str) -> None:
        self._habit = new_habit


print("--- Creating Objects ---")
dog = Dog()
cat = Cat("Luna") # Overriding the default name

print("\n--- Encapsulation & Inheritance ---")
# This automatically calls the __str__ method we defined in Animal
print(dog) # [Mammal] Dog named Duggu
print(cat) # [Mammal] Cat named Luna

print("\n--- Abstraction & Polymorphism ---")
# We can put both in a list and treat them simply as "Animals"
animals = [dog, cat]

for animal in animals:
    animal.eat()          # Both inherited this exact method
    animal.make_sound()   # Python knows to use the Dog sound for the dog, and Cat sound for the cat!

print("\n--- Using the Setter ---")
print(f"{cat.name}'s current habit: {cat.habit}") # Luna's current habit: Sleeping in boxes
cat.habit = "Knocking cups off the table"
print(f"{cat.name}'s new habit: {cat.habit}") # Luna's new habit: Knocking cups off the table
