class student :
    grade=10
    name="Samuel"
    
    def intro(self):
        print("Hello I am a student")

    def details(self):
        print("My name is" , self.name)
        print("I am in grade" , self.grade)

ob=student()
ob.intro()
ob.details()
