import math
from dataclasses import dataclass,field

@dataclass
class calc:
    r: float

    def area(self):
        return round(math.pi*math.pow(self.r,2),2)
    
    def circum(self):
        return round(2*math.pi*self.r,2)
    
c1=calc(3.0)
print(c1.area())
print(c1.circum())