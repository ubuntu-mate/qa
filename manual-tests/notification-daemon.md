# MATE Notification Daemon

The MATE Notification Daemon is used to serve and display desktop notifications.

User can choose the style of desktop notifications by launching `mate-notification-properties`.

## Set theme and placement

Steps to test:

1. Run `mate-notification-properties` from terminal or from `<Alt>+<F2>` menu
1. Set *Theme* to one of the following values - *Nodoka*, *Standard theme*, *Slider*, *Coco*
1. Set *Position* to one of the following values - *Top Left*, *Top Right*, *Bottom Left*, *Bottom Right*
1. Uncheck *Enable Do Not Disturb*
1. Click *Preview*
1. Repeat steps above for different *Theme* and *Position*
1. Click *Close* button

Expected results:

* notification baloons looks good and appears in the user-specified locations.

## Set active monitor

Steps to test:

1. Run `mate-notification-properties` from terminal or from `<Alt>+<F2>` menu
1. Uncheck *Use Active Monitor*
1. Select needed *Monitor* and click *Preview*
1. Click *Close*

Expected results:

* notification is shown on user-specified monitor.

## Test "Do Not Disturb" mode (since Ubuntu 19.10)

Steps to test:

1. Run `mate-notification-properties` from terminal or from `<Alt>+<F2>` menu
1. Check *Enable Do Not Disturb*
1. Click *Preview*
1. Click *Close*

Expected results:

* notifications are not shown when *Enable Do Not Disturb* is checked.
