from ramdom_values_generator import Generate
class Flips:
    def Number_of_flips():
        trails=int(input("number of flips of a coin"))
        tail=0
        head=0
        for i in range(trails):
            random=Generate.Random_Values(2)
            if random==1:
                head=head+1
            else:
                tail=tail+1
        sample_space=2**(trails)
        l=[]
        l.append(head)
        l.append(tail)
        l.append(sample_space)
        return l
