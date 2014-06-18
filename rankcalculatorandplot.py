import matplotlib.pyplot as plt    //matplotlob for plotting the graph
import json             // i've used json for encoding the data into the file
import numpy as np      //  you dont need numpy for this. i was testing its usage when i wrote this code :P
plt.axis([1,100,0,10])      // x axis for rollnos from 1-100 and y axis for gpa from 0-10
i=1             //flag used for counting the rollnos from 1
roll=110112001      //starting roll number in the class
rank=1                  // set rank as 1 first and then increment 
f=open('file','r')      // open a file called file in the directory
val=json.load(f)        // load json to read from file
rnkchk=raw_input("enter rollnumber to check rank :: ")      //flag for holding the rollnos whose rank is to be checked
while(roll<110112100):
    try :                           // some rollnos are missing, to handle exceptions i've used try and except. 
        plt.plot(i,val[str(roll)],'b^')     //plots the data. phew. finally !
        i=i+1       // bleh
        if(float(val[str(roll)]) > float(val[rnkchk])): // this is for the rank thing. self explanatory
            rank=rank+1         //increments rank
        roll=roll+1
    except:
        roll=roll+1         // what to do when exception is raised ? just skip that roll number cuz the person doesnt exist
        pass
print rank," is your rank da."      // yeehaw
plt.xlabel('ROLLNUMBER')        // labelling x axis
plt.ylabel('GPA')       //labelling y axis
plt.title('GPA  vs  ROLLNUMBER')    //add a title
plt.grid(True)  //chumma display grid for fun . 
plt.show()  // finally opens the window that displays the graph
f.close()       // close the file that we've opened to extract data. very important or your os will have no read permission is you want to open the file. 
