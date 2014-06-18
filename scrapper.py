from splinter import Browser
import json
data=dict()
browser = Browser('firefox')
browser.visit('http://www.nitt.edu/prm/ShowResult.htm')
roll=110112000
f=open('gpasem4','w')
while(roll<110112100):
    #browser.type('TextBox1',roll)
    roll=roll+1
    with browser.get_iframe('main') as iframe:  
        try :
            iframe.fill('TextBox1',roll)
            iframe.find_by_name('Button1').click()
            browser.find_by_xpath('//select[@id="Dt1"]/option[@value="96"]')._element.click()
            
            name=iframe.find_by_id('LblName')
            #gpa=iframe.find_by_id('LblGPA')
            
            data.update({roll:gpa.value})
            print roll, "done"
            pass
        except :
            print roll, "skipped"
            pass
json.dump(data,f)
f.close()
