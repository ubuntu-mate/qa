# Pluma text editor

Pluma text editor is preinstalled on MATE DE. It may be called from terminal as `pluma`.

## Print preview

Steps to test:

1. Open Pluma
1. Write some text
1. Select *File*→*Print Preview* (or use `<Shift>+<Ctrl>+<P>`)

Expected result:

* Tab of current document changed to print preview until user presses `<Esc>`.

## Pluma extensions

Visit *Edit* → *Preferences*, switch to *Plugins* tab, then enable all Pluma extensions by doing right mouse click and selecting *Enable All* (or *Activate All*) and compare their list with the table below:

| Active Plugins               | 16.04 LTS | 18.04 LTS | 19.04 | 19.10 | 20.04 LTS | 20.10 |
| ---------------------------- | --------- | --------- | ----- | ----- | --------- | ----- |
| Change Case                  | +         | +         | +     | +     | +         | +     |
| Document Statistics          | +         | +         | +     | +     | +         | +     |
| External Tools               | +         | n/a       | +     | +     | +         | +     |
| File Browser Pane            | +         | +         | +     | +     | +         | +     |
| Insert Date/Time             | +         | +         | +     | +     | +         | +     |
| Modelines                    | +         | +         | +     | +     | +         | +     |
| Python Console               | +         | n/a       | +     | +     | +         | +     |
| Quick Open                   | +         | n/a       | +     | +     | +         | +     |
| Save Without Trailing Spaces | +         | +         | +     | +     | +         | +     |
| Snippets                     | +         | n/a       | +     | +     | +         | +     |
| Sort                         | +         | +         | +     | +     | +         | +     |
| Spell Checker                | +         | +         | +     | +     | +         | +     |
| Tag list                     | +         | +         | +     | +     | +         | +     |

Try to enable all plugins by checking their checkmarks. They should be enabled silently.

If you see stop-mark sign, then run `pluma` from terminal and check output in the terminal and in `tail -f ~/.xsession-errors`.

And then report bug using `apport-bug pluma`.

