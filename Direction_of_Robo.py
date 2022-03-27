from robot import Robot
def direction():
    Direction=Robot()
    for i in range(100):
        movement=input("provide the direction robot")
        present_position=Direction.movements(movement)
        if(present_position[0]==-1 or present_position[1]==-1 or
           present_position[0]==100 or present_position[1]==100):
            print("Your movement is out of grid")
        elif(present_position[0]==99 and present_position[1]==99):
            print("You won the treasure")
            break
        
        
if __name__=='__main__':
    direction()
    
    
    
