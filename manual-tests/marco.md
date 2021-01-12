# Marco

Marco is preinstalled on MATE DE. It is the MATE Window Manager.

## Using `marco` command

### Replace the currently running window manager with Marco

Steps to test:

1. Open MATE Terminal
1. Execute `marco --replace &`
1. Close MATE Terminal

Expected result:

* The currently running window manager was replaced with Marco. No applications crashed or freezed.

### Run Marco with compositing enabled

Steps to test:

1. Open MATE Terminal
1. Execute `marco --composite --replace &`
1. Close MATE Terminal
1. Drag window to the screen edge to snap it here.

Expected result:

* The currently running window manager was replaced with Marco. The compositing was enabled. Snapping is done with color shadow below the window. No applications crashed or freezed.

### Run Marco with compositing disabled

Steps to test:

1. Open MATE Terminal
1. Execute `marco --no-composite --replace &`
1. Close MATE Terminal
1. Drag window to the screen edge to snap it here.

Expected result:

* The currently running window manager was replaced with Marco. The compositing was disabled. Snapping is done with wire frame instead of window border. No applications crashed or freezed.

## Using `marco-message` command

The `marco-message` command allows to send messages to Marco.

### Restart

Steps to test:

1. Open MATE Terminal
1. Execute `marco-message restart`
1. Close MATE Terminal

Expected results:

* Marco was restarted. No applications crashed or freezed.

### Reload theme

Steps to test:

1. Open MATE Terminal
1. Execute `marco-message reload-theme`
1. Close MATE Terminal

Expected results:

* Marco reloaded active theme, there no visual window changes. No applications crashed or freezed.

### Disable keybindings

Steps to test:

1. Open MATE Terminal
1. Execute `marco-message disable-keybindings`
1. Close MATE Terminal
1. Press `<Ctrl>+<Alt>+<T>`

Expected results:

* All Marco keybindings disabled. After pressing `<Ctrl>+<Alt>+<T>` the MATE Terminal is not opened.

### Enable keybindings

Steps to test:

1. Open MATE Terminal
1. Execute `marco-message enable-keybindings`
1. Close MATE Terminal
1. Press `<Ctrl>+<Alt>+<T>`

Expected results:

* All Marco keybindings enabled. After pressing `<Ctrl>+<Alt>+<T>` the MATE Terminal is opened as usual.

### Toggle verbose

Steps to test:

1. Open two MATE terminals
1. Execute `tail -f ~/.xsession-errors` in the first MATE Terminal
1. Execute `marco-message toggle-verbose` in the second terminal
1. Open some new application (for example MATE Calculator) and see growing log in the first terminal
1. Execute `marco-message toggle-verbose` in the second terminal again

Expected results:

* The contents of `~/.xsession-errors` changed according to the number of executions of `marco-message toggle-verbose` command.

## Using `marco-theme-viewer` command

The `marco-theme-viewer` allows user to preview window themes using Marco.

Steps to test:

1. Open MATE Terminal
1. Execute `marco-theme-viewer Radiant-MATE` to preview *Radiant-MATE* theme
1. Close the preview window.
1. Execute `marco-theme-viewer Ambiant-MATE` to preview *Ambiant-MATE* theme
1. Close the preview window.

Expected results:

* The theme previewer window changes its contents in style of user-defined theme.

## Using `marco-window-demo` command

The `marco-window-demo` is a demo of window features.

Steps to test:

1. Open MATE Terminal
1. Execute `marco-window-demo`
1. Choose needed window features
1. Close all demo windows

Expected results:

* All demos of window features are shown correctly.
