# ============================================
# Section 1: Class & Object Fundamentals
# ============================================

class Person:
    # The __init__ method is called automatically when an object is created.
    # It is the constructor method in Python.
    def __init__(self, name, age):
        # The 'self' keyword refers to the current object being created or used.
        self.name = name  # instance variable for the person's name
        self.age = age    # instance variable for the person's age

    # Instance method (default type of method)
    # It can access instance variables through 'self'.
    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

    # Another instance method to show how multiple methods can be defined
    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age}.")

# ===============================
# Creating objects (instances)
# ===============================

# We create instances of the class by calling it like a function.
person1 = Person("Alice", 22)
person2 = Person("Bob", 30)

# ===============================
# Accessing attributes and methods
# ===============================

# You can access instance variables directly
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 30

# You can also call methods using dot notation
person1.greet()         # Hi, I'm Alice and I'm 22 years old.
person2.have_birthday() # Happy Birthday Bob! You are now 31.

# Each object maintains its own data — changing one doesn’t affect the other
print(person1.age)  # Still 22

# ============================================
# Section 2: Variables and Method Types
# ============================================

class Dog:
    # This is a **class variable** — it's shared by all instances of the class.
    species = "Canis Familiaris"

    def __init__(self, name, age):
        # These are **instance variables** — unique to each instance.
        self.name = name
        self.age = age

    # =====================
    # Instance Method
    # =====================
    def bark(self):
        # Instance methods take 'self' as the first argument.
        # They can access both instance and class variables.
        print(f"{self.name} says: Woof! I am a {self.species} and {self.age} years old.")

    # =====================
    # Class Method
    # =====================
    @classmethod
    def set_species(cls, new_species):
        # Class methods take 'cls' (the class itself) as the first argument.
        # They are used to modify or access class-level data.
        cls.species = new_species
        print(f"Species has been updated to: {cls.species}")

    # =====================
    # Static Method
    # =====================
    @staticmethod
    def info():
        # Static methods take NO 'self' or 'cls'.
        # They are like regular functions that are logically grouped with the class.
        print("Dogs are loyal and friendly animals.")

# ===============================
# Instance vs Class Variables
# ===============================

dog1 = Dog("Buddy", 3)
dog2 = Dog("Rex", 5)

dog1.bark() # Buddy says: Woof! I am a Canis Familiaris and 3 years old.
dog2.bark() # Rex says: Woof! I am a Canis Familiaris and 5 years old.

# Update the class variable using the class itself
Dog.set_species("Canis Lupus")

# Now all dogs will reflect the new species
dog1.bark()  # Buddy says: Woof! I am a Canis Lupus and 3 years old.
dog2.bark()  # Rex says: Woof! I am a Canis Lupus and 5 years old.

# ===============================
# Static Method Call
# ===============================
Dog.info()    # Called from class
dog1.info()   # Also callable from instance (but not recommended)

# ===============================
# Overriding a class variable at instance level (not recommended)
# ===============================
dog1.species = "Alien Dog"
print(dog1.species)  # Outputs "Alien Dog" (instance-level shadowing)
print(dog2.species)  # Still "Canis Lupus"
print(Dog.species)   # Still "Canis Lupus"

# ===============================
# Dynamically Adding Instance Variables After Object Creation
# ===============================
dog1.color = "Brown"  # We can add a new attribute at any time to an individual object
print(dog1.color)     # Output: Brown

# dog2 does NOT have this attribute
# print(dog2.color)   # Would raise AttributeError

# ============================================
# Section 3: Encapsulation and Attribute Control
# ============================================

# In Python, everything is technically public — there's no enforced access control like in Java.
# Variables with a single underscore (_x) are meant to be "protected", and double underscore (__x) triggers name mangling to avoid accidental conflicts.
# But for practical purposes, especially in quant work, you can treat all attributes as accessible.
# Just be consistent and clean in how you name and organize attributes.
# Use 'self.x' for regular attributes, and '_x' if you want to hint to yourself or teammates that it's internal logic.
# Skip strict encapsulation unless you're designing reusable components — focus on clarity, simplicity, and getting things done.

# ============================================
# Section 4: Inheritance and Method Overriding
# ============================================

# A base class (also called a parent or superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")
        # Output: Generic sound if not overridden

    def __str__(self):
        return f"Animal named {self.name}"

# A child class that inherits from Animal
class Dog(Animal):
    # Override parent's constructor
    def __init__(self, name, breed):
        # Call the parent class constructor using super()
        super().__init__(name)
        self.breed = breed

    # Override the speak method
    def speak(self):
        print(f"{self.name} barks: Woof!")
        # Output: Customized dog barking

    # Override __str__ for string output
    def __str__(self):
        return f"{self.name} the {self.breed}"

# Another child class
class Cat(Animal):
    # Note that it doesn't have a constructor, so it will use parent's constructor by default
    def speak(self):
        print(f"{self.name} meows: Meow~")
        # Output: Cat-specific sound

# ===============================
# Create instances and demonstrate inheritance
# ===============================
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

dog.speak()   # Output: Buddy barks: Woof!
cat.speak()   # Output: Whiskers meows: Meow~

# __str__ method gives readable output when printing the object; it is a special type of inherent function in python
print(dog)    # Output: Buddy the Golden Retriever
print(cat)    # Output: Animal named Whiskers
