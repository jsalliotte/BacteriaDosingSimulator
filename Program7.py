## Jason Salliotte                         ##                           
##                                         ##
## Bacteria Simulator                      ##
##                                         ##
##                                         ##
##                                         ##
#############################################
from random import randint

# Bacteria class gets passed resistance, and has set parameters for health lifespan and birth counter
class bacteria:
    def __init__(self,resistance):
        self.resistance = resistance + randint(-1, 1)
        if self.resistance < 1:
            self.resistance = 1
        if self.resistance > 10:
            self.resistance = 10
        self.health = 10
        self.life_span = 15
        self.birth_counter = 3
    def __str__(self):
        """str method prints values of all parameters"""
        str_ret = "H" + "(" + str(self.health) + ")     " + "R" + "(" + str(self.resistance) + ")     "+"LS" + "(" + str(self.life_span) + ")     "+"BC" + "(" + str(self.birth_counter) + ")"
        return str_ret
    def is_alive(self):
        """returns true if health and lifespan above 0, otherwise false"""
        if self.health > 0 and self.life_span > 0:
            return True
        else:
            return False
    def tick(self):
        """decrements birth counter and lifespan of bacteria"""
        self.birth_counter -= 1
        self.life_span -= 1
    def dose(self,dose):
        """ reduces health dependant on dose and resistance"""
        damage = dose/self.resistance
        self.health -= damage
    def reproduce(self):
        """returns new bacteria if birth counter is 0"""
        if self.birth_counter <= 0 and self.is_alive() == True:
            return bacteria(self.resistance)


class host:
    def __init__(self,num_bacteria):
        self.num_bacteria = num_bacteria
        self.bacterias = list()
        cnt = 0
        while cnt < num_bacteria:
            new_bacteria = bacteria(3)
            self.bacterias.append(new_bacteria)
            cnt += 1
    def __str__(self):
        """prints total number of bacteria, and averages of health and resistance of all bacteria"""
        avg_health = 0
        cnt = 0
        avg = 0
        non_none_total = [bact for bact in self.bacterias if bact is not None] 
        if len(self.bacterias) > 0:
            for num in range (0,len(self.bacterias)):
                if self.bacterias[cnt] is not None:
                    avg += self.bacterias[cnt].health
                cnt += 1
             
            avg_health = avg/(len(non_none_total))
        else:
            avg_health = 0
        cnt = 0
        res = 0
        if len(self.bacterias) > 0:
            for num in range (0,len(self.bacterias)):
                if self.bacterias[cnt] is not None:
                    res += self.bacterias[cnt].resistance
                cnt += 1
            avg_res = res/(len(non_none_total))
        else:
            avg_res = 0
        str_ret =  "Count : " + str(len(self.bacterias))+"\n"+"Average Health : " + str(avg_health) +"\n"+"Average Resistance : " + str(avg_res)
        return str_ret
    
    def tick(self,_dose):
        """doses bacteria if _dose parameter is true, bacteria reproduces if counter is at 0, if dead they are removed from the list, calls tick method for all bacteria"""
        cnt = 0
        iteration = len(self.bacterias)
        
        if len(self.bacterias) >= cnt and len(self.bacterias) >= 0:
            for num in range (0,iteration):
               if len(self.bacterias) > 0:
                   self.bacterias = [bact for bact in self.bacterias if bact is not None] 
                   if None in self.bacterias:
                       print("meow")
                   if cnt == len(self.bacterias) or cnt > len(self.bacterias):
                       if len(self.bacterias) == 0:
                           break
                       else:
                           cnt = len(self.bacterias)-1
                   self.bacterias[cnt].tick()
                   if _dose == True:
                       self.bacterias[cnt].dose(25)
                   if self.bacterias[cnt].is_alive() == False:
                       self.bacterias.pop(cnt)
                   if cnt == len(self.bacterias) or cnt > len(self.bacterias):
                       if len(self.bacterias) == 0:
                           break
                       else:
                           cnt = len(self.bacterias)-1
                   if self.bacterias[cnt].birth_counter <= 0:
                       self.bacterias.append(self.bacterias[cnt].reproduce())
                       self.bacterias[cnt].birth_counter = 3
                   
                   cnt += 1
        
                
        
        

# three host objects required
host_one = host(1)
host_two = host(1)
host_three = host(1)


# calls tick 30 times for each object
print("Loading...")
for cnt in range (0,30):
    host_one.tick(False)
    host_two.tick(False)
    host_three.tick(False)

# calls tick 15 times for each object, first object with no dose, second object full dose, third object half dose
for cnt in range(0,15):
    host_one.tick(False)
    host_two.tick(True)
    if cnt % 2 != 0:
        host_three.tick(True)
    else:
        host_three.tick(False)
#prints all three objects
print("No Dosage")    
print(host_one)
print("")
print("Full Dosage")
print(host_two)
print("")
print("Half Dosage")
print(host_three)
input("")
