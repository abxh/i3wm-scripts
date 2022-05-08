#!/usr/bin/python

"""
Copyright (C) 2022 Shamim Siddique abir09bs@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# Script to update i3blocks, when user changes focus.

from i3ipc import Connection,  Event
import subprocess

SIGNAL=10

def update_title():
    subprocess.run(["pkill","-SIGRTMIN+"+str(SIGNAL),"i3blocks"])

def main():
    ipc = Connection()

    def on_window_change(ipc, e):
        if e.change in ["focus","close","title"]:
            update_title()
    ipc.on(Event.WINDOW,on_window_change)
    
    def on_workspace_change(ipc, e):
        if e.change == "focus":
            update_title()
    ipc.on(Event.WORKSPACE,on_workspace_change)

    ipc.main()

if __name__ == "__main__": 
    main()
