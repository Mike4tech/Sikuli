f = open("C:\\SikuliLogs\\GMItest.htm",'w')
f.write('<font color= "#347C17">GMI Web GUI test demo</font><br />')
f.write('<font color= "#347C17">Launch FireFox</font><br />')
App.open("c:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
f.write('<font color= "#347C17">FireFox Launched</font><br />')
wait(5) # make sure window is ready add exists assertion later
type("l", KeyModifier.CTRL)#direct focus to the address bar
f.write('<font color= "#347C17">Focus directed to the address bar</font><br />')
paste("https://www.globaltestmarket.com/")#launch the GMI site
wait(1)
type(Key.ENTER)
f.write('<font color= "#347C17">Launch the GMI Site</font><br />')
#use visual check to verify page is launched
wait(,30)
#add if not exists statement
f.write('<font color= "#347C17">GMI Site displayed</font><br />')
click(Pattern().targetOffset(0,24))
click("__SIKULI-CAPTURE-BUTTON__")

popup("Continue to verify HOME link navigates to home page")
click(Pattern().targetOffset(0,28))
f.write('<font color= "#347C17">Click Home Link</font><br />')
wait(2)
click(Pattern().targetOffset(53,-2))
f.write('<font color= "#347C17">Click join link 2</font><br />')
# add visual assertion
wait(2)
click(Pattern().targetOffset(0,28))
# add visual assertion if not exists
f.write('<font color= "#347C17">Click Home Link</font><br />')
wait(2)
click()
f.write('<font color= "#347C17">Click Join Link 3</font><br />')
f.close