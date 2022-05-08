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

# Script, which prints focused window title to stdout.

from i3ipc import Connection

def get_focused_window_title(ipc):
    return ipc.get_tree().find_focused().window_title


def main():
    ipc = Connection()
    focused_window_title = get_focused_window_title(ipc)
    if focused_window_title is not None:
        print(focused_window_title)
    else:
        print('')

if __name__ == "__main__":
    main()
