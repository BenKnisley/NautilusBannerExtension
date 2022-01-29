"""
Author: Ben Knisley [benknisley@gmail.com]
Created: 27 January, 2022
Title: NautilusBannerExtension
Description:
Nautilus extension that provides an way to display a custom text banner at the 
top of a Nautilus window. Scans each folder displayed by Nautilus for a file 
named '.banner', if found the text inside the file is displayed on the banner at
the top of the window.
"""
import os
import gi
gi.require_version('Nautilus', '3.0')
from gi.repository import Nautilus, Gtk, GObject, Gdk
from urllib.parse import unquote, urlparse

BANNER_FILENAME = '.banner'
BANNER_COLOR = "#993147"


class NautilusBannerExtension(GObject.GObject, Nautilus.LocationWidgetProvider):
    """
    The NautilusBanner Extension class. The entry point to the extension, called
    automatically by the Nautilus application to provide a widget to display at 
    the top of the Nautilus Window.
    """

    def get_widget(self, uri, window):
        """
        If a banner file exists in the Nautilus window current directory, 
        creates a new NoteBanner instance with .banner file text and returns 
        widget to caller.

        Parameters:
            uri (str): The uri of the current window.

            window (__gi__.NautilusWindow): The parent window object that the 
                widget will be added to.
        """
        ## Generate the full path for banner file in the window's folder
        directory_path = os.path.abspath(urlparse(unquote(uri)).path)
        banner_file_path = f"{directory_path}/{BANNER_FILENAME}"
        
        ## Return None if the banner file does not exist (nothing shown)
        if not os.path.exists(banner_file_path):
            return
        
        ## Read banner file and strip whitespace from text
        with open(banner_file_path) as f:
            banner_txt = f.read().strip()

        ## If banner file is empty, return None (nothing shown)
        if banner_txt == "":
            return

        ## Create and return a new NoteBanner instance with banner text
        return NoteBanner(banner_txt)

class NoteBanner(Gtk.Bin):
    """
    A widget that displays text overlayed on top of a ribbon; intended to be 
    displayed at the top of the Nautilus window.
    """
    def __init__(self, banner_txt):
        """
        Initializes the NoteBanner object. Sets up layout and label with given
        banner text.

        Parameters:
            banner_txt (str): The text to display on the banner. Can be markdown
                format with html tags.
        
        Returns:
            None
        """
        Gtk.Bin.__init__(self)
        
        ## Prepend and append empty lines to text to act at padding
        banner_txt = '\n' + banner_txt + '\n'

        ## Create a horizontal layout, and have it managed widget's layout
        self.layout = Gtk.HBox()
        self.add(self.layout)

        ## Set the color of banner by setting the layout's bg color
        self.layout.modify_bg(Gtk.StateType(0), Gdk.color_parse(BANNER_COLOR))

        ## Create a label and set it to display the banner text
        self.label = Gtk.Label()
        self.label.set_markup(banner_txt)

        ## Set the alignment to left
        self.label.set_alignment(0,0)

        ## Add label to layour
        self.layout.pack_start(self.label, True, True, 10)

        ## Show all widgets
        self.show_all()
