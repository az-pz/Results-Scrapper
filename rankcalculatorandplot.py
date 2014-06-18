import matplotlib.pyplot as plt
import json
import numpy as np
plt.axis([1,100,0,10])
i=1
roll=110112001
rank=1
f=open('file','r')
val=json.load(f)
rnkchk=raw_input("enter rollnumber to check rank :: ")
while(roll<110112100):
    try :
        plt.plot(i,val[str(roll)],'b^')
        i=i+1
        if(float(val[str(roll)]) > float(val[rnkchk])):
            rank=rank+1
        roll=roll+1
    except:
        roll=roll+1
        pass
print rank," is your rank da."
plt.xlabel('ROLLNUMBER')
plt.ylabel('GPA')
plt.title('GPA  vs  ROLLNUMBER')
plt.grid(True)
plt.show()
f.close()
