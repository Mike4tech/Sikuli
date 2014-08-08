Create configuration files

from sikuli.Sikuli import * #


#userB config
import ConfigParser
config = ConfigParser.RawConfigParser()
#cfgfile = open("Z:\\ZZZautomation\\Sikuli\\Config\\UserA.ini",'w')
cfgfile = open("C:\SikuliTest\UserB.ini",'w')#local config file
#change path to desired location for the cfg file

#Install any user
config.add_section('Install')
#path requires mapping of share to z
config.set('Install', 'dirname',"Z:\\BUILDS\\Daily_BUILDS\\QA_MainBranch_Install\\*.install" )
config.set('Install', 'filespec',"setup.exe")
#EulaParamerters
config.add_section('EULA')
#config.set('EULA','BundlePathEULA',"Z:\\ZZZautomation\\Sikuli\\ImageLibrary\\96dpi\\SignIn") file location changed to local a
config.set('EULA','BundlePathEULA',"C:\\SikuliTest\\ImageLibrary\\96dpi\\SignIn")
config.set('EULA','SignIn_EULA',)
#config.set('EULA','EULA_TOF1E',"497")
#config.set('EULA','EULA_TOF2E',"489")
config.set('EULA','SignIn_MediaRouter',)
#MediaRouterParameters any user
config.add_section('MediaRouter')
config.set('MediaRouter','BundlePathMediaRouter',"C:\\SikuliTest\\ImageLibrary\\96dpi\\SignIn")
config.set('MediaRouter','SignIn_MediaRouter',)
config.set('MediaRouter','MediaRouter_TOF1M',"147")
config.set('MediaRouter','MediaRouter_TOF2M',"7")
config.set('MediaRouter','MediaRouter_TOF3M', "123")
config.set('MediaRouter','MediaRouter_TOF4M', "63")
config.set('MediaRouter','SignIn_OKButton',)
#SignInParameters set for userA
config.add_section('SignIn')
config.set('SignIn','BundlePathSignIn',"C:\\SikuliTest\\ImageLibrary\\96dpi\\SignIn")
config.set('SignIn','SignIn_Launch',)

config.set('SignIn','SignIn_SignIn',)#not sure of the function
config.set('SignIn','TOF1S',"-98",)
config.set('SignIn','TOF2S',"-88",)
config.set('SignIn','SignIn_BlankPanel',)
config.set('SignIn','SignIn_PasswordInput',)
config.set('SignIn','TOF1L',"-95",)
config.set('SignIn','TOF2L',"-15",)
config.set('SignIn','SignIn_SignInButton',)
config.set('SignIn','SignIn_OKButton',)
config.set('SignIn','TOF1LS',"-62",)
config.set('SignIn','TOF2LS',"113",)
config.set('SignIn','LoginUser',"michael.richardson02@X10.hphalo.net")#add ability to take users from a list
config.set('SignIn','Password',"skyroom")
config.set('SignIn','SignIn_EULA',)
config.set('SignIn','TOF1E',"506")
config.set('SignIn','TOF2E',"444")
#ContactList UserA
config.add_section('ContactList')
config.set('ContactList','BundlePathContactList', "C:\\SikuliTest\\ImageLibrary\\96dpi\\ContactList")
config.set('ContactList','ContactList_WelcomePanel',)
config.set('ContactList','ContactList_AddContact',)
config.set('ContactList','ContactList_Add',)
config.set('ContactList','ContactList_AddContactUser',"michael.richardson01")#Add a path to user B login ID
config.set('ContactList','ContactList_GreenDot',)
config.set('ContactList','TOF1CL',"135")
config.set('ContactList','TOF2CL',"81")
#ContactList accept add user userB
config.set('ContactList','ContactList_AcceptAddToList',)
config.set('ContactList','ContactList_AddContactUserB',"michael.richardson02")#Add a path to user B login ID
config.set('ContactList','ContactList_GreenDot',)# this is a dupe
config.set('ContactList','AcceptAddToList_TOF3CL',"89")#target offset for ContactList_AcceptAddToList.png
config.set('ContactList','AcceptAddToList_TOF4CL',"40")
#contactList remove contact
config.set('ContactList','ContactList_MessageVerifyRemoval',)
config.set('ContactList','TOF13CL',"88")#specific to b accept remove message
config.set('ContactList','TOF14CL',"37")

#config.set('ContactList','ContactList_SignOut',"ContactList_SignOut.png")
#contactList sign out
config.set('ContactList','ContactList_DropList',)
config.set('ContactList','ContactList_SignOut',)
config.set('ContactList','TOF5CL',"17")
config.set('ContactList','TOF6CL',"-1")
config.set('ContactList','TOF9CL',"0")
config.set('ContactList','TOF10CL',"-17")
config.set('ContactList','TOF11CL',"92")
config.set('ContactList','TOF12CL',"39")
#Conference A invites B
config.add_section('Conference')
config.set('Conference','BundlePathConference', "C:\\SikuliTest\\ImageLibrary\\96dpi\\Conference")
config.set('Conference','Conference_GreenDot',)
config.set('Conference','Conference_BlueLaunchWindow',)
config.set('Conference','Conference_Start',)
config.set('Conference','Conference_InConferenceSpeaker',)
config.set('Conference','Conference_MeetingSetupTimeout',)
config.set('Conference','Conference_Close',)
config.set('Conference','Conference_MeetingRequestDeclined',)
config.set('Conference','Conference_AcceptMeetingRequest',)
config.set('Conference','TOF5CL',"-78")
config.set('Conference','TOF6CL',"47")
config.set('Conference','Conference_ControlPanel',)#Images used for the functiondrawlens
config.set('Conference','Conference_DrawLens',)
config.set('Conference','Conference_StopSharing',)
config.set('Conference','Conference_Leave',)
config.set('Conference','Conference_ViewingLens',)
config.set('Conference','Conference_EndedAllLeft',)
config.set('Conference','TOF7CL',"136")
config.set('Conference','TOF8CL',"64")
config.set('Conference','ContactList_DropList',"ContactList_DropList")
config.set('Conference','TOF9CL',"126")
config.set('Conference','TOF10CL',"46")


#ExitVCDKillProcess
config.add_section('Desktop')
config.set('Desktop','BundlePathDesktop', "C:\\SikuliTest\\ImageLibrary\\96dpi\\Desktop")

config.set('Desktop','Desktop_ExpandSysTray',)
config.set('Desktop','Desktop_SysTrayClose',)
config.set('Desktop','Desktop_SysTrayIcon',)
config.set('Desktop','Desktop_SysTrayIcon_RTClickMenu',)
config.set('Desktop','TOF1DK',"-3")
config.set('Desktop','TOF2DK',"14")




config.write(cfgfile)

#f = open("Z:\\ZZZautomation\\Sikuli\\Web\\functionCreateConfigFileA.htm",'w')
popup("Configuration File Created Successfully")
#f.write ('Configuration File Created Successfully<br />')#
cfgfile.close()
#f.close()
exit()






Configuration file:

[ContactList]

tof10cl = -17

tof2cl = 81

contactlist_droplist = ContactList_DropList.png

acceptaddtolist_tof3cl = 89

contactlist_addcontactuserb = michael.richardson02

contactlist_messageverifyremoval = ContactList_MessageVerifyRemoval.png

contactlist_addcontactuser = michael.richardson01

contactlist_signout = ContactList_SignOut.png

tof14cl = 37


contactlist_welcomepanel = ContactList_WelcomePanel.png

bundlepathcontactlist = C:\SikuliTest\ImageLibrary\96dpi\ContactList

tof6cl = -1

tof13cl = 88

contactlist_acceptaddtolist = ContactList_AcceptAddToList.png

acceptaddtolist_tof4cl = 40

contactlist_greendot = ContactList_GreenDot.png

tof12cl = 39

tof5cl = 17

contactlist_addcontact = ContactList_AddContact.png

contactlist_add = ContactList_Add.png

tof11cl = 92

tof9cl = 0

tof1cl = 135



[Desktop]

desktop_systrayclose = Desktop_SysTrayClose.png

tof2dk = 14

desktop_expandsystray = Desktop_ExpandSysTray.png

tof1dk = -3

desktop_systrayicon = Desktop_SysTrayIcon.png

bundlepathdesktop = C:\SikuliTest\ImageLibrary\96dpi\Desktop

desktop_systrayicon_rtclickmenu = Desktop_SysTrayIcon_RTClickMenu.png



[MediaRouter]


mediarouter_tof3m = 123

signin_okbutton = SignIn_OKButton.png

signin_mediarouter = SignIn_MediaRouter.png

mediarouter_tof4m = 63

mediarouter_tof1m = 147

mediarouter_tof2m = 7

bundlepathmediarouter = C:\SikuliTest\ImageLibrary\96dpi\SignIn



[EULA]

signin_mediarouter = SignIn_MediaRouter.png

signin_eula = SignIn_EULA.png

bundlepatheula = C:\SikuliTest\ImageLibrary\96dpi\SignIn



[Install]

dirname = Z:\BUILDS\Daily_BUILDS\QA_MainBranch_Install\*.install

filespec = setup.exe



[SignIn]

signin_blankpanel = SignIn_BlankPanel.png

signin_signin = SignIn_SignIn.png

signin_okbutton = SignIn_OKButton.png

signin_eula = SignIn_EULA.png

tof1e = 506

tof2e = 444

tof1ls = -62


tof1s = -98

tof2s = -88

tof2l = -15

tof2ls = 113

bundlepathsignin = C:\SikuliTest\ImageLibrary\96dpi\SignIn

signin_signinbutton = SignIn_SignInButton.png

tof1l = -95

signin_launch = SignIn_Launch.png

password = skyroom

signin_passwordinput = SignIn_PasswordInput.png

loginuser = michael.richardson02@X10.hphalo.net



[Conference]

conference_bluelaunchwindow = Conference_BlueLaunchWindow.png

tof10cl = 46

contactlist_droplist = ContactList_DropList

conference_greendot = Conference_GreenDot.png

conference_drawlens = Conference_DrawLens.png

conference_inconferencespeaker = Conference_InConferenceSpeaker.png

tof6cl = 47

conference_viewinglens = Conference_ViewingLens.png

conference_meetingsetuptimeout = Conference_MeetingSetupTimeout.png

bundlepathconference = C:\SikuliTest\ImageLibrary\96dpi\Conference

tof8cl = 64

tof7cl = 136


tof5cl = -78

conference_controlpanel = Conference_ControlPanel.png

conference_stopsharing = Conference_StopSharing.png

conference_endedallleft = Conference_EndedAllLeft.png

conference_leave = Conference_Leave.png

conference_start = Conference_Start.png

conference_acceptmeetingrequest = Conference_AcceptMeetingRequest.png

conference_meetingrequestdeclined = Conference_MeetingRequestDeclined.png

conference_close = Conference_Close.png

tof9cl = 126













































