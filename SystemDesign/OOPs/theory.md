# OOPs Doc

## Encapsulation
Encapsulation wraps data and methods into a single unit and restricts direct access to prevent unauthorized modification. Python enforces this convention using prefixes:

* **Protected (single underscore `_`):** Suggests a variable shouldn't be accessed outside the class hierarchy.
* **Private (double underscore `__`):** Triggers name mangling, making it harder to access directly from outside.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    # Getter method to safely access private data
    def get_balance(self):
        return self.__balance

    # Setter method to safely modify private data
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)    # Throws AttributeError
```

## Inheritance
Inheritance allows a new class (child) to adopt the attributes and methods of an existing class (parent), minimizing code repetition. You can use the `super()` function to call the parent class's constructor or methods.

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy")
print(my_dog.eat())   # Inherited method: Buddy is eating.
print(my_dog.bark())  # Child method: Buddy says Woof!
```

## Polymorphism
Polymorphism literally means "many forms". It allows different classes to share the exact same method name but implement different behaviors. This is often achieved via method overriding in inheritance.

```python
class Cat:
    def make_sound(self):
        return "Meow"

class Dog:
    def make_sound(self):
        return "Bark"

# A unified interface handling different object types
def animal_sound(animal_object):
    print(animal_object.make_sound())

cat = Cat()
dog = Dog()

animal_sound(cat)  # Output: Meow
animal_sound(dog)  # Output: Bark
```

## Abstraction
Abstraction hides complicated internal structures and only displays the necessary features to the user. Python implements abstraction using the `abc` (Abstract Base Classes) module. You cannot create an instance of an abstract class directly; it forces child classes to implement specific methods.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract Base Class
    @abstractmethod
    def start_engine(self):
        pass

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started. Vroom!"

# my_vehicle = Vehicle() # Throws TypeError: Can't instantiate abstract class
bike = Motorcycle()
print(bike.start_engine())
```


##
## Python Property Decorators Quick Reference

The `@property` ecosystem allows methods to behave like standard attributes. This enables clean syntax while maintaining strict control over data validation, formatting, and access.

### Core Components

#### 1. `@property` (The Getter)
* **Purpose:** Defines an attribute's read behavior or generates a value dynamically.
* **Syntax:** `obj.attribute` (executed without parentheses `()`).
* **Requirement:** Must accept only `self` and must explicitly `return` a value.
* **Ordering:** Must always be defined **first** in the class block.

#### 2. `@<attribute>.setter` (The Setter)
* **Purpose:** Defines an attribute's write behavior and runs validation code during assignments.
* **Syntax:** `obj.attribute = new_value`
* **Requirement:** Must accept `self` and exactly one value argument (`new_value`).
* **Ordering:** Must be defined **after** its corresponding `@property`.

#### 3. `@<attribute>.deleter` (The Deleter)
* **Purpose:** Cleans up underlying data or handles dependencies when an attribute is removed.
* **Syntax:** `del obj.attribute`
* **Requirement:** Must accept only `self`.

### Implementation Template

```python
class ManagedAttribute:
    def __init__(self, value):
        # Store data in a protected variable using a leading underscore
        self._var = value  

    @property
    def var(self):
        """Getter: Triggers on reading."""
        return self._var

    @var.setter
    def var(self, new_value):
        """Setter: Triggers on assignment (=)."""
        if new_value < 0:
            raise ValueError("Values cannot be negative")
        self._var = new_value

    @var.deleter
    def var(self):
        """Deleter: Triggers on deletion (del)."""
        del self._var
```

### 3 Golden Rules for Usage

1. **Name Matching:** The method name under `@property`, `@var.setter`, and `@var.deleter` must be **identical** (e.g., `def var(self):`).
2. **Avoid Loops:** Internal methods must access the protected backing variable (`self._var`) instead of the property interface (`self.var`). Accessing `self.var` inside the getter or setter triggers an infinite recursion crash.
3. **Implicit Execution:** Users interacting with your class do not need to know these decorators exist. They use standard dot notation assignments seamlessly.
