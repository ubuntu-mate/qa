# Main Menu

Main Menu editor for MATE DE is preinstalled. It may be called from terminal as `mozo`.

## Show and hide item

Steps to test:

1. Open Main Menu
1. Navigate to *Accesories* menu and check the *Show* checkbox near *About MATE* (or any other unchecked item)
1. Open Applications menu with `<Alt>+<F1>`, navigate to the category with just-enabled item and ensure that it is now shown
1. Uncheck this menu item again in the *Main Menu* Application

Expected results:

* user is able to control visibility of the needed item.

## Add New Menu

Steps to test:

1. Open Main Menu
1. Navigate to *Applications* main menu
1. Click *New Menu*, specify its name (for example *MyMenu*)
1. Check the *Show* checkmark to make just-created menu visible

Expected result:

* user is able to create new menu.

## Add New Item

Steps to test:

1. Open Main Menu
1. Click on the just-created user-defined menu named *MyMenu*
1. Click *New Item*
1. Fill the fields of *Create Launcher* window with information about existing applicaiton - for example *Type* : *Application*, *Name:* `MATE Calculator`, *Command*: `mate-calc`) and click *OK*
1. Open Applications menu with `<Alt>+<F1>`, locate the just-created menu with single launcher, run the application

Expected results:

* user is able to add new item to the previously created menu and to launch the application from this new item.

## Add New Separator

Steps to test:

1. Open Main Menu
1. Place cursor on any menu item, click *New Separator*
1. Open Applications menu with `<Alt>+<F1>`, locate the just-created separator here

Expected results:

* user is able to create and locate menu separator.

## Delete element

Steps to test:

1. Open Main Menu
1. Place cursor on user-created item, menu or separator
1. Open Applications menu with `<Alt>+<F1>`, ensure that item, menu or separator was really deleted
1. Click *Delete*

Expected results:

* user is able to locate and delete item, menu or separator.
