from AppKit import NSWorkspace
# NSWorkspace is a class in the Cocoa framework for macOS. It provides an interface
# for interacting with the file system,
# including opening and launching files and applications, performing file
# operations such as copying and moving, and working with volumes and drives.
import time

active_window_name = ""
while True:

    new_window_name = (NSWorkspace.sharedWorkspace().activeApplication()
    ['NSApplicationName'])

    if active_window_name != new_window_name:
        active_window_name = new_window_name
        print(active_window_name)
    time.sleep(10)

