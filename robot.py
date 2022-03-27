class Robot:
    def __init__(self):
        self.i=0
        self.j=0
    def movements(self,Direction):
        if(Direction =='R'):
            self.j=self.j+1
        elif(Direction == 'D'):
            self.i=self.i+1
        elif(Direction == 'L'):
            self.j=self.j-1
        elif(Direction == 'T'):
            self.ji=self.i-1
        return ((self.i,self.j))
    
