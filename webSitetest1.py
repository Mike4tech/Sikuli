#Automation of the post deploy test currenttly executed manually.
#This is a prototype created in the INT enviornment
#Mike Richardson January, 24, 2012
#
#Step 1 create new Net-MR feasability
#
# Declare variables for login
def CreateNetMRStudy():
        f = open("C:\\SHARE\\TestRunLogs\\PostDeployTest1.htm",'w')  #create simple logging
        f.write('<font color= "#347C17">Test Launched</font><br />')
        f.close()
        login='1066'
        password='test123'
        userid='214590'
        studyNameInt='post_deploy_test_Yes This Works Terrell'
        browser='C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe -private'
        enviornment='http://intnetmr.gmi-mr.com/admin/login.phtml'
        titleQuestion1='Question 1'
        questionText='Do You Want To Complete or Screen?'
        logic1='@LABEL1=[?2] STOP'
        f = open("C:\\SHARE\TestRunLogs\\PostDeployTest1.htm",'a')  #create simple logging
        f.write('<font color= "#347C17">Variables Initialized</font><br />')
        f.close()
        #studyNumber='need to copy and add this for later user
        #userid is for int
        #
        #Launch the FireFox instance, create a variable for this to cover other browsers
        App.open(browser)
        #maximize if fail is implicit that is max
        wait(2)
        #if exists("IEE.png", 5):
        #    click("1327468972721.png")
        #    wait(2) #verify ff is open and in private mode
        if exists("1327468022049.png", 5):
            f = open("C:\\SHARE\\TestRunLogs\\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">FF launched in Private Mode</font><br />')
            f.close()
        #    popup("test break")
        #
        #
            type("l",KeyModifier.CTRL)# places focus in the address bar
        #add code to expand browser window
            wait(2)
            paste(enviornment)
            wait(2)#add visual assertion later
            type(Key.ENTER)
            wait(2)
        #visual assertion
        if exists("LoginFormUse.png", 10):
            f = open("C:\\SHARE\\TestRunLogs\\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Net-MR login displayed</font><br />')
            f.close()
            type(Pattern("UserID.png").targetOffset(8,4), login)#login hover may cause failure to find input
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">User ID submitted</font><br />')
            f.close()
            type(Key.TAB)#to clear hover window
            type(Pattern("Password.png").similar(0.66).targetOffset(2,-1), password)
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Password submitted</font><br />')
            f.close()
            click("Login.png")
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Click on login</font><br />')
            f.close()
        #    popup("test break")
        #add next visual assertion
        if exists("Searchpartne.png", 10):
            click(getLastMatch())
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Found Search Partner Button</font><br />')
            f.close()
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Click On Search Partner Button</font><br />')
            f.close()
        #    popup("test break")
        #add visual assertion to verify search partner page displays
        if exists("Searchpartne-1.png", 10):
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Search Partner Page Displays</font><br />')
            f.close()
            type(Pattern("UserID-1.png").targetOffset(47,2), userid)
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">User ID submitted</font><br />')
            f.close()
        #    popup("test break")
            click("1327442896392.png")
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Search Button Clicked On</font><br />')
            f.close()
        #add visual assertion search result
        if exists("Searchresult.png", 10):
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Search Result Area Found</font><br />')
            f.close()
            click("LaunchNetMR.png")
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Click on Launch Net-MR button</font><br />')
            f.close()
        #add visual assertion for Net-MR page display
        if exists("A1AUA.png"):
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">NetMR page found</font><br />')
            f.close()
            click("1327443211865.png")
            wait (2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Projects Button Clicked On</font><br />')
            f.close()
            click("CreateNewPro.png")
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Clicked on Create New Project Button</font><br />')
            f.close()
        #add visual assertion create new project page displays
        if exists("CreateNewPro-1.png", 10):
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Create new project radio button found</font><br />')
            f.close()
            click("Next.png")
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Click on next</font><br />')
            f.close()
        #add visual assertion create a study
        if exists(Pattern("StudyDetails.png").targetOffset(66,19), 10):
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Study Details Founs</font><br />')
            f.close()
            type(Pattern("Title.png").targetOffset(151,-1), studyNameInt)
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Study Name submitted</font><br />')
            f.close()
            click("1327446490730.png")
            type(Key.PAGE_DOWN)#Need to add focus to make work or pull down bar
            wait(2)
            click("1327446490730.png")
            type(Key.PAGE_DOWN)#Need to add focus to make work or pull down bar
            wait(2)
        #    wait(2)
            click(Pattern("1327443804494.png").similar(0.83))
            wait(3)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Click on right arrow</font><br />')
            f.close()
            click("1327446490730.png")
            type(Key.PAGE_DOWN)#Need to add focus to make work or pull down bar
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Click on white space</font><br />')
            f.close()
            click("1327446490730.png")
            type(Key.PAGE_DOWN)#Need to add focus to make work or pull down bar
            wait(3)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17"Move page down</font><br />')
            f.close()
            wait(2)
            click("1327444398422.png")
        #capture screenshot of new questionaire number and page type Region,text()
            wait(2)
        #    popup("test break")
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Click on left arrow button</font><br />')
            f.close()
            click("1327446490730.png")
            type(Key.PAGE_DOWN)
            wait(2)
            click("1327444482214.png")
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Click on Right arrow button</font><br />')
            f.close()
        #add visual assertion study creation step 2 of 6
        if exists("tudyCreation.png", 10):
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Study creation step 2 locator found</font><br />')
            f.close()
            wait(3)
        if exists(Pattern("Passwordprot.png").targetOffset(-182,0), 10):
            click(Pattern("Passwordprot.png").targetOffset(-182,0))
            wait(2)
        #    popup("test break")
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Password protect de-selected</font><br />')
            f.close()
            click("1327446538860.png")
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">whitespace clicked on</font><br />')
            f.close()
            type(Key.PAGE_DOWN)
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Page moved down</font><br />')
            f.close()
            click(Pattern("Off.png").targetOffset(-13,-2))
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Off radio button selected</font><br />')
            f.close()
            click("1327445329023.png")
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Right Arrow button clicked on</font><br />')
            f.close()
        #click through page 3
            click("3.png")
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Right Arrow button clicked on page 3</font><br />')
            f.close()
        #click through page 4
            click("1327446812484.png")
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Right Arrow button clicked on page 4</font><br />')
            f.close()
        #click through page 5
            click("1327446773011.png")
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Right Arrow button clicked on page 5</font><br />')
            f.close()
        #    popup("test break")
        #click through page 6
            click("1327446538860.png")
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">White space clicked on</font><br />')
            f.close()
            type(Key.PAGE_DOWN)
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Page Moved Down</font><br />')
            f.close()
            click("1327446830881.png")
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Right Arrow button clicked on page 6</font><br />')
            f.close()
        #newly created study page is displayed
        #need to find way to copy the new study number and save as variable
        #start the Net-MR Design the newly created study
        #the easiest thing to do is assume the test users is using the latest study
        #Later strip the text add to clipboard and compare, this function wwill be needed elsewhere
        #in this app to string compare
            click(Pattern("Studynum.png").targetOffset(0,24))
        #    popup("test break")
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Study Number clicked on</font><br />')
            f.close()
        #the code above launches the newest study
        #add visual assertion for the manage project screen
        if exists("SettingsRhnd.png", 10):
            click("DesignTools.png")
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Study Info Settings Found</font><br />')
            f.close()
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Design tools button clicked on</font><br />')
            f.close()
            wait(4)
            click(Pattern("DsignTooIsHT.png").similar(0.78).targetOffset(48,-1))
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">HTML designer button clicked on</font><br />')
            f.close()
        #    popup("test break")
        #add visual assertion this step can take a while to render
        if exists("OPEDeleteThe.png", 30):
            wait(2)
            click("MdQS-1.png")
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Question Locator Found</font><br />')
            f.close()
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Add Question button clicked on</font><br />')
            f.close()
        #addvisual assertion for the new window launched
        if exists("AddQuestionS-2.png", 10):
            click("1327449492329-1.png")
            type(Key.DOWN+Key.DOWN+Key.DOWN+Key.ENTER)
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Question type selected</font><br />')
            f.close()
        if exists("AddQuestionS-2.png", 10):           
            click("Add-1.png")
            type(Pattern("Title-1.png").targetOffset(-22,14), titleQuestion1)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Question title added</font><br />')
            f.close()
            wait(4)
            type(Pattern("Questiontext.png").targetOffset(-42,16), questionText)
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Question Text Added</font><br />')
            f.close()
        #visual assertion verify add question 1 details added
        if exists(Pattern("Question1111-1.png").similar(0.84), 10):
            click(Pattern("1327472141942-1.png").targetOffset(-1,-15))
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">White Space clicked on</font><br />')
            f.close()
            type(Key.PAGE_DOWN)#Need to add focus to make work or pull down bar
            wait(3)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Page Moved Down</font><br />')
            f.close()
            click("1327535219783.png")
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">White Space clicked on</font><br />')
            f.close()
            type(Key.PAGE_DOWN)#moving page down without slider
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Page Moved Down</font><br />')
            f.close()
            click("BranchLogic-1.png")
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Click on identified branch logic</font><br />')
            f.close()
            type(Key.PAGE_DOWN)#moving page down without slider
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Page Moved Down</font><br />')
            f.close()
            wait(2)
        #assert visual of enter branch logic input
        if exists("EnterConditi-2.png", 10):
            type(Pattern("Enter-1.png").targetOffset(-13,10), logic1)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Enter Condition Locator Found</font><br />')
            f.close()
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Branch Logic Entered</font><br />')
            f.close()
            wait(3)
        #find droplist to change to after
        if exists("Before-3.png", 10):
            click(Pattern("Before-2.png").targetOffset(34,-1))
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Droplist Value Changed To After</font><br />')
            f.close()
            type(Key.DOWN+Key.ENTER)
            click("Add-3.png")
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Droplist Value Submitted</font><br />')
            f.close()
        #    click(Pattern("1327486277525-1.png").similar(0.96).targetOffset(-8,118)) 
        #    wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Clicked on location identifier</font><br />')
            f.close()
            type(Key.PAGE_DOWN)#moving page down without slider
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Move Page Down</font><br />')
            f.close()
            type(Pattern("1327475861855-1.png").similar(0.80).targetOffset(-67,0), Key.DELETE)
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Clear add response default</font><br />')
            f.close()
            type(Pattern("1327475861855-1.png").similar(0.80).targetOffset(-67,0), "2")
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Add response changed to 2</font><br />')
            f.close()
            click(Pattern("AddResponse-1.png").similar(0.82))
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Add response clicked on</font><br />')
            f.close()
        #assert do response entries display
        if exists(Pattern("1EditRespons-1.png").similar(0.81), 10):
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Response text found</font><br />')
            f.close()
            type(Pattern("1Edithtml-1.png").similar(0.87).targetOffset(-43,8), "complete")
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Response Complete entered</font><br />')
            f.close()
            type(Pattern("2Edithtml-1.png").targetOffset(-43,6), "screen")
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Response Screen entered</font><br />')
            f.close()
            type(Key.F12)
            #click(Pattern("F12-1.png").targetOffset(20,3))
            wait(4)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Responses saved</font><br />')
            f.close()
            wait(5)
        #launch survey verification tuned to full from start
        click(Pattern("FullPreviewF-1.png").similar(0.84).targetOffset(-13,22))
        wait(5)
        f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
        f.write('<font color= "#347C17">Survey Verification Launched</font><br />')
        f.close()
        #the following is an example of removing language and usind specific images
        #and geometric primitives
        if exists("GL0BLT-1.png", 10):
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Survey page found</font><br />')
            f.close()
            click(Pattern("1327477674846-1.png").targetOffset(-1,-19))
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Top radio button selected</font><br />')
            f.close()
            click(Pattern("1327477754253-1.png").targetOffset(8,0))
            wait(4)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Next arrow selected</font><br />')
            f.close()
        if exists("GL0BLTESArem-1.png", 10):
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Exit locator found</font><br />')
            f.close()
            click(Pattern("IEIEnRKEBXpI-1.png").targetOffset(51,-62))
            wait(2) 
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Exit survey test 1</font><br />')
            f.close()
        click(Pattern("FullPreviewF-1.png").similar(0.84).targetOffset(-13,22))
        wait(4)
        f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
        f.write('<font color= "#347C17">Survey Verification Launched</font><br />')
        f.close()
        #the following is an example of removing language and usind specific images
        #and geometric primitives
        if exists("GL0BLT-1.png", 10):
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Survey page found</font><br />')
            f.close()
            click(Pattern("1327477674846-1.png").targetOffset(0,12))
            wait(2)
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Bottom radio button selected</font><br />')
            f.close()
            click(Pattern("1327477754253-1.png").targetOffset(8,0))
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Next arrow selected</font><br />')
            f.close()
        if exists("GL0BLTESTPAr-1.png", 10):
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Exit locator found</font><br />')
            f.close()
            click(Pattern("IEIEnRKEBXpI-1.png").targetOffset(51,-62))
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Exit survey test 2</font><br />')
            f.close()
            f = open("C:\SHARE\TestRunLogs\PostDeployTest1.htm",'a')  #create simple logging
            f.write('<font color= "#347C17">Exit Create Survey in Net-MR</font><br />')
            f.close()
            App.close(browser)
def Looper():
    count = 0
    while (count < 10):
#        f = open("C:\SHARE\TestRunLogs\IterationCounter.htm",'w'
#        f.write('CreateNet-MRStudy iteration ' + (str (count)) + '<br />')
#        f.close()
        CreateNetMRStudy()
    count = count+1
    exit()
Looper()
        
    
