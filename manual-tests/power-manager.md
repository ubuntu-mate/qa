# Power Manager

MATE Power Manager is pre-installed on MATE DE.

## Power Management Preferences

Power Management Preferences allows user to set several preferences. Maybe called from terminal as `mate-power-preferences`.

### Changing settings On AC Power

Steps to test:

1. Launch Power Management Preferences
1. Set action to *put computer to sleep when inactive for* to *30 minutes*.
1. Set action to *put display to sleep when inactive for* to *10 minutes*.
1. Wait for specified amounts of time.

Expected results:

* Display was put to sleep in 10 minutes, the computer was put to sleep in 30 minutes.

### Changing settings On Battery Power

Steps to test:

1. Launch Power Management Preferences
1. Switch to *On Battery Power* tab
1. Set action to *put computer to sleep when inactive for* to *30 minutes*.
1. Set action to *put display to sleep when inactive for* to *10 minutes*.
1. For laptop check *Reduce backlight brightness*
1. For laptop check *Dim display when idle*
1. Wait for specified amounts of time.

Expected results:

* Display was put to sleep in 10 minutes, the computer was put to sleep in 30 minutes. Laptop screen uses reduced display brightness and dims when idle.

### Changing General settings

Steps to test:

1. Launch Power Management Preferences
1. Switch to *General* tab
1. Set action *when the power button is pressed* to *Ask me*
1. Set action *when the suspend button is pressed* to *Suspend*
1. Press power button

Expected results:

* System asks user for action when power button was pressed.

## Power Statistics

Power Statistics shows power statistics for AC adapter, battery and processor. Maybe called from terminal as `mate-power-statistics`.

### AC adapter

Steps to test:

1. Launch Power Statistics
1. Switch to the *AC adapter* vertical tab
1. Switch to the *Details* tab

Expected results:

* The *Details* tab shows actual information about AC adapter.

### Laptop battery

Steps to test:

1. Launch Power Statistics
1. Switch to the battery (second) vertical tab
1. Switch to the *Details* tab
1. Switch to the *History* tab
1. Switch to the *Statistics* tab

Expected results:

* The *Details* tab shows actual information about the battery; the *History* tab shows several plots as *Rate*, *Charge*, *Time to full*, *Time to empty* with battery data; the *Statistics* tab shows several statistical plots as *Charge profile*, *Charge accuracy*, *Discharge profile*, *Discharge accuracy*.

### Processor

Steps to test:

1. Launch Power Statistics
1. Switch to the *Processor* vertical tab
1. Watch for changes on the *Wakeups* tab

Expected results:

* The *Wakeups* tab shows processor wakeups per second in real time.
