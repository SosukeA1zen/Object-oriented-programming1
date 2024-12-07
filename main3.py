class parrot :

    def __init__(self,name,age):
        self.name = name
        self.age =age

    def sing(self,song):
       return self.name ,"sings",song,"song"
    
    def dance(self):
        return self.name ,"is now dancing"
    
blue=parrot("blue",10)
print(blue.sing("happy"))
print(blue.dance())

