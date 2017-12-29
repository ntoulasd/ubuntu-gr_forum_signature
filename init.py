#!/usr/bin/python
import platform
import subprocess

if platform.python_version() < '2.5':
    exit('ERROR: You need python 2.5 or higher to use this program.')
if platform.system() != "Linux":
    exit('ERROR: This script is built for GNU/Linux platforms (for now)')

try:
    import gi
    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk, Gdk
    # Start gtk3
    import forum_signature_gtk3
    forum_signature_gtk3.main()
except ImportError:
    print("Could not load gtk3 module.\n")

