from splinter import Browser    //splinter is the module used for manipulating the browser
import json             //json for encoding the data into the file 
data=dict()         // dictionaries save rollnumber and gpa of the student
browser = Browser('firefox')        //firefox for life
browser.visit('http://www.nitt.edu/prm/ShowResult.htm')     //our results page 
roll=110112000  //starting roll number -1
f=open('gpasem4','w')       // opens the file that has to be written into
while(roll<110112100):  
    #browser.type('TextBox1',roll)
    roll=roll+1 
    with browser.get_iframe('main') as iframe:      // the page is being divided into frames . so select the appropriate frame  
        try :
            iframe.fill('TextBox1',roll)
            iframe.find_by_name('Button1').click()
            browser.find_by_xpath('//select[@id="Dt1"]/option[@value="96"]')._element.click()
            
            name=iframe.find_by_id('LblName')
            gpa=iframe.find_by_id('LblGPA')
            
            data.update({roll:gpa.value})       //appends the new data to our dictionary
            print roll, "done"  // success
            pass
        except :
            print roll, "skipped"       // missing rollnos are skipped
            pass
json.dump(data,f)           //store the dictionary in our file in hdd
f.close()       // very imp . close the file after use. 
