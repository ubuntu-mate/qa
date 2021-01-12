# Atril document viewer

Atril document is preinstalled on MATE DE. It may be called from terminal as `atril`.

## File

### Opening document

Steps to test:

1. Open Atril
1. Select *File* → *Open*
1. Open some file - for example `/usr/share/cups/data/default-testpage.pdf`

Expected result:

* Document is opened.

### Opening a copy document

Steps to test:

1. Open Atril
1. Select *File* → *Open*
1. Open some file - for example `/usr/share/cups/data/default-testpage.pdf`
1. Select *File* → *Open a copy*

Expected result:

* Atril opened two windows with the same document.

### Saving a copy

Steps to test:

1. Open Atril
1. Select *File* → *Open*
1. Open some file - for example `/usr/share/cups/data/default-testpage.pdf`
1. Select *File* → *Save as* (or *Save a copy* in older versions) and specify filepath for a copy

Expected result:

* Atril opened document and saved its copy.

### Sending document to other location

#### Sending file to removable drive

Steps to test:

1. Connect USB-flash to the system
1. Open Atril
1. Select *File* → *Open*
1. Open some file - for example `/usr/share/cups/data/default-testpage.pdf`
1. Select *File* → *Send To*
1. In the *Send To* window set *Send as* to *Removable disks and shares* and in *Send to* select location of USB-flash, click *Send*
1. Open USB-flash in the Caja and ensure that file was copied here

Expected result:

* Atril opened document and is able to send to it to USB-flash.

#### Sending file as e-mail attachment

Steps to test:

1. Open Atril
1. Select *File* → *Open*
1. Open some file - for example `/usr/share/cups/data/default-testpage.pdf`
1. Select *File* → *Send To*
1. In the *Send To* window set *Send as* to *Email* and fill *Send to* with correct e-mail address, click *Send*

Expected result:

* Atril opened document and is able to send it using *Send To* option using GNOME Evolution (e-mail account should be preconfigured).

### Printing the document

Steps to test:

1. Open Atril
1. Select *File* → *Open*
1. Open some file - for example `/usr/share/cups/data/default-testpage.pdf`
1. Select *File* → *Print*, specify printer and other settings, click *Print*

Expected result:

* Atril opened document, document is printed on selected printer.

### Viewing document properties

Steps to test:

1. Open Atril
1. Select *File* → *Open*
1. Open some file - for example `/usr/share/cups/data/default-testpage.pdf`
1. Select *File* → *Properties* (or click `<Alt>+<Return>`)

Expected result:

* Document Properties window is opened, user can see *General* and *Fonts* tabs.

### Using list of recent documents

Steps to test:

1. Open Atril
1. Select *File* → *Open*
1. Open some file - for example `/usr/share/cups/data/default-testpage.pdf`
1. Close Atril
1. Open Atril again
1. Select *File* and click on the first list element below *Properties* option (or use keyboard shortcut `<Alt>+<F>, <1>`)

Expected result:

* Atril shows list of recent documents, user is able to open them.

## Edit

### Document rotation

Steps to test:

1. Open Atril
1. Open some file - for example `/usr/share/cups/data/default-testpage.pdf`
1. Select *Edit*→*Rotate Left* or *Edit*→*Rotate Right* (`<Ctrl>+<Left>` / `<Ctrl>+<RIght>`)

Expected result:

* Document is rotated to the left or to the right.

### Toolbar

Steps to test:

1. Open Atril
1. Select *Edit*→*Toolbar*
1. Drag some icons from the *Toolbar Editor* window to the Toolbar
1. Drag some icons from the Toolbar back to *Toolbar Editor* window
1. Close *Toolbar Editor* window

Expected result:

* User is able to add and remove toolbar items

## View

### Showing and hiding Toolbar

Steps to test:

1. Open some document in Atril
1. Select *View* and check or uncheck *Toolbar* checkbox

Expected result:

* Toolbar visibility changes according to state of *View*→*Toolbar* checkbox.

### Side Pane

#### Showing and hiding Side Pane

Steps to test:

1. Open some document in Atril
1. Select *View* and check or uncheck *Side Pane* checkbox (or use `<F9>`)

Expected result:

* Side Pane visibility changes according to state *View*→*Side Pane* checkbox.

#### Selecting side pane mode

Steps to test:

1. Open some document in Atril
1. Enable *Side Pane* by clicking on *View*→*Side Pane*
1. Select any of modes from drop-down list - *Thumbnails*, *Index*, *Attachments*, *Layers*, *Annotations*, *Bookmarks*

Expected result:

* user is able to switch side pane modes, mode availability depends on document properties.

### Showing document on full-screen

Steps to test:

1. Open some document in Atril
1. Select *View* and check *Fullscreen* checkbox (or use `<F11>`)

Expected result:

* Document is shown in full-screen view until user presses `<Esc>`.

### Showing document as presentation

Steps to test:

1. Open some document in Atril
1. Select *View* and check *Presentation* checkbox (or use `<F5>`)

Expected result:

* Document is shown in presentation view until user presses `<Esc>`.

### Showing document in continous or one-page view

Steps to test:

1. Open some document in Atril
1. (a) Select *View* and check *Continous* checkbox, try to scroll document with mouse wheel
1. (b) Select *View* and uncheck *Continous* checkbox, try to scroll document with mouse wheel

Expected results:

* (a) Mouse wheel scrolls document by pages.
* (b) Mouse wheel scrolls one page of the document.

### Showing document in single or dual page view

Steps to test:

1. Open some document in Atril
1. (a) Select *View* and check *Dual* checkbox
1. (b) Select *View* and uncheck *Dual* checkbox

Expected results:

* (a) Atril shows two pages of document side-by-side.
* (b) Atril shows single page of document.

### Showing document with color inversion

Steps to test:

1. Open some document in Atril
1. (a) Select *View* and check *Inverted Colors* checkbox (or use `<Ctrl+I>`).
1. (b) Select *View* and uncheck *Inverted Colors* checkbox (or use `<Ctrl+I>`).

Expected results:

* (a) Atril shows document with inverted colors.
* (b) Atril shows document with normal colors.

## Bookmarks

### Adding Bookmarks

Steps to test:

1. Open some document in Atril
1. Click *Bookmarks*→*Add bookmark*
1. Click *Bookmarks* menu again and locate just created bookmark here
1. Open *Side Pane* and switch it to the *Bookmarks* mode and locate just created bookmark here

Expected results:

* Atril opened document, user is able to create bookmark, bookmark is shown in both *Bookmarks* menu and in *Side Pane*

### Navigating using Bookmarks

Steps to test:

1. Open some document with previously created bookmarks in Atril
1. Open *Side Pane* and switch it to the *Bookmarks* mode and click on previously created bookmark
1. Open *Bookmarks* menu and click on previously created bookmark

Expected results:

* user is able to use previously created bookmarks from *Bookmarks* menu and from *Side Pane*.

### Renaming Bookmarks

Steps to test:

1. Open some document with previously created bookmarks in Atril
1. Open *Side Pane* and switch it to the *Bookmarks* mode and locate previously created bookmark here
1. Do right mouse click on bookmark in the *Side Pane* and select *Rename Bookmark*

Expected results:

* user is able to rename previously created bookmarks from the *Side Pane*.

### Removing Bookmarks

Steps to test:

1. Open some document with previously created bookmarks in Atril
1. Open *Side Pane* and switch it to the *Bookmarks* mode and locate previously created bookmark here
1. Do right mouse click on bookmark in the *Side Pane* and select *Remove Bookmark*

Expected results:

* user is able to remove previously created bookmarks from the *Side Pane*.

---

## Special helper applications

Atril is shipped with two special helper applications:

* `atril-previewer` - to show print preview for a document
* `atril-thumbnailer` - to create  png thumbnails from atril supported documents

### Atril Previewer

Steps to test:

1. Open terminal and execute `atril-previewer` for some pdf-document - for example `atril-previewer /usr/share/doc/shared-mime-info/shared-mime-info-spec.pdf`
1. Check user controls in the opened *MATE Document Previwer* window
1. Close *MATE Document Previwer* window

Expected results:

* *MATE Document Previwer* window is opened with pdf-document for preview.

### Atril Thumbnailer

Steps to test:

1. Open terminal and execute `atril-thumbnailer` for some pdf-document and output thumbnail file - for example `atril-thumbnailer /usr/share/doc/shared-mime-info/shared-mime-info-spec.pdf /tmp/thumb.png`
1. Open created thumnail file with Eye of MATE with `eom /tmp/thumb.png`
1. Close Eye of MATE window

Expected results:

* Atril Thumbnailer created thumbnail for the pdf-file and user is able to view it in the  Eye of MATE image viewer.
