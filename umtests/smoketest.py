# Ubuntu MATE Whole-Desktop smoketest
# Needs to check at least one function of every component used by Ubuntu MATE
# The list for those components is in the README.md of the root directory

# Coverage:

targets = ['ubuntu-mate-welcome', 'software-boutique', 'mate-tweak',
           'mate-menu', 'mate-hud', 'atril', 'caja', 'engrampa', 'eom',
           'marco', 'mate-applets', 'mate-calc', 'mate-control-center',
           'mate-indicator-applet', 'mate-menus', 'mate-netbook',
           'mate-notification-daemon', 'mate-panel', 'mate-polkit',
           'mate-power-manager', 'mate-screensaver', 'mate-sensors-applet',
           'mate-session-manager', 'mate-settings-daemon',
           'mate-system-monitor', 'mate-terminal', 'mate-user-guide',
           'mate-user-share', 'mate-utils', 'pluma', 'robint99/mate-dock-applet',
           'IKRadulov/mate-window-applets', 'solus-project/brisk-menu']

steps = [

    {
        'action': 'Login',
        'expected': 'MATE Desktop loads normally, Welcome opens up',
        'components': ['mate-session-manager', 'mate-settings-daemon', 'caja', 'ubuntu-mate-welcome', 'mate-panel']
    },
    {
        'action': 'Connect to a network',
        'expected': 'Connection established',
        'components': ['ubuntu']
    },
    {
        'action': 'Right click Desktop, select change background.',
        'expected': 'Appearance Preferences window opens up with the background tab selected',
        'components': ['caja', 'marco', 'mate-control-center']
    },
    {
        'action': 'Select another wallpaper for background',
        'expected': 'The change is reflected on the desktop',
        'components': ['caja', 'mate-control-center']
    },
    {
        'action': 'Logout, then log back in.',
        'expected': 'After login, the new wallpaper is active',
        'components': ['mate-settings-daemon']
    },
    {
        'action': 'In welcome, click "Software"',
        'expected': 'The Software Boutique opens up',
        'components': ['ubuntu-mate-welcome', 'software-boutique']
    },
    {
        'action': 'In Boutique, install Accessories -> Redshift',
        'expected': 'Application installs successfully',
        'components': ['software-boutique', 'ubuntu']
    },
    {
        'action': 'From Welcome -> Getting Started -> Customization open MATE Tweak (button is named "User Interface")',
        'expected': 'MATE Tweak Opens',
        'components': ['ubuntu-mate-welcome', 'mate-tweak']
    },
    {
        'action': 'In MATE Tweak, change layout to Pantheon',
        'expected': 'Pantheon layout loads successfully',
        'components': ['mate-tweak', 'mate-panel', 'solus-project/brisk-menu']
    },
    {
        'action': 'Hit the "Windows" key.',
        'expected': 'Brisk menu pops up.',
        'components': ['solus-project/brisk-menu']
    },
    {
        'action': 'Click the power button in the top right corner',
        'expected': 'A menu comes up listing "About this computer", "System Settings", etc...',
        'components': ['mate-indicator-applet']
    },
    {
        'action': 'In MATE Tweak, switch panels back to redmond',
        'expected': 'Redmond layout loads successfully',
        'components': ['mate-tweak', 'mate-panel']
    },
    {
        'action': 'Hit the "Windows" key',
        'expected': 'MATE Menu comes up from the bottom left',
        'components': ['mate-menu']
    },
    {
        'action': 'In MATE Tweak, switch layout to mutiny.',
        'expected': 'Mutiny layout loads sucessfully',
        'components': ['mate-tweak', 'robint99/mate-dock-applet']
    },
    {
        'action': 'Open Firefox, then Hit the ALT key.',
        'expected': 'HUD comes up',
        'components': ['mate-hud']
    },
    {
        'action': 'In MATE Tweak, switch layout to Traditional',
        'expected': 'Default layout is restored',
        'components': ['mate-teak', 'mate-panel']
    },
    {
        'action': 'Right click top panel, and select "Add to panel"',
        'expected': '"Add to panel" window opens',
        'components': ['mate-panel']
    },
    {
        'action': 'Add a System Monitor applet',
        'expected': 'The applet is added and starts monitoring the CPU',
        'components': ['mate-panel', 'mate-applets']
    },
    {
        'action': 'Hit CTRL+ALT+T',
        'expected': 'An instance of mate-terminal opens.',
        'components': ['mate-settings-daemon', 'mate-terminal']
    },
    {
        'action': 'Go to Appliations -> System Tools and select "System Monitor"',
        'expected': 'System Monitor window opens',
        'components': ['mate-menus', 'mate-system-monitor']
    },
    {
        'action': 'Right click the top panel and add a Window Picker Applet',
        'expected': 'The applet is added, showing icons for each open window',
        'components': ['mate-netbook']
    },
    {
        'action': 'Hit CTRL+ALT+L',
        'expected': 'Screen is blanked and locked.',
        'components': ['mate-screensaver']
    },
    {
        'action': 'Login',
        'expected': 'Password accepted, desktop is visible again',
        'components': ['mate-screensaver']
    },
    {
        'action': 'Go to System -> Preferences -> Hardware -> Power Management',
        'expected': 'The Power Management Preferences window opens',
        'components': ['mate-power-manager']
    },
    {
        'action': 'In the power management window move the slider to set display brightness',
        'expected': 'The screen brigthness change',
        'components': ['mate-power-manager']
    },
    {
        'action': 'In the terminal: eom /usr/share/backgrounds/ubuntu-mate-common/',
        'expected': 'Eye Of MATE opens and you can see the background',
        'components': ['eom', 'mate-terminal']
    },
    {
        'action': 'In the terminal: atril /usr/share/cups/data/form_russian.pdf',
        'expected': 'A pdf document opens in Atril',
        'components': ['atril', 'mate-terminal']
    },
    {
        'action': 'In the terminal: engrampa /usr/lib/libreoffice/share/config/images_tango.zip',
        'expected': 'The archive manager opens up, allowing you to browse inside the archive',
        'components': ['engrampa']
    },
    {
        'action': 'In the terminal: pluma /usr/share/doc/xorg/index.txt',
        'expected': 'The text editor comes up',
        'components': ['pluma']
    },
    {
        'action': 'System -> Preferences -> Look & Feel -> Pop Up Notifications',
        'expected': 'The Notification settings window opens',
        'components': ['mate-notification-daemon']
    },
    {
        'action': 'In terminal: mate-calc',
        'expected': 'Calculator comes up',
        'components': ['mate-calc']
    },
    {
        'action': 'In Applications -> Accessories select "Ubuntu MATE guide',
        'expected': 'The Ubuntu MATE Help window comes up',
        'components': ['mate-user-guide']
    },
    {
        'action': 'In Applications -> System Tools select "MATE Disk Usage Analyzer"',
        'expected': 'Disk Usage Analyzer window comes up',
        'components': ['mate-utils']
    },
    {
        'action': 'Right click the top panel -> Add to panel -> Hardware Sensors Monitor',
        'expected': 'The applet is added and lists temperatures',
        'components': ['mate-sensors-applet']
    },
    {
        'action': '',
        'expected': '',
        'components': ['']
    }
]


if __name__ == '__main__':

    print "Passed SyntaxCheck"

    components = set()
    for s in steps:
        for c in s['components']:
            components.add(c)

    print "Smoketest Coverage: "

    for c in components:
        print c

    print "Not covered:"
    targets_set = set(targets)
    for c in components:
        if c in targets_set:
            targets_set.remove(c)

    print targets_set
