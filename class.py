class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b
calculator=calculator()
add=calculator.add(3,4)
print(add)    
sub=calculator.sub(9,5)
print(sub)
mul=calculator.mul(6,6)
print(mul)
div=calculator.divide(4,2)
print(div)