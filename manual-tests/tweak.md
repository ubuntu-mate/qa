# MATE Tweak

MATE Tweak is preinstalled on MATE DE. Its executable is named `mate-tweak`.

## *Desktop* icons

Steps to test:

1. Open MATE Tweak
1. Select *Desktop* tab
1. Un-check *Show Desktop Icons* checkmark and ensure that desktop icons are not shown
1. Check *Show Desktop Icons* checkmark and ensure that desktop icons are now shown again
1. Optionally check all desktop icons (*Computer*, *Home*, *Trash*, *Network* and *Mounted Volumes*) and ensure that all the are shown on desktop

Expected results:

* desktop icons are shown in accordance to the settings on the Desktop tab of MATE Tweak.

## *Panel* settings

MATE Tweak allows to select layouts for the MATE Panel

### Choosing MATE Panel layout

Steps to test:

1. Open MATE Tweak
1. Select *Panel* tab
1. Select a panel layout to change the user interface:

    * Contemporary
    * Cupertino
    * Familiar
    * Mutiny
    * Netbook
    * Pantheon
    * Redmond
    * Traditional

1. Ensure that every panel layout were applied and MATE Panels were not crashed

Expected results:

* MATE Tweak switches panel layouts, MATE Panels react as usual and do not crash.

### Setting panel menu features

Steps to test:

1. Open MATE Tweak
1. Select *Panel* tab
1. Select *Traditional* panel layout to change the user interface
1. Check/uncheck all/one of the following checkboxes: *Show Applications*, *Show Places*, *Show System*
1. Ensure that MATE Panel reacts to the changes of the aforementioned checkboxes

Expected results:

* MATE Panel reacts to the changes of the aforementioned checkboxes, MATE Panel and its applets do not crash.

### Setting panel features

Steps to test:

1. Open MATE Tweak
1. Select *Panel* tab
1. Select *Traditional* panel layout to change the user interface
1. Check/uncheck all/one of the following checkboxes: *Enable Dock*, *Enable HUD*, *Enable pull-down terminal*, *Enable keyboard LED*
1. Select the icon size for the panel icons

Expected results:

* MATE Panel reacts to the changes of the aforementioned checkboxes, pull-down  terminal (`tilda`) reacts on `<F12>` key, dock is shown on moving mouse to the bottom center of the screen, the size of panel icons changes as user requested.

## *Windows* settings

### Setting performance

#### Enabling and disabling animations

Steps to test:

1. Open MATE Tweak
1. Select *Windows* tab
1. Check/uncheck *Enable animations*
1. Ensure that changes were applied

Expected results:

* animation related changes are applied, desktop do not crash.

#### Show window content when moving windows

Steps to test:

1. Open MATE Tweak
1. Select *Windows* tab
1. Check *Do not show window content when moving windows* checkmark
1. Move MATE Tweak window and ensure that it has wire frame and its contents are not shown
1. Uncheck *Do not show window content when moving windows* checkmark mark

Expected results:

* unchecking *Do not show window content when moving windows* hides window contents and disables *Enable window snapping* functionality.

### Setting window behaviour

#### Window snapping

Steps to test:

1. Open MATE Tweak
1. Select *Windows* tab
1. Uncheck *Enable window snapping* checkmark
1. Open any other application and try to snap its window to the left of to the right part of the screen, then close it
1. Check *Enable window snapping* checkmark back

Expected results:

* Window snapping changes in accordance to the state of *Enable window snapping* checkmark.

#### Undecorate maximized windows

Steps to test:

1. Open MATE Tweak
1. Select *Windows* tab
1. Check *Undecorate maximized windows* checkmark
1. Open any other application and try to maximize its window and ensure that it does not have window decoration, then close it
1. Uncheck *Undecorate maximized windows* checkmark
1. Open any other application and try to maximize its window and ensure that it has window decoration, then close it

Expected results:

* decoration of the maximized window is changed in accordance to the state of *Undecorate maximized windows* checkmark.

#### Maximizing new windows

Steps to test:

1. Open MATE Tweak
1. Select *Windows* tab
1. Uncheck *Do not auto-maximize new windows* checkmark
1. Open MATE Terminal and ensure that its window is maximized, then close it
1. Check *Do not auto-maximize new windows* checkmark
1. Open MATE Terminal and ensure that its window is not maximized, then close it

Expected results:

* window maximization is changed in accordance to the state of *Do not auto-maximize new windows* checkmark.

### Setting window appearance

Steps to test:

1. Open MATE Tweak
1. Select *Windows* tab
1. Choose one of the values from the *Window control placement* drop-down menu and ensure that position of controls were changed

Expected results:

* the position of window controls are changed to the value in drop-down list.

### Setting HiDPI

Steps to test:

1. Open MATE Tweak
1. Select *Windows* tab
1. Choose one of the values from the *Select a window scaling factor* drop-down menu and ensure that it changes the scaling

Expected results:

* the desktop scaling changes depending the value from drop-down list.

### Setting fonts

Steps to test:

1. Open MATE Tweak
1. Select *Windows* tab
1. Click on *Fonts* button
1. In the Appearance window click on *Details* button, disable *Automatic detection* and choose needed *Dots per inch (DPI)* value

Expected results:

* font size and DPI are set to the user-defined values.

### Selecting window manager

MATE DE may work wits its default window manager named `marco` and with advanced window managers like Compton and Compiz.

#### Using and selecting Marco without compositor

Steps to test:

1. Open MATE Tweak
1. Select *Windows* tab
1. Under *Window manager* switch *Select window manager* to *Marco (No compositor)*

Expected result:

* Window manager was switched to Marco without compositor, desktop effects are minimal (for example window-snapping use wire frames).

#### Using and selecting Marco with adaptive compositor

Steps to test:

1. Open MATE Tweak
1. Select *Windows* tab
1. Under *Window manager* switch *Select window manager* to *Marco (Adaptive compositor)*

Expected result:

* Window manager was switched to Marco with adaptive compositor, desktop effects are good.

#### Using and selecting Compton

To use Compton we need to install it first with `sudo apt-get install compton`.

Steps to test:

1. Open MATE Tweak
1. Select *Windows* tab
1. Under *Window manager* switch *Select window manager* to *Marco (Compton GPU compositor)*

Expected result:

* Window manager was switched to Compton, desktop effects are better.

#### Using and selecting Compiz

To use Compiz we need to install it first with `sudo apt install compiz compiz-core compiz-mate compiz-plugins compiz-plugins-default`.

Steps to test:

1. Open MATE Tweak
1. Select *Windows* tab
1. Under *Window manager* switch *Select window manager* to *Compiz (Advanced GPU accelerated desktop effects)*

Expected result:

* Window manager was switched to Compiz, desktop effects are full-featured.

