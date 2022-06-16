# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Import
from typing import List  # noqa: F401

from libqtile import bar, layout, widget, extension, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder

# Defines aliases
mod = "mod4"
mod1 = "mod1"
mod2 = "control"
mod3 = "shift" 

# Automatic floating dialogs
@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True

# Calendar

def opencal():
        qtile.cmd_spawn("gsimplecal")

def closecal():
        qtile.cmd_spawn("killall -q gsimplecal")

#Keybindings
keys = [
       
    # Toggles Fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen()), 

    # Switch between windows
    Key([mod], "j", lazy.layout.down()), # Tile
    Key([mod], "k", lazy.layout.up()),
    #Key([mod], "h", lazy.layout.left()), # MonadTall
    #Key([mod], "l", lazy.layout.right()),
    #Key([mod], "j", lazy.layout.down()),
    #Key([mod], "k", lazy.layout.up()),
    #Key([mod], "space", lazy.layout.flip()),

    # Shuffle Windows 
    Key([mod, mod3], "j", lazy.layout.shuffle_down()), # Tile
    Key([mod, mod3], "k", lazy.layout.shuffle_up()),
    #Key([mod, mod3], "h", lazy.layout.shuffle_left()), # MonadTall
    #Key([mod, mod3], "l", lazy.layout.shuffle_right()),
    #Key([mod, mod3], "j", lazy.layout.shuffle_down()),
    #Key([mod, mod3], "k", lazy.layout.shuffle_up()),

    # Grow windows
    Key([mod], "h", lazy.layout.decrease_ratio()), # Tile
    Key([mod], "l", lazy.layout.increase_ratio()),
    Key([mod], "i", lazy.layout.reset()),
    #Key([mod, mod2], "h", lazy.layout.shrink()), # MonadTall
    #Key([mod, mod2], "l", lazy.layout.grow()),
    #Key([mod, mod2], "j", lazy.layout.reset()),
    #Key([mod, mod2], "k", lazy.layout.maximize()),
    
    # Toggle Layout
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    # Kill window
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    # Qtile restart
    Key([mod, mod3], "r", lazy.restart(), desc="Restart Qtile"),
    # Qtile shutdown
    Key([mod, mod3], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

# www
Brave = 'brave-browser'
Firefox = 'firefox'
Freetube = 'freetube'
Nuclear = 'nuclear'
# sys
Kitty = 'kitty'
PCManFM = 'pcmanfm'
Nautilus = 'org.gnome.Nautilus'
Alacritty = 'Alacritty'
# Coding
VSCode = 'vscodium'
# 3D
Superslicer = 'superslicer'
FreeCAD = 'freecad'
OpenSCAD = 'openscad'
# 2D
Inkscape = 'Inkscape'
GIMP = 'gimp'
# Media
VLC = 'vlc'
MPV = 'mpv'
# VM
VirtManager = 'virt-manager'
# Chat
Telegram = 'telegram-desktop'
Signal = 'Signal'
# Games
Steam = 'Steam'

# Groups
groups = [
               Group("", matches=[Match(wm_class=[Brave, Firefox])]),
               Group("", matches=[Match(wm_class=[Freetube, Nuclear, VLC, MPV])]),
               Group("", matches=[Match(wm_class=[Alacritty, Kitty])]),
               Group("", matches=[Match(wm_class=[PCManFM, Nautilus])]),
               Group("", matches=[Match(wm_class=[VSCode])]),
               Group("", matches=[Match(wm_class=[Superslicer, FreeCAD, OpenSCAD])]),
               Group("", matches=[Match(wm_class=[Inkscape, GIMP])]),
               Group("", matches=[Match(wm_class=[VirtManager])]),
               Group("", matches=[Match(wm_class=[Telegram, Signal])]),
               Group("", matches=[Match(wm_class=[Steam])]),

                ]

# Groups Keybining
dgroups_key_binder = simple_key_binder(mod)

layouts = [
               #layout.MonadTall(
                   #border_focus="#b58900", border_normal="#586e75", 
                   #border_width=3, margin=15, max_ratio=0.80, 
                   #single_border=True, single_margin=15, ratio=0.7
                   #),
               layout.Tile(
                   border_focus="b58900", border_normal="586e75", border_width=3, 
                   margin=15, shift_windows=True, ratio=0.7 
                   ),
    	       layout.Floating(
                   border_focus="b58900", border_normal="586e75", border_width=3
                   ),
               #layout.Columns(),
               #layout.Max(),
               #layout.Stack(),
               #layout.Bsp(),
               #layout.Matrix(),
               #layout.MonadWide(),
               #layout.RatioTile(),
               #layout.TreeTab(),
               #layout.VerticalTile(),
               #layout.Zoomy(),
]

widget_defaults = dict(
    font='Hack',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
         top=bar.Bar(
            [
                widget.GroupBox(
                                font='FontAwesome6Free', fontsize=18, disable_drag=True, 
                                active='cb4b16', inactive='586e75',
                                this_current_screen_border='b58900',
                                urgent_alert_method='text', urgent_text='d33682'
                                ),
                widget.WindowName(foreground='268bd2'),
                widget.TextBox(
                    font='FontAwesome', fontsize=18,
                    foreground='dc322f', text='  ',
                    ),
                widget.CPU(
                            foreground='dc322f', 
                            format='{load_percent}%',
                            ),
                widget.TextBox(
                                font='FontAwesome6Free', fontsize=18,
                                foreground='b58900', text='  ',
                                ),
                widget.Memory(
                                format='{MemPercent}%', 
                                foreground='b58900'
                                ),
                widget.TextBox(
                                font='FontAwesome6Free', fontsize=18,
                                foreground='d33682', text='  ',
                                ),
                 widget.Net(
                                foreground='d33682',
                                format='{down}',
                                prefix='M',
                                ),
                widget.TextBox(
                                font='FontAwesome6Free', fontsize=18,
                                foreground='d33682', text=' ',
                                ),
                 widget.Net(
                                foreground='d33682',
                                format='{up}',
                                prefix='M',
                                ),
                widget.TextBox(
                                foreground='859900', text='  ',
                                font='FontAwesome6Free', fontsize=18,
                                ),
                widget.Volume(foreground='859900'),
                widget.CurrentLayout(foreground='268bd2'),
                widget.TextBox(
                                font='FontAwesome6Free', fontsize=18,
                                foreground='6c71c4', text='',
                                ),
                widget.Clock(
                    format='%H:%M', foreground='6c71c4',
                    ),
                widget.TextBox(
                                font='FontAwesome6Free', fontsize=18,
                                foreground='6c71c4', text=' ',
                                ),
                widget.Clock(
                    format='%a.%d/%m/%y', foreground='6c71c4',
                    mouse_callbacks={'Button1': opencal, 'Button2': closecal}
                    ),
                widget.Systray(),
                                 
            ],
            30, background='002b36', foreground='268bd2' 
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
