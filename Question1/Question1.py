import random

class nqueens():

    def __init__(self,N):
        self.size = N
        self.state = ""
        self.statelist = []
        self.count = 0
    
    def __str__(self):
        return "N: {}\tState: {}\tCount: {}".format(self.size,self.state,self.count)       
    
    def set_state(self):
        print("To set state randomly press '1'\nTo set state manually press '2' ")
        a = int(input("Choice: "))
        if a == 1:
            self.generate_random_state()
            print("random created state: ",self.state)
        elif a == 2:
            print("Set state with",self.size,"digit numbers")
            while True:
                b = input("Number: ")
                if self._is_valid(b) == True:
                    self.state+=b
                    break
                else:
                    print("enter a valid number!")
                        
    def generate_random_state(self):
        i = 0
        while (i<self.size): 
            a = random.randint(1,self.size)
            self.state+=str(a)
            i+=1
        
    def _is_valid(self,state_str):
        if state_str.isdigit() == False:
            return False
        q = 0
        for i in state_str:
            q+= 1
            if int(i)>self.size:
                return False                
            if int(i) == 0:
                return False        
        if q != self.size:
            return False
        return True
    
    def count_attacking_pairs(self):
        count = 0
        for i in range(0,len(self.state)):
            for j in range(0,len(self.state)):
                if i > j:
                    continue
                else:
                    if i == j:
                        continue
                    else:
                        if self.state[i] == self.state[j]:
                            count+=1
                        if int(self.state[i])-(i-j) == int(self.state[j]) or int(self.state[i])+(i-j) == int(self.state[j]):
                            count+=1
        self.count = count
        return count

