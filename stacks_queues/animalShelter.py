class Animal:
   def __init__(self,species=0,name="petName",next=None):
       self.species=species   #0->cat 1->dog
       self.name=name
       self.next=next


class AnimalShelter:
   def __init__(self,animal=None):
       self.animal=animal
       self.top=None
       self.bottom=None


   def enqueue(self,animal):
       if self.bottom:
           self.bottom.next=animal
           self.bottom=animal
       else:
           self.top=self.bottom=animal
       self.bottom.next=None

   def dequeueAny(self):
       node=None
       if self.top:
           node=self.top
           self.top=self.top.next
           node.next=None
       if not self.top:
           self.bottom=None
       return node
 
   def peak(self):
       if self.top:
           return self.top.species
       else:
           return None

   def isEmpty(self):
       if not self.bottom:
           return True
       return False
   
   def dequeueAnimal(self,species):
       temp=AnimalShelter()
       node=None
       while not self.isEmpty():
           if not node and self.peak() == species:
               node=self.dequeueAny()
           temp.enqueue(self.dequeueAny())

       while not temp.isEmpty():
           self.enqueue(temp.dequeueAny())

       return node

   def dequeueCat(self):
       return self.dequeueAnimal(0)

   def dequeueDog(self):
       return self.dequeueAnimal(1)

   def __str__(self):
       mystr=""
       node=self.top
       while node:
           mystr += str(node.name) + " "
           node=node.next
       return mystr


if __name__ == "__main__":

   shelter=AnimalShelter()
   shelter.enqueue(Animal(1,"kopek1"))
   shelter.enqueue(Animal(1,"kopek2"))
   shelter.enqueue(Animal(0,"kedi1"))
   shelter.enqueue(Animal(1,"kopek3"))
   shelter.enqueue(Animal(0,"kedi2"))

   print(shelter)

   shelter.dequeueAny()
   
   print(shelter)
   
   shelter.dequeueCat()
   
   print(shelter)
   shelter.dequeueDog()
   print(shelter)

   
   shelter.enqueue(Animal(0,"kedi30"))
   shelter.enqueue(Animal(0,"kedi31"))
   shelter.enqueue(Animal(1,"kopek34"))

   print(shelter) 
   shelter.dequeueCat()
   print(shelter)
   shelter.dequeueDog()
   print(shelter)
