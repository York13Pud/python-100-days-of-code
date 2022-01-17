# Class inheritance allows methods / attributes to be inherited by another class.
# To do this, you pass in the name of the class into the class that will inherit it
# and then use the super() class. 

# --- The animal class is the super class for this example:
class Animal():
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale.")
        
    def eyes(self):
        print(f"I have {self.num_eyes} eyes.")

# --- To use anything in the Animal class in the fish class, we first need to pass Animal as an argument:        
class Fish(Animal):
    def __init__(self):
    # Now we need to call the super() class to allow the Animal class to be used during the initialisation
    # of the Fish class:
        super().__init__()
    
    def swim(self):
        print("I can swim.")
    
    # Let's say we want to modify the breathe method to add an additional print to it.
    # First, define a new method (doesn't have to be the same name):
    def breathe(self):
        # Using the super class, call the breathe method:
        super().breathe()
        # print out some additional text. The result will be the text from the Animal breathe class / method
        # and the below on two different lines.
        print("doing this in water.")
        
# --- Let's create a new object and call some of the methods from each of the above classes:
nemo = Fish()
nemo.swim()
# The below are called from the inherited class (Animal)
nemo.breathe()
nemo.eyes()
# Or, you can use the attribute (num_eyes) directly from the inherited class:
print(nemo.num_eyes)