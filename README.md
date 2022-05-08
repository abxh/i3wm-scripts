# i3ipc-scripts
Scripts, which depends on python-i3ipc made for i3wm.
## autoname_workspaces.py
Scripts which automatically names workspaces based on the windows in the workspaces.

Inspired by:
- https://github.com/walshc/i3/blob/master/scripts/autoname-workspaces.py
- https://github.com/swaywm/sway/blob/master/contrib/autoname-workspaces.py

## focused_window.py
Script, which prints focused window title to stdout.

## focused_window_update.py
Script, which updates i3blocks, when focused window title has changed.

Sample configuration:
### i3blocks:
```
[window]
command=~/.scripts/i3ipc/focused_window.py
min_width=1920
align=center
signal=10
```
### i3:
```
# focused_window_update.py - update focused window title in i3blocks
exec_always --no-startup-id $scripts/i3ipc/focused_window_update.py
