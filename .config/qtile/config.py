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

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import subprocess

@hook.subscribe.startup
def func():
    subprocess.run(["sh", "-c", "$HOME/.config/autostart.sh"])

mod = "mod4"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "mod1"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "mod1"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "Return", lazy.spawn("rofi -show drun"), desc="Run a command using rofi"),
    Key([mod, "mod1"], "Return", lazy.spawn("pcmanfm"), desc="Run a command using rofi")
]

groups = [Group(i) for i in "123456789"]
groups = [
        Group(name="1", label="", matches=[Match(wm_class=["kitty"])]),
        Group(name="2", label="󰖟", matches=[Match(wm_class=["firefox"])]),
        Group(name="3", label="", matches=[Match(wm_class=["FreeTube"])]),
        Group(name="4", label="", matches=[Match(wm_class=["Pcmanfm"])]),
        Group(name="5", label=""),
        Group(name="6", label="󱕴", matches=[Match(wm_class=["KeePassXC"])]),
        Group(name="7", label="󱊞"),
        Group(name="8", label="", matches=[Match(wm_class=["Virt-manager"])]),
        Group(name="9", label="", matches=[Match(wm_class=["Signal"])]),
        Group(name="0", label="", matches=[Match(wm_class=["Steam"])])
        ]

for i in groups:
    keys.extend(
            [
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                ),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                ),
            ]
        )

# F Shortcuts
keys.extend([
    Key([mod], "F1", lazy.spawn("firefox")),
    Key([mod], "F2", lazy.spawn("flatpak run io.freetubeapp.FreeTube"))
    ])

layouts = [
    layout.Columns(
        border_focus="FFFFFF",
        border_normal="222222",
        border_on_single=True,
        border_width=2,
        margin=[10, 10, 20, 10],
        margin_on_single=[10, 10, 20, 10]
        ),
    layout.Floating(
        border_focus="FFFFFF",
        border_normal="222222",
        border_width=2
        )
]

widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=12,
    padding=3,
)

extension_defaults = widget_defaults.copy()

screens = [
        Screen(
            top=bar.Bar(
                [
                    widget.GroupBox(
                        active="666666",
                        inactive="222222",
                        borderwidth=2,
                        margin=2,
                        highlight_method="text",
                        this_current_screen_border="FFFFFF",
                        this_screen_border="FFFFFF",
                        urgent_alert_method="text",
                        urgent_border="FF0000",
                        urgent_text="FF0000"
                        ),
                    widget.Spacer(length=10),
                    widget.WindowName(),
                    widget.Spacer(length=10),
                    widget.CPU(format="󰻠 {freq_current}GHz {load_percent}%"),
                    widget.Spacer(length=10),
                    widget.Memory(format="󰍛 {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm} {MemPercent:.0f}%", measure_mem="G"),
                    widget.Spacer(length=10),
                    widget.Net(format=" {down} /  {up}"),
                    widget.Spacer(length=10),
                    widget.StatusNotifier(),
                    widget.Systray(),
                    widget.Spacer(length=10),
                    widget.Clock(format="%Y-%m-%d %a %H:%M")
                ],
                24,
                opacity=0.7,
                background="222222",
                border_width=2,
                border_color="FFFFFF",
                margin=[20, 10, 10, 10]
            ),
        ),
    ]

# Drag floating layouts.
mouse = [
        Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front()),
    ]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
        float_rules=[
            *layout.Floating.default_float_rules,
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(wm_class="Pinentry-gtk-2"),  # GPG key password entry
        ]
    )

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
