#outfittery flow automation prototype 
#created by Mike Richardson using SikuliX
#only works with JRE7 and lower JRE8 breaks this
#capture region to begin with
Region(0,0,1365,767)
if exists("1425490119453.png"):
   f = open("C:\\Users\\Heinz\\Downloads\\Desktop\\Outfittery flow automation prototype.htm",'w')
   f.write('<font color= "#347C17">Lets go button found</font><br />')
   f.close()
#initiate action
click("1425489872002.png")
#   f = open("C:\\Users\\Heinz\\Downloads\\Desktop\\Outfittery flow automation prototype.htm",'w')
#   f.write('<font color= "#347C17">Lets go button clicked on</font><br />')
#   f.close()
#now user is in survey
#simple top selection without image recognition, usng relative positioning
wait(1)
#target offset from text, will always pick the image no matter waht it is
click(Pattern("1425490896625.png").targetOffset(74,75))
f = open("C:\\Users\\Heinz\\Downloads\\Desktop\\Outfittery flow automation prototype.htm",'w')
f.write('<font color= "#347C17">Lets go button found</font><br />')
f.close()



  
