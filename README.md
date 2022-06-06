# i3wm-scripts
Scripts made for i3wm. Depends on `i3ipc` python module, often packaged as `python-i3ipc` or `python3-i3ipc`.
## autoname_workspaces.py
Automatically name workspaces based on the windows in the workspaces.

Sample config:
```
# i3
exec_always --no-startup-id ~/.scripts/i3wm-scripts/autoname_workspaces.py
```
## focused_window.py
Print focused window title to stdout.

Sample config:
```
# i3blocks
[window]
command=~/.scripts/i3wm-scripts/focused_window.py
min_width=1920
align=center
signal=10
```
## focused_window_update.py
Update i3blocks blocklet, when focused window title has changed.

Sample config:
```
exec_always --no-startup-id ~/.scripts/i3wm-scripts/focused_window_update.py
```
