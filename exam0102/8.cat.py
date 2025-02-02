class animal:
    def speak(self):
        print("an animal")

class dog(animal):
    def speak(self):
        print("dog barks")


class cat(animal):
    
    def speak(self):
        super().speak()
        print("cat meows")
c=cat()
d=dog()
c.speak()
d.speak()
