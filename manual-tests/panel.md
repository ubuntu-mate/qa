# MATE Panel

MATE Panel is preinstalled on MATE DE. It is usually shown on the top and down parts of the screen. Its main executable is named `mate-panel`.

## Applets

MATE Panel has a lot of preinstalled applets.

### Testing applets

MATE Panel allows to test any applet by using special program named `mate-panel-test-applets`.

Steps to test:

1. Open MATE Terminal
1. Execute `mate-panel-test-applets`
1. In the *Test applet utility* select needed *Applet* and then click *Execute*
1. Ensure that applet is shown in separated window and it looks as expected
1. Close the *Test applet utility*

Expected results:

* the *Test applet utility* was opened, all applets look and operate as expected.

### Add and remove applets

MATE Panel allows user to add and remove applets.

#### Add custom application launched

Steps to test:

1. Move mouse cursor above top MATE Panel
1. Do a right mouse click
1. Select *Add to Panel*
1. Choose *Custom Application Launcher* and click *Add*
1. Fill all needed fields with needed information (for example: *Type* : *Application*, *Name:* `MATE Calculator`, *Command*: `mate-calc`) and click *OK*
1. Test the applet by clicking on it

Expected results:

* user is able to add *Custom Application Launcher* applet to the Panel, the application from it can be launched normally.

#### Add application launcher

Steps to test:

1. Move mouse cursor above top MATE Panel
1. Do a right mouse click
1. Select *Add to Panel*
1. Choose *Application Launcher* and click *Add*
1. Select needed application from the list (or use search) and click *Add*
1. Test the applet by clicking on it

Expected results:

* user is able to add *Application Launcher* applet to the Panel, the application from it can be launched normally and has correct icon for selected application.

#### Add applet

Steps to test:

1. Move mouse cursor above top MATE Panel
1. Do a right mouse click
1. Select *Add to Panel*
1. Choose needed applet in the opened *Add to Panel* window and click *Add*
1. Close the *Add to Panel* by clicking *Close*
1. Test the just added applet

Expected results:

* user is able to add applet to the MATE Panel, applet looks and operates well.

#### Remove applet

Steps to test:

1. Move mouse cursor above the some applet of top MATE Panel
1. Do a right mouse click
1. Select applet to remove and click *Remove From Panel*

Expected results:

* user is able to remove applet from the MATE Panel, removing the applet do not crash the Panel.

### Add and test some useful applets

#### Clock applet

Steps to test:

1. Move mouse cursor above top MATE Panel
1. Do a right mouse click
1. Select *Add to Panel*
1. Choose *Clock* applet
1. Do right mouse click on newly added Clock applet, select *Preferences*
1. Switch to *Location* tab and add your favorite locations
1. Switch to *General* tab and uncheck all checkboxes then check them back
1. Switch to *Weather* tab and change all values
1. Close Clock Preferences window
1. Click on Clock applet

Expected results:

* user is able to add new locations, view calendar, weather, date and time in them.

#### Workspace Switcher

##### Setting workspace switcher preferences

Steps to test:

1. Move mouse cursor above top MATE Panel
1. Do a right mouse click
1. Select *Add to Panel*
1. Choose *Workspace Switcher* applet
1. Do right mouse click on newly added *Workspace Switcher* applet, select *Preferences*
1. Set *Switcher* to *Show only the current workspace*, then to *Show all workspaces in* to `2` *rows*, then back to `1` row
1. Set *Number of workspaces* to `8` and then back to `4`
1. Set new *Workspace names* by double clicking on their names (*Workspace 1* and so on), check *Show workspace names in switcher* and then uncheck it

Expected results:

* workspace switcher correctly reacts on changing of its preferences.

##### Dragging windows between workspaces

Steps to test:

1. Move mouse cursor above top MATE Panel
1. Do a right mouse click
1. Select *Add to Panel*
1. Choose *Workspace Switcher* applet
1. Open some application on first workspace
1. Place cursor on the 1st workspace in the *Workspace switcher* applet, press left mouse button and drag the window miniature to other workspace
1. Move to the workspace with dragged window

Expected results:

* workspace switcher shows window contour on the first workspace, then this window got moved to other workspace.

## Panel reset

Any panel may be reseted to its default view for current panel layout. Do not reset panel appearance on your daily driver systems without screenshot or other way of backup.

Steps to test:

1. Reset the panel
    * Move mouse above needed MATE Panel and do right mouse click and select *Reset Panel*
    * Use terminal and run `mate-panel --reset` command here

1. Ensure that panel was reseted to the current layout defaults

Expected results:

* MATE Panel was running with some appearance, then it was reseted to current layout default and it is still running.

## Panel restart/replace

Steps to test:

1. Open MATE Terminal
1. Execute `mate-panel --replace &`
1. Close MATE Terminal

Expected results:

* MATE Panel was running with some appearance, then it was restarted/replaced and it is still running.

## Using Run dialog

Steps to test:

1. Open *Run Application* dialog

    * Press `<Alt>+<F2>`
    * Open terminal and execute `mate-panel --run-dialog`

1. Enter application name - for example `mate-calc` and click *Run*
1. Ensure that application is started

Expected results:

* the *Run Application* window was shown, reacted on the user input and started needed application after click on *Run*.

## Screenshot

MATE Panel package provides `mate-panel-screenshot` for creating screenshots. It is a just a symlink to `mate-screenshot`.

Steps to test:

1. Open MATE Terminal
1. Execute `mate-panel-screenshot`
1. Save the screenshot somewhere

Expected results:

* The *Save screenshot* window was shown, user is able to save screenshot.

## Panel operations

MATE panels are very customizable. User can add, remove, move, auto-hide and manually hide them.

### Add new panel

Steps to test:

1. Do right mouse click on any MATE Panel
1. Select *New Panel*
1. Do right mouse click on this MATE Panel and click *Delete This Panel*

Expected results:

* new MATE Panel was created and user is able to delete it.

### Set panel orientation

Steps to test:

1. Do right mouse click on any MATE Panel and select *Properties*
1. Change panel orientation to all orientations including *Top*, *Bottom*, *Left* and *Right*
1. Click *Close*

Expected results:

* user is able to change MATE Panel orientation

### Set panel size

Steps to test:

1. Do right mouse click on any MATE Panel and select *Properties*
1. Change panel size to the minimal value (usually 16)
1. Change panel size to the maximal value (usually 240)
1. Change panel size back to the default value (usually 28)
1. Click *Close*

Expected results:

* user is able to change MATE Panel size, its contents are scaled accordingly.

### Set panel expand

Steps to test:

1. Do right mouse click on any MATE Panel and select *Properties*
1. Uncheck *Expand* checkbox
1. Check *Expand* checkbox again
1. Click *Close*

Expected results:

* MATE panel shrinks to its minimal width (needed for its elements) with *[ ] Expand* and fills whole screen width (for horizontal panel) or height (for vertical panel) with *[v] Expand*.

### Set panel autohide

Steps to test:

1. Do right mouse click on any MATE Panel and select *Properties*
1. Check *Autohide*
1. Click *Close*
1. Move mouse cursor out of this MATE Panel
1. Ensure that panel hides automatically
1. Do right mouse click on any MATE Panel and select *Properties*
1. Uncheck *Autohide*
1. Move mouse cursor out of this MATE Panel
1. Ensure that panel does not hide automatically
1. Click *Close*

Expected results:

* MATE panel auto-hide is controlled by *Autohide* checkbox and changes behavior respectively.

### Using panel hide buttons

Steps to test:

1. Do right mouse click on any MATE Panel and select *Properties*
1. Check *Show hide buttons* and *Arrows on hide buttons*
1. Press on left hide button to hide panel to the left and then press it again to show
1. Press on right hide button to hide panel to the right and then press it again to show
1. Uncheck *Show hide buttons*
1. Click *Close*

Expected results:

* MATE panel hides to the left of to the right using buttons on panel ends.

### Setting panel background

Steps to test:

1. Do right mouse click on any MATE Panel and select *Properties*
1. Switch to *Background* tab
1. Select *Solid color* and choose needed color
1. Select *Background image* and choose needed image
1. Select the default value - *None (use system theme)*
1. Click *Close*

Expected results:

* MATE panel changes background to the solid color, then to user-defined background image and then to default color from the theme.

## Applications menus

Depending on the layout of MATE Panel menus with applications may look different. But in anyway they allow to copy application icons by dragging to the desktop and to the panel.

### Copying application icon from the application menu to the Desktop

Steps to test:

1. Open *Applications* menu or *Brisk* menu
1. Navigate to the needed application icon
1. Drag application icon to the Desktop
1. Double-click the just-copied application icon on the desktop.

Expected result:

* user is able to drag application icon from the Applications/Brisk menu to the Desktop and is able to run application using its icon on the Desktop.

### Copying application icon from the application menu to the Panel

Steps to test:

1. Open *Applications* menu or *Brisk* menu
1. Navigate to the needed application icon
1. Drag application icon to the Panel
1. Click the just-copied application icon on the Panel.

Expected result:

* user is able to drag application icon from the Applications/Brisk menu to the Panel and is able to run application using its icon on the Panel.
