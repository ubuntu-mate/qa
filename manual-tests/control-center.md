# MATE Control Center

MATE Control Center is preinstalled in MATE DE. It has many control center applets to set various aspects of the desktop.

Its main executable is named `mate-control-center`.

By default MATE Control Center have the following categories of the settings with the following elements:

* **Administration**

    - *Login Window* from `lightdm-settings` (not a part of MATE);
    - *Printers* from `system-config-printer` (not a part of MATE);
    - *Software & Updates* from `software-properties-gtk` (not a part of MATE);
    + *Software Boutique* from `ubuntu-mate-welcome.software-boutique`;
    - *Software Updater* from `update-manager` (not a part of MATE);
    - *Users and Groups* from `users-admin` (not a part of MATE);
    + *Welcome* from `ubuntu-mate-welcome`.

* **Hardware**

    - *Additional Drivers* from `software-properties-gtk` (not a part of MATE);
    - *Bluetooth Adapters* from `blueman-adapters` (not a part of MATE);
    - *Bluetooth Manager* from `blueman` (not a part of MATE);
    - *Disks* from `gnome-disks` (not a part of MATE);
    + *Displays* from `mate-display-properties`;
    + *Keyboard* from `mate-keyboard-properties` with `mate-typing-monitor`;
    + *Keyboard Shortcuts* from `mate-keybinding-properties`;
    + *Mouse* from `mate-mouse-properties`;
    + *Power Management* from `mate-power-preferences` (see [power-manager.md](power-manager.md));
    + *Sound* from `mate-volume-control`;
    + *Time And Date manager* from `mate-time-admin`;

* **Internet and Network**

    - *Advanced Network Configuration* from `nm-connection-editor` (not a part of MATE);
    - *Firewall Configuration* from `gufw-pkexec` (not a part of MATE);
    + *Network Proxy* from `mate-network-properties`;

* **Look and Feel**

    + *Appearance* from `mate-appearance-properties`;
    + *Main Menu* from `mozo` (see [mozo.md](mozo.md));
    + *MATE Tweak* from `mate-tweak` (see [tweak.md](tweak.md));
    + *Popup Notifications* from `mate-notification-properties` (see [notification-daemon.md](notification-daemon.md));
    + *Screensaver* from `mate-screensaver-preferences` (see [screensaver.md](screensaver.md));
    + *Windows* from `mate-window-properties`;

* **Personal**

    + *About Me* from `about-me` (see [about-me.md](about-me.md));
    + *Assistive Technologies* from `mate-at-properties`;
    + *File Management* from `caja-file-management-properties` (see [caja.md](caja.md));
    - *Language Support* from `gnome-language-selector` (not a part of MATE);
    - *Onboard Settings* from `onboard-settings` (not a part of MATE);
    + *Preferred Applications* from `mate-default-applications-properties`;
    + *Startup Applications* from `mate-session-properties` (see [session.md](session.md)).

This test-suite covers only MATE components.

## Control Center itself

Steps to test:

1. Open MATE Control Center
1. Click on every control center element, wait its window to appear and then close its window
1. Close MATE Control Center

Expected results:

* MATE Control Center opens, user is able to run every control center element.

## Hardware: Display

`mate-display-properties`

TODO

## Hardware: Keyboard

`mate-keyboard-properties`

TODO

## Hardware: Keyboard Shortcuts

`mate-keybinding-properties`

TODO

## Hardware: Mouse

`mate-mouse-properties`

TODO

## Hardware: Sound

`mate-volume-control`

TODO

## Hardware: Time And Date manager

`mate-time-admin`

TODO

## Internet and Network: Network Proxy

`mate-network-properties`

TODO

## Look and Feel: Appearance

The Appearance Preferences may be called from terminal by using `mate-appearance-properties` command.

### Setting Theme

#### Selecting existing theme

Steps to test:

1. Open Appearance Preferences
1. Select needed theme on the *Theme* tab by single clicking on its name
1. Close Appearance Preferences

Expected results:

* theme is selected and applied.

#### Customizing existing theme

Steps to test:

1. Open Appearance Preferences
1. Click *Customize*
1. In the opened window named *Customize Theme*:

    * Select controls style from *Controls* tab
    * Switch to *Window Border* tab and select its new style
    * Switch to *Icons* tab and change select their new style
    * Switch to *Pointer* tab and change select its new style
1. Close window named *Customize Theme*
1. Revert theme to the favorite one
1. Close Appearance Preferences

Expected results:

* user is able to customize theme parameters including *Controls*, *Window Border*, *Icons* and *Pointer*.

#### Installing new theme

Steps to test:

1. Open Appearance Preferences
1. Obtain new theme by clicking on the *Get more themes online* and download theme using web-browser
1. Switch to Appearance Preferences window, click *Install* and select downloaded theme
1. Choose installed theme
1. Close Appearance Preferences

Expected results:

* user is able to install downloaded theme and to select it.

### Setting Background

#### Using preinstalled images

Steps to test:

1. Open Appearance Preferences
1. Minimize all other windows
1. Switch to *Background* tab
1. Select needed background image from the list
1. Optionally set its *Style* and *Colors*
1. Close Appearance Preferences

Expected results:

* user is able to set background image and its parameters.

#### Using user-defined image

Steps to test:

1. Open Appearance Preferences
1. Minimize all other windows
1. Switch to *Background* tab
1. Click *Add* and select needed background image file
1. Optionally set its *Style* and *Colors*
1. Close Appearance Preferences

Expected results:

* user is able to set own background image and its parameters.

### Setting Fonts

#### General settings

Steps to test:

1. Open Appearance Preferences
1. Switch to *Fonts* tab
1. Set needed font names and sizes
1. Specify font rendering in *Rendering* section
1. Close Appearance Preferences

Expected results:

* font settings were changed on user preferences.

#### Adding new font

Steps to test:

1. Download new font file from somewhere
1. Open Appearance Preferences
1. Switch to *Fonts* tab
1. Click on *Add new font*, select font file and click *Open*
1. Select this new installed font for font types
1. Close Appearance Preferences

Expected results:

* user is able to select font and use it in the interface.

#### Details

Steps to test:

1. Open Appearance Preferences
1. Switch to *Fonts* tab
1. Click *Details*
1. Set *Resolution* - switch *Automatic detection* to `0`, and then set needed *Dots per inch (DPI)* value
1. Change *Smoothing*, *Hinting* and *Subpixel Order* settings
1. Close Appearance Preferences

Expected results:

* user is able to change settings of *DPI*, *Smoothing*, *Hinting* and *Subpixel Order*.

### Setting Interface

#### Menus and Toolbars

Steps to test:

1. Open Appearance Preferences
1. Switch to *Interface* tab
1. In the *Menus and Toolbars* uncheck the *Show icons in menus*
1. Check the *Preview* below
1. In the *Menus and Toolbars* check the *Show icons in menus* again
1. Check the *Preview* below
1. Close Appearance Preferences

Expected results:

* user is able to change the appearance of icons in the menus.

#### Buttons

Steps to test:

1. Open Appearance Preferences
1. Switch to *Interface* tab
1. In the *Buttons* uncheck the *Show icons on buttons*
1. Check the *Preview* below or buttons of the window
1. In the *Buttons* check the *Show icons on buttons* again
1. Check the *Preview* below or buttons of the window
1. Close Appearance Preferences

Expected results:

* user is able to change the appearance of icons on the buttons.

## Look and Feel: Main Menu

from `mozo` (see [mozo.md](mozo.md));

## Look and Feel: MATE Tweak

from `mate-tweak` (see [tweak.md](tweak.md)).

## Look and Feel: Popup Notifications

from `mate-notification-properties` (see [notification-daemon.md](notification-daemon.md)).

## Look and Feel: Screensaver

from `mate-screensaver-preferences` (see [screensaver.md](screensaver.md)])

## Look and Feel: Windows

`mate-window-properties`

TODO

## Personal: About Me

from `about-me` (see [about-me.md](about-me.md))

## Personal: Assistive Technologies

The Assistive Technologies may be called from terminal by using `mate-at-properties`.

### Setting Preferred Applications

Steps to test:

1. Open Assistive Technologies
1. In the *Assistive Technologies* area click on *Preferred Applications* button

Expected results:

* the Preferred Applications window (from `mate-default-applications-properties` executable) is opened on Accessibility tab, user is able to choose *Visual* and *Mobility* tools from the corresponding lists.

### Enabling assistive technologies

Steps to test:

1. Open Assistive Technologies
1. In the *Assistive Technologies* area check the *Enable assistive technologies* checkmark
1. Click *Close and Log Out* button

Expected results:

* Assistive Technologies are applied on next login.

Do not forget to disable Assistive Technologies after testing.

### Setting Keyboard Accessibility

Steps to test:

1. Open Assistive Technologies
1. In the *Preferences* area click *Keyboard Accessibility* button

Expected results:

* the Keyboard Preferences window (from `mate-keyboard-properties` executable) is opened on Accessibility tab, user is able to change keyboard accessibility settings from here.

### Setting Mouse Accessibility

Steps to test:

1. Open Assistive Technologies
1. In the *Preferences* area click *Mouse Accessibility* button

Expected results:

* the Mouse Preferences window (from `mate-mouse-properties`) is opened, user is able to set mouse properties from here.

## Personal: File Management

The File Management (`caja-file-management-properties`) is covered in [caja.md](caja.md).

## Personal: Preferred Applications

The Preferred Applications may be called from terminal by using `mate-default-applications-properties` command. It allows one to set default applications for Internet, Multimedia, System, Office and Accessibility.

### Setting Preferred Applications for Internet

Before proceeding one have to install at least two web browser and two mail reader applications.

#### Selecting default Web Browser

Steps to test:

1. Open Preferred Applications
1. Navigate to the Internet tab
1. Remember the name of current Web Browser
1. Press `<Alt>+<F2>` and open website by running `mate-open https://ubuntu-mate.org` command, remember the name of Web Browser opened
1. In the Preferred Applications window select other Web Browser and run `mate-open https://ubuntu-mate.org` command again, remember the name of Web Browser opened

Expected results:

* the web site was opened in two different web browsers - first (usually Firefox) and second (depends on user decision).

#### Selecting default Mail Reader

Steps to test:

1. Open Preferred Applications
1. Navigate to the Internet tab
1. Remember the name of current Mail Reader
1. Press `<Alt>+<F2>` and open mail reader by running `mate-open mailto:some@body.org` command, remember the name of Mail Reader opened
1. In the Preferred Applications window select other Mail Reader and run `mate-open mailto:some@body.org` command again, remember the name of Mail Reader opened

Expected results:

* the e-mail/account creation wizard was opened in two different mail readers - first (usually Thunderbird or Evolution) and second (depends on user decision).

### Setting Preferred Applications for Multimedia

Before proceeding one have to install at least two image viewer, multimedia and video player applications.

#### Selecting default Image Viewer

Steps to test:

1. Open Preferred Applications
1. Navigate to the Multimedia tab
1. Remember the name of current Image Viewer
1. Press `<Alt+F2>` and open image viewer by running `mate-open /usr/share/app-install/icons/mate.png` command, remember the name of Image Viewer opened
1. In the Preferred Applications window select other Image Viewer and run `mate-open /usr/share/app-install/icons/mate.png` command again, remember the name of Image Viewer opened

Expected results:

* the image was opened in two different image viewers - first (usually Eye of MATE) and second (depends on user decision).

#### Selecting default Multimedia Player

Steps to test:

1. Open Preferred Applications
1. Navigate to the Multimedia tab
1. Remember the name of current Multimedia Player
1. Press `<Alt+F2>` and open multimedia player by running `mate-open /usr/share/sounds/mate/default/alerts/glass.ogg` command, remember the name of Multimedia Player opened
1. In the Preferred Applications window select other Multimedia Player and run `mate-open /usr/share/sounds/mate/default/alerts/glass.ogg` command again, remember the name of Multimedia Player opened

Expected results:

* the audio file was opened in two different multimedia players.

#### Selecting default Video Player

Steps to test:

1. Open Preferred Applications
1. Navigate to the Multimedia tab
1. Remember the name of current Video Player
1. Open Caja, navigate to the folder with video files, open video file, remember the name of Video Player opened
1. In the Preferred Applications window select other Video player and open video file using Caja again remembering the name of Video Player opened

Expected results:

* the video file was opened in two different video players.

### Setting Preferred Applications for System

Before proceeding one have to install at least two text editor, terminal emulator and file manager applications.

#### Selecting default Text Editor

Steps to test:

1. Open Preferred Applications
1. Navigate to the System tab
1. Remember the name of current Text Editor
1. Press `<Alt>+<F2>` and open text file by running `mate-open /etc/issue` command, remember the name of Text Editor opened
1. In the Preferred Applications window select other Text Editor and run `mate-open /etc/issue` command again, remember the name of Text Editor opened

Expected results:

* the text file was opened in two different text editors - first (usually Pluma) and second (depends on user decision).

#### Selecting default Terminal Emulator

Steps to test:

1. Open Preferred Applications
1. Navigate to the System tab
1. Remember the name of current Terminal Emulator
1. Press `<Ctrl>+<Alt>+<T>` to open terminal emulator, remember its name
1. In the Preferred Applications window select other Terminal Emulator and press `<Ctrl>+<Alt>+<T>` again to open terminal and remember its name

Expected results:

* two terminal emulators were opened - first (usually MATE Terminal) and second (depends on user decision)

#### Selecting default File Manager

Steps to test:

1. Open Preferred Applications
1. Navigate to the System tab
1. Remember the name of current File Manager
1. Press `<Alt>+<F2>` and open file manager in home folder by running `mate-open ~` command, remember the name of opened file manager
1. In the Preferred Applications window select other File Manager and run `mate-open ~` command again, remember the name of opened file manager

Expected results:

* two file managers were opened - first (usually Caja) and second (depends on user decision)

### Setting Preferred Applications for Office

Before proceeding one have to install at least two document viewer, word processor and spreadsheet editor applications.

#### Selecting default Document Viewer

Steps to test:

1. Open Preferred Applications
1. Navigate to the Office tab
1. Remember the name of current Document Viewer
1. Press `<Alt>+<F2>` and open PDF-document by running `mate-open /usr/share/cups/data/default-testpage.pdf` command, remember the name of opened document viewer
1. In the Preferred Applications window select other Document Viewer and run `mate-open /usr/share/cups/data/default-testpage.pdf` command again, remember the name of opened document viewer

Expected results:

* two document viewers were opened - first (usually Atril) and second (depends on user decision)

#### Selecting default Word Processor

Steps to test:

1. Open Preferred Applications
1. Navigate to the Office tab
1. Remember the name of current Word Processor
1. Open Caja, navigate to the folder with document files, open file, remember the name of Word Processor opened
1. In the Preferred Applications window select other Word Processor and open document file using Caja again remembering the name of Word Processor opened

Expected results:

* the document file was opened in two different word processors - first (usually LibreOffice Writer) and second (depend on user decision).

#### Selecting default Spreadsheet Editor

Steps to test:

1. Open Preferred Applications
1. Navigate to the Office tab
1. Remember the name of current Spreadsheet Editor
1. Open Caja, navigate to the folder with spreadsheet files, open file, remember the name of Spreadsheet Editor opened
1. In the Preferred Applications window select other Spreadsheet Editor and open spreadsheet file using Caja again remembering the name of Spreadsheet Editor opened

Expected results:

* the document file was opened in two different spreadsheet processors - first (usually LibreOffice Calc) and second (depend on user decision).

### Setting Preferred Applications for Accessibility

Before proceeding one have to install at least two visual and mobility accessibility applications.

Steps to test:

1. Open Preferred Applications
1. Navigate to the Accessibility tab
1. Select needed Visual or Mobility tool
1. Check *Run at startup* checkmark
1. Logout and login back

Expected results:

* visual and mobility accessibility tools are started on next login.

## Personal: Startup Applications

The Startup Applications (`mate-session-properties`) is covered in [session.md](session.md).

