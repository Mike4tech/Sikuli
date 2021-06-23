f = open("C:\\FyberTest.htm",'a')
f.write('<font color= "#347C17">Offers button appears</font><br />')
f.close()
#f.write('<font color= "#347C17">Launch FireFox</font><br />')

global count
count = 10
def LoopSignInConferenceExit():
    global SmokeTest
    global WebPath
    global count
    count = 0
    while (count < 10):
