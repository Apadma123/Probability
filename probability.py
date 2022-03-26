from Flip import Flips
def Probability():
    Data=Flips.Number_of_flips()
    print("Pabability of getting head:",(Data[0]/Data[2]))
    print("Pabability of getting tail:",(Data[1]/Data[2]))
    Data_1=Data[0]-Data[1]
    Data_2=Data[0]+Data[1]
    Compare=Data_1/Data_2
    print("Comparision of probabilities:",Compare)
    
if __name__=="__main__":
    Probability()
    
    
    
