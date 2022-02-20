#W6 Task 1
#class definition for Dog
class Dog():
    #Public / Private attributes
    def __init__(self, dogName, myColour):
#In Python, names starting with a double underscore are private
#They are not visible outside the method
#This is data hiding, an important aspect of "encapsulation"
        self.__name = dogName
        self.__colour = myColour
        
    def bark(self, barkTimes):
        for n in range (barkTimes):
            print(self.__name + " says Woof!")
            
    def setColour(self,myColour):
        self.__colour = myColour
        
    def getColour(self):
        return self.__colour
        
    def getName(self):
        return self.__name
    
    def printDogDetails(self):
        print (self.__name, self.__colour)
    
class Puppy(Dog):
#Puppy inherits attributes and methods from parent class Dog

#In Python, names starting with a double underscore are private
#They are not visible outside the method
#This is data hiding, an important aspect of "encapsulation"
#This class has an extra private attribute __shoesChewed, initialised to 0
 
    def __init__(self, dogName, myColour):
        super().__init__(dogName, myColour) # Dog Constructor
        self.__shoesChewed=0
    #end procedure
        
    #public procedure chewShoe(myShoesChewed)    
    def chewShoe(self, myShoesChewed):      
        self.__shoesChewed = self.__shoesChewed + myShoesChewed
    #end procedure

    def getShoesChewed(self):
        return self.__shoesChewed
 
    def bark(self, barkTimes):
        super().bark(1)
        for n in range (barkTimes):
            print("Yap!")
    
        
myDog1 = Dog("Fido", "Black")
myDog2 = Dog ("Bonnie","Golden")
myDog3 = Dog ("Mutt", "Unknown")
myDog4 = Dog ("Jeff", "Unknown")
puppy1 = Puppy("Malla","light brown")
puppy2 = Puppy("J","Black")

myDog3.bark(3)
puppy1.bark(2)

##if myDog3.getColour() == "Unknown":
##    print("Please enter colour for", myDog3.getName())
##    newColour = input() 
##    myDog3.setColour (newColour)
##
##dog2Name = myDog2.getName()
##dog2Colour = myDog2.getColour()
##print (dog2Name, dog2Colour)
##
##print(myDog3.getName(), "is", myDog3.getColour())
##print(puppy1.getName(), "is", puppy1.getColour())
#myDog3.chewShoe(3)
puppy1.chewShoe(3)
puppy1.chewShoe(1)
print(puppy1.getName(), "has chewed", puppy1.getShoesChewed(), "shoes")

print("Polymorphism in action")

my_animal_list = [myDog1,myDog2,puppy1,myDog3,myDog4,puppy2]

for animal in my_animal_list:
    animal.bark(3)

                  
