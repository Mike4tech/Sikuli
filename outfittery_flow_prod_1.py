#outfittery flow in prod site
#we will set a region first
Region(1,0,1364,767)
#now we will verify of the cookie prompt exists, if it does we will click on it
#establish simple logging
f = open("C:\\Users\\Heinz\\Downloads\\Desktop\\Outfittery flow automation prototype.htm",'w')
f.write('<font color= "#347C17">Set HTML logging</font><br />')
f.close()
if exists("1425491568842.png"):
   click("1425491628725.png"):
wait(1)
elif exists("1425491718483.png"):
#using target offset and asymetrical image to increase accuracy of image
   click(Pattern("1425491747339.png").targetOffset(2,-20))
wait("1425491952451.png",20)
#screen capture follows, will need t revise flow later
exists("1425492522230.png")
#click on the following, script this
exists("1425492536371.png")
#must scroll down to get to the following, must click on the next
#must exercise all links note this
#abstract the images out of this 
exists("1425492595527.png")
click("1425492704206.png")
# if next clicked on with no selection the folowing appears briefly
"1425492813854.png"

#if image is slected it appears as the following, crop and detune to isolate the chjeck mark in the image
exists("1425493050624.png")
#after go to step 2
exists("1425493128406.png")






    

