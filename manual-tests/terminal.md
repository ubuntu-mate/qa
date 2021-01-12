# MATE Terminal

MATE Terminal is preinstalled on MATE DE. It may be called from terminal as `mate-terminal` or by using `<Ctrl>+<Alt>+<T>` in MATE DE.

## File

### Opening terminal window

Steps to test:

1. Open MATE Terminal
1. Select *File* → *Open Terminal* (or `<Shift>+<Ctrl>+<N>`)

Expected result:

* New terminal window is opened.

### Opening terminal tab

Steps to test:

1. Open MATE Terminal
1. Select *File* → *Open Tab* (or `<Shift>+<Ctrl>+<T>`)

Expected result:

* New tab is opened inside already opened terminal window.

### Creating new profile

Steps to test:

1. Open MATE Terminal
1. Select *File* → *New Profile*
1. Specify the name of new profile in *Profile name*
1. Click *Create*
1. In the opened window change some settings and click *Close*

Expected result:

* MATE Terminal created new profile, its settings were saved.

### Closing terminal tab

Steps to test:

1. Open MATE Terminal
1. Select *File* → *Open Tab* (or `<Shift>+<Ctrl>+<T>`)
1. Select *File* → *Close Tab* (or `<Shift>+<Ctrl>+<W>`)

Expected result:

* MATE Terminal opens new tab  and closes it.

### Closing terminal window

Steps to test:

1. Open MATE Terminal
1. Select *File* → *Close Window* (or `<Shift>+<Ctrl>+<Q>`)

Expected result:

* MATE Terminal is opened that closed.

## Edit

### Copy, Paste

Steps to test:

1. Open MATE Terminal
1. Select some text with mouse
1. Select *Edit* → *Copy* (or `<Shift>+<Ctrl>+<C>`) to copy the text
1. Select *Edit* → *Paste* (or `<Shift>+<Ctrl>+<V>`) to paste the text

Expected results:

* text is copied from terminal and pasted to it upon user request.

### Select All

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Select All* (or `<Shift>+<Ctrl>+<A>`)

Expected results:

* all text is the terminal was selected.

### Profiles

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Profiles*

Expected results:

* the Profiles window is opened

#### Create new profile

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Profiles*
1. In the opened Profiles window click *New*
1. Specify *Profile name*
1. Click *Create*
1. In the opened window change some settings and click *Close*

Expected results:

* Profiles window was opened, new profile is created

#### Edit profile

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Profiles*
1. In the opened Profiles window select profile
1. Click *Edit*
1. In the opened window change some settings and click *Close*

Expected results:

* Profiles window was opened, existing profile was edited

#### Delete existing profile

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Profiles*
1. In the opened Profiles window select profile
1. Click *Delete*
1. Confirm profile deletion by click on *Delete*

Expected results:

* Profiles window was opened, existing profile was deleted

#### Setting default profile

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Profiles*
1. In the opened Profiles window select set *Profile used when launching new terminal* to the needed profile name
1. Click *Close* and close MATE Terminal
1. Open MATE Terminal again and ensure that it was opened with the specified profile

Expected results:

* Default profile was set, the new terminal was opened with specified profile applied

### Keyboard Shortcuts

#### Enable or disable menu access keys (mnemonics)

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Keyboard Shortcuts* and uncheck the *Enable menu access kets (such as Alt+F to open File menu* checkbox, click *Close*
1. Press `<Alt>+<F>`
1. Select *Edit* → *Keyboard Shortcuts* and check the *Enable menu access kets (such as Alt+F to open File menu* checkbox, click *Close*
1. Press `<Alt>+<F>`

Expected results:

* Menu access keys behavior changes according to the state of  *Enable menu access kets (such as Alt+F to open File menu* checkbox

#### Enable or disable menu shortcut key (F10)

To execute this test one needs to install Midnight Commander. On Ubuntu it is done by `sudo apt-get install mc`.

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Keyboard Shortcuts* and uncheck *Enable the menu shortcut key (F10 by default)*, click *Close*
1. Open Midnight Commander with `mc` and press `<F10>` to exit from it
1. Select *Edit* → *Keyboard Shortcuts* and check *Enable the menu shortcut key (F10 by default)*, click *Close*
1. Open Midnight Commander with `mc` and press `<F10>` to exit from it

Expected results:

* user is able to exit from Midnight Commander by using `<F10>` key only if *Enable the menu shortcut key (F10 by default)* is unchecked
* user is able to open MATE Terminal menu by using `<F10>` key only if  *Enable the menu shortcut key (F10 by default)* is checked

#### Viewing, redefining and disabling shortcut keys

To execute this test one needs to install Midnight Commander. On Ubuntu it is done by `sudo apt-get install mc`.

Steps to test:

1. Open MATE Terminal
1. Open Midnight Commander with `mc` and press `<F1>` to open its help
1. Select *Edit* → *Keyboard Shortcuts*, locate *Help* → *Contents* item, click on the `F1` value in the *Shortcut Key* column and press `<Backspace>` to disable this shortcut, click *Close*
1. Open Midnight Commander with `mc` and press `<F1>` to open its help

Expected results:

* user is able to open help of Midnight Commander only if *Help* → *Contents* shortcut is disabled.

### Profile Preferences

#### General

##### Setting font and its width

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Profile Preferences*, navigate to *General* tab
1. Uncheck *Use the system fixed width font* checkbox
1. Check *Use the system fixed width font* checkbox

Expected results:

* The font inside terminal changes according to the state of *Use the system fixed width font* checkbox

##### Setting bold font

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Profile Preferences*, navigate to *General* tab
1. Check *Allow bold text* checkbox
1. Uncheck *Allow bold text* checkbox

Expected results:

* The font inside terminal changes from normal to bold according to the state of *Allow bold text* checkbox

##### Setting menubar in new terminals

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Profile Preferences*, navigate to *General* tab
1. Uncheck *Show menubar by default in new terminals*, click *Close*
1. Open new MATE Terminal
1. Select *Edit* → *Profile Preferences*, navigate to *General* tab and check  *Show menubar by default in new terminals*, click *Close*
1. Open new MATE Terminal

Expected results:

* The menubar visibility is changed according to the state of *Show menubar by default in new terminals* checkbox

##### Setting terminal bell

Steps to test:

1. Unmute speakers
1. Open MATE Terminal
1. Select *Edit* → *Profile Preferences*, navigate to *General* tab, uncheck *Terminal bell* checkbox
1. Set focus to the MATE Terminal window and press down button on the keyboard (`<↓>`)
1. Select *Edit* → *Profile Preferences*, navigate to *General* tab, check *Terminal bell* checkbox
1. Set focus to the MATE Terminal window and press down button on the keyboard (`<↓>`)

Expected results:

* The terminal produces sound after `<↓>` key is pressed only if *Terminal bell* checkbox is checked

##### Setting option to copy selected text into clipboard

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Profile Preferences*, navigate to *General* tab, check *Copy selected text into keyboard* checkbox
1. Execute some command in the terminal, select some words from its output by mouse
1. Paste the text from clipboard to some other application
1. In the MATE Terminal select *Edit* → *Profile Preferences*, navigate to *General* tab, check *Copy selected text into keyboard* checkbox

Expected results:

* If *Copy selected text into keyboard* checkbox is checked, then selection of the text in the terminal get it copied to the clipboard

##### Setting highlight of the URLs

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Profile Preferences*, navigate to *General* tab, uncheck *Highlight URLs under mouse pointer* checkbox
1. Run `sudo apt-get update` in the terminal, move mouse cursor over any URL and ensure that it is not highlighted
1. Select *Edit* → *Profile Preferences*, navigate to *General* tab, check *Highlight URLs under mouse pointer* checkbox back, click *Close*
1. Move mouse cursor over any URL and ensure that it is highlighted

Expected results:

* URLs in the MATE Terminal are highlighted only if  *Highlight URLs under mouse pointer*  checkbox is checked

##### Setting properties of the cursor

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Profile Preferences*, navigate to *General* tab
1. Change value of *Cursor blink* and view changes is active terminal window
1. Change value of *Cursor shape* and view changes is active terminal window
1. Click *Close*

Expected results:

* The properties of cursor get changed according to the values in  *Cursor blink* and  *Cursor shape*

##### Setting default terminal size

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Profile Preferences*, navigate to *General* tab
1. Check the *Use custom default terminal size*
1. Set *Default size* to custom value (for example – `100` columns and `50` rows)
1. Open new instance of MATE Terminal

Expected results:

* The default size of new terminal was changed according to values in *Default size* fields

#### Title and Command

== TBW ==

#### Colors

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Profile Preferences*, navigate to *Colors* tab
1. Uncheck *Use colors from system theme* and check it back
1. Change *Built-in schemes* from *Tango* some other, then change back to *Tango*

Expected results:

* The colors of terminal are changed according to the settings on the *Colors* tab

#### Background

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Profile Preferences*, navigate to *Background* tab
1. Switch the radio button from *Solid color* to *Background image* and then to *Transparent background*
1. Switch the radio button back to *Solid color*

Expected results:

* The terminal background changes according to the position of radio button on *Background* tab

#### Scrolling

##### Changing scrollbar position

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Profile Preferences*, navigate to *Scrolling* tab
1. Set *Scrollbar is* to *On the left side*, then to *On the right side*, then to *Disabled*
1. Set *Scrollbar is* back to *On the left side*

Expected results:

* The position of the scrollbar changes depending on the item selected from *Scrollbar is*, the terminal contents are scrollable by using mouse wheel for any value of  *Scrollbar is*

##### Changing scrollback depth

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Profile Preferences*, navigate to *Scrolling* tab
1. Set *Scrollback* to the `512`, click *Close*
1. View the contents of some lengthy file by using command like `cat /var/log/syslog`, scroll the output to the first line
1. Select *Edit* → *Profile Preferences*, navigate to *Scrolling* tab
1. Set *Scrollback* to *Unlimited*, click *Close*
1. View the contents of some lengthy file by using command like `cat /var/log/syslog`, scroll the output to the first line

Expected results:

* The depth of the terminal scrollback maybe changed, setting it to *Unlimited* allows user to view whole log-file

##### Setting scroll on output option

Select this option to enable you to scroll the output on the terminal while the terminal continues to display more output from a command.

== TBW ==

##### Setting scroll on keystroke option

Select this option to enable you to press any key on the keyboard to scroll down the terminal window to the command prompt. This action only applies if you scrolled up the terminal window and you want to return to the command prompt.

== TBW ==

#### Compatibility

Steps to test:

1. Open MATE Terminal
1. Select *Edit* → *Profile Preferences*, navigate to *Compatibility* tab
1. Select some non-default value from the pull-down menu *Backspace key generates*
1. Select some non-default value from the pull-down menu *Delete key generates*
1. Click on *Reset Compatibility Options to Defaults*

Expected results:

* User is able to change the compatibility options, click on the *Reset Compatibility Options to Defaults* sets  *Backspace key generates*  to *ASCII DEL* and *Delete key generates* to *Escape sequence*

## View

### Show Menubar

Steps to test:

1. Open MATE Terminal
1. Uncheck *VIew* → *Show Menubar*
1. Do right mouse click in the terminal are and select *Show Menubar* from drop-down menu

Expected results:

* The visibility of Menubar is changed accordingly to the state *Show Menubar*  of menu items

### Full Screen

Steps to test:

1. Open MATE Terminal
1. Select *View* → *Full Screen* (or press `<F11>`)
1. Press `<F11>` again to exit from full screen mode

Expected results:

* User is able to set MATE Terminal window to full screen window, the `<F11>` key changes the size of window

### Zoom In

Steps to test:

1. Open MATE Terminal
1. Select *View* → *Zoom In* (or press `<Ctrl>+<Shift>+<+>`)

Expected results:

* The size of terminal window and font inside it become larger on each *Zoom In* operation

### Zoom Out

Steps to test:

1. Open MATE Terminal
1. Select *View* → *Zoom On* (or press `<Ctrl>+<->`)

Expected results:

* The size of terminal window and font inside it become smaller on each *Zoom Out* operation

### Normal Size

Steps to test:

1. Open MATE Terminal
1. Select *View* → *Normal Size* (or press `<Ctrl>+<0>`)

Expected results:

* The size of terminal window and font inside it become normal/default after clicking on *Normal Size*

## Search

### Find, Find Next, Find Previous

Steps to test:

1. Open MATE Terminal
1. Execute `sudo apt-get update`
1. Select *Search* → *Find* (or press `<Shift>+<Ctrl>+<F>`)
1. Fill the *Search for* field with string `http`, check *Search backwards* and *Wrap around*  checkboxes, click *Find*
1. Select *Search* → *Find Next* (or press `<Shift>+<Ctrl>+<H>`)
1. Select *Search* → *Find Previous* (or press `<Shift>+<Ctrl>+<G>`)

Expected results:

* User is able to search some text in the terminal output

## Terminal

### Change Profile

Steps to test:

1. Open MATE Terminal
1. Select *Terminal* → *Change Profile*
1. Choose one of the available profiles by mouse or by using `<Alt>+<Page Up>` / `<Alt>+<Page Down>`

Expected results:

* User is able to change profile of the MATE Terminal

### Set Title

Steps to test:

1. Open MATE Terminal
1. Select *Terminal* → *Set Title*
1. Fill the *Title* field with new terminal name

Expected results

* User is able to set new name for the terminal, it is shown on the top of window border

### Set Character Encoding

Before proceeding one need to obtain some text file in non-UTF-8 encoding.

Steps to test:

1. Open MATE Terminal
1. Select *View* → *Set Character Encoding*, then click on *Add/Remove* to add one or more available encodings (for example, `WINDOWS-1251`)
1. Switch terminal encoding to the just added by selecting *View* → *Set Character Encoding* and clicking on the needed encoding
1. View the encoded file with `cat`
1. Switch terminal encoding back to the UTF-8 by selecting *View* → *Set Character Encoding* and clicking on  *Unicode (UTF-8)*

Expected results:

* the contents of the file in the non-UTF-8 encoding is shown normally when the correct encoding was selected

### Reset

Steps to test:

1. Open MATE Terminal
1. Inverse colors of the terminal by running `setterm --inversescreen on`
1. Select *Terminal* → *Reset*

Expected results:

* Inverse colors was canceled only after resetting the terminal

### Reset and Clear

Steps to test:

1. Open MATE Terminal
1. Inverse colors of the terminal by running `setterm --inversescreen on`
1. View contents of some file by running `cat /etc/os-release`
1. Select *Terminal* → *Reset and Clear*

Expected results:

* After selecting *Reset and Clear* the terminal has normal/default colors and reseted scroll-back history

### Using predefined sizes

Steps to test:

1. Open MATE Terminal
1. Select *View* and one of the predefined sizes (for example *80x43* or others)

Expected results:

* Terminal size is changed to the user-defined size

## Right mouse click menu in terminal area

This drop-down menu allows to:

* to *Open Terminal*;
* to *Open Tab*;
* to *Close Window*;
* to *Copy*;
* to *Paste*;
* to apply profile (select from *Profiles* submenu);
* to toggle menubar (by checking *Show Menubar*).

All test for them are already defined for them.
