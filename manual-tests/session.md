# MATE session

## Startup Programs

Launch *Startup Applications Preferences* from *System*→*Preferences*→*Personal*→*Startup Applications* or using `mate-session-properties`.

Steps to test:

1. Navigate to *Startup Programs* tab
1. Click *Add* to add new program to autostart - fill the fields (*Name:* `pluma`, *Command:* `pluma`) and click *Add*
1. Close the *Startup Applications Preferences* window and logout
1. Login back and ensure that Pluma was started with the system
1. Open *Startup Applications Preferences* again and remove just created Pluma entry from the list

## Session auto-restore

Launch *Startup Applications Preferences* from *System*→*Preferences*→*Personal*→*Startup Applications* or using `mate-session-properties`.

Steps to test:

1. Navigate to *Options* tab
1. Check the *Automatically remember running applications when logging out* checkbox
1. Open as many GTK-based applications as you can - for example Firefox, Caja, Pluma, Atril, MATE Terminal, SeaMonkey, Zotero and so on
1. Logout
1. Login back and ensure that last opened applications are now opened as it was before logout

