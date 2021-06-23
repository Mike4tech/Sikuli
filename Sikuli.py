#executes deletes via the Archimedes GUI
#add check for If exists to make delete response dynamic
#add logging function for each iteration
#create the log first then use the append code block
#make the log into a def
#pre condition is to execute the search QA MR 5-28 which returns 1198 results
#import timeit include timeit to time the exwecution and events

def Logger():
    f = open("C:\\Users\\mRichardson\\Desktop\\DeleteMay30.htm",'a')
    f.write('<font color= "#cc0066">DeletedMay30</font><br />')
    f.close()

def DynamicDelete():
   #if exists("1401309184355.png",3):
    #click("1401309263331.png")
   #if exists("1401310411618.png",3):
   # click("1401310427839.png") 
   #if  exists("1401311723835.png", 20):
   # wait(1)
   # click("1401409634808.png")
   #if exists(Pattern("1401461680603.png").similar(0.93).targetOffset(9,0), 20):
    #click("1401461776065.png") 
   exists("1401465650432.png")
   
   if exists("1401310584489.png",20):
    click("1401310599122.png")
   if exists("1401311114594.png",20):
    click(Pattern("1401311133207.png").targetOffset(-21,0))
while True:
   DynamicDelete()
   Logger()


   