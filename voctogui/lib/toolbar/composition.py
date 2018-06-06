import logging

from gi.repository import Gtk
import lib.connection as Connection

from lib.config import Config
from lib.videomixcontroller import VideoMixController


class CompositionToolbarController(object):
    """Manages Accelerators and Clicks on the Composition Toolbar-Buttons"""

    def __init__(self, toolbar, win, uibuilder):
        self.log = logging.getLogger('CompositionToolbarController')

        self.toolbar = toolbar
        self.uibuilder = uibuilder
        self.accelerators = Gtk.AccelGroup()
        win.add_accel_group(self.accelerators)

        composites = [
            'fullscreen',
            'picture_in_picture',
            'side_by_side_equal',
            'side_by_side_preview'
        ]

        self.composite_btns = {}

        # Composites = F1-F4
        for idx, name in enumerate(composites):
            self.add_composite_button(name, 'F%u' % (idx + 1))

    def add_composite_button(self, name, accel_key):
        key, mod = Gtk.accelerator_parse(accel_key)

        btn = self.uibuilder.find_widget_recursive(
            self.toolbar,
            'composite-' + name.replace('_', '-')
        )
        btn.set_name(name)

        btn.set_label(btn.get_label() + " (%s)" % accel_key)

        tooltip = Gtk.accelerator_get_label(key, mod)
        btn.set_tooltip_text(tooltip)

        # Thanks to http://stackoverflow.com/a/19739855/1659732
        btn.get_child().add_accelerator('clicked', self.accelerators,
                                        key, mod, Gtk.AccelFlags.VISIBLE)
        btn.connect('clicked', self.on_btn_toggled)

        self.composite_btns[name] = btn

    def on_btn_toggled(self, btn):
        btn_name = btn.get_name()
        self.log.info('composition-mode activated: %s', btn_name)
        VideoMixController.composite_mode = btn_name
        VideoMixController.apply()
