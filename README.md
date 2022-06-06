# i3wm-scripts
Scripts made for i3wm. Depends on `python-i3ipc`.
## autoname_workspaces.py
Automatically name workspaces based on the windows in the workspaces.

Inspired by:
- https://github.com/walshc/i3/blob/master/scripts/autoname-workspaces.py
- https://github.com/swaywm/sway/blob/master/contrib/autoname-workspaces.py

## focused_window.py
Print focused window title to stdout.

## focused_window_update.py
Update i3blocks blocklet, when focused window title has changed.

## Sample configuration:
### i3:
```
exec_always --no-startup-id ~/.scripts/i3wm-scripts/autoname_workspaces.py
exec_always --no-startup-id ~/.scripts/i3wm-scripts/focused_window_update.py
```
### i3blocks:
```
[window]
command=~/.scripts/i3wm-scripts/focused_window.py
min_width=1920
align=center
signal=10
```
