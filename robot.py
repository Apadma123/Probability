class Robot:
    def __init__(self):
        self.position=[0,0]
    def movements(self,Direction):
        if(Direction =='R'):
            self.position[1]=self.position[1]+1
        elif(Direction == 'D'):
            self.position[0]=self.position[0]+1
        elif(Direction == 'L'):
            self.position[1]=self.position[1]-1
        elif(Direction == 'T'):
            self.position[0]=self.position[0]-1
        return ((self.position[0],self.position[1]))
    

