from inheritfile import Parents
class Child(Parents):
    def __init__(self, height, hairtype, features,eyecolor):
        self.eyecolor = eyecolor
        super().__init__(height, hairtype, features) #supper me self nahi aata 
                                                      # only super(). function can bring or access to parents attributes("height","hairtype") but we can access functions directly

    def genes(self):
        g = input("your genes in XX or XY terms = ")
        print(f"child has {g} genes")   

q = Parents(5.5,"black silky","sharp")
q.habbits()
f = Child(5.4,"Curly n fizzy","sharp","honey brown")  
print(f.hairtype)
print(f.eyecolor)
print(f.height , f.features)
f.genes()   
f.habbits()