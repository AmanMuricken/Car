class car:
    attr1="benz"
    attr2="black"
    attr3="s-class"


    def fun(self):
      print("the company of my car is",self.attr1)
      print("color of my car is",self.attr2)
      print("the model of my car is",self.attr3)

c=car()
print(c)
c.fun()