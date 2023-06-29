#!/usr/bin/env python
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import subprocess
import os



@hook.subscribe.startup
def func():
    # Autostart
    subprocess.run(['sh', '-c', '$HOME/scripts/autostart.sh'])

# Variables
mod = 'mod4'
home = os.getenv('HOME')
wofi = [
    'wofi --xoffset 1500 --insensitive ',
    '--height 1080 --hide-scroll --width 420 ',
    f'--style {home}/.config/wofi/style.css --term kitty --prompt "Search" --show run'
]

keys = [
    # Qtile base keys
    Key([mod], 'h', lazy.layout.left(),
        desc='Move focus to left'),
    Key([mod], 'l', lazy.layout.right(),
        desc='Move focus to right'),
    Key([mod], 'j', lazy.layout.down(),
        desc='Move focus down'),
    Key([mod], 'k', lazy.layout.up(),
        desc='Move focus up'),
    Key([mod], 'space', lazy.layout.next(),
        desc='Move window focus to other window'),
    Key([mod, 'shift'], 'h', lazy.layout.shuffle_left(),
        desc='Move window to the left'),
    Key([mod, 'shift'], 'l', lazy.layout.shuffle_right(),
        desc='Move window to the right'),
    Key([mod, 'shift'], 'j', lazy.layout.shuffle_down(),
        desc='Move window down'),
    Key([mod, 'shift'], 'k', lazy.layout.shuffle_up(),
        desc='Move window up'),
    Key([mod, 'control'], 'h', lazy.layout.grow_left(),
        desc='Grow window to the left'),
    Key([mod, 'control'], 'l', lazy.layout.grow_right(),
        desc='Grow window to the right'),
    Key([mod, 'control'], 'j', lazy.layout.grow_down(),
        desc='Grow window down'),
    Key([mod, 'control'], 'k', lazy.layout.grow_up(),
        desc='Grow window up'),
    Key([mod], 'n', lazy.layout.normalize(),
        desc='Reset all window sizes'),
    Key([mod], 'Tab', lazy.next_layout(),
        desc='Toggle between layouts'),
    Key([mod], 'q', lazy.window.kill(),
        desc='Kill focused window'),
    Key([mod, 'mod1'], 'r', lazy.reload_config(),
        desc='Reload the config'),
    Key([mod, 'mod1'], 'q', lazy.shutdown(),
        desc='Shutdown Qtile'),
    # Terminal, App launcher, Filemanager
    Key([mod], 'Return', lazy.spawn('kitty'),
        lazy.group['1'].toscreen(), desc='Launch terminal'),
    Key([mod, 'control'], 'Return', lazy.spawn(wofi[0] + wofi[1] + wofi[2]),
        desc='Run a command using wofi'),
    Key([mod, 'mod1'], 'Return', lazy.spawn('pcmanfm'),
        lazy.group['4'].toscreen(), desc='Open Filemanager'),
    # Poweroff and reboot
    Key([mod, 'mod1'], 'p', lazy.spawn('systemctl poweroff'),
        desc='Shutdown the computer'),
    Key([mod, 'mod1'], 'o', lazy.spawn('systemctl reboot'),
        desc='Reboot the computer'),
    Key([mod], 'f', lazy.window.toggle_floating(),
        desc='Toggle floating on the window.'),
    Key([mod, 'control'], 'f', lazy.window.toggle_fullscreen(),
        desc='Toggle fullscreen on the window.')
]


# F Shortcuts
keys.extend([
    Key([mod], 'F1', lazy.spawn('firefox'),
        lazy.group['2'].toscreen())
])

# Audio Keys
keys.extend([
    Key([], 'XF86AudioMute',
        lazy.spawn('sh -c $HOME/scripts/muteVol.sh')),
    Key([], 'XF86AudioLowerVolume',
        lazy.spawn('sh -c $HOME/scripts/lowerVol.sh')),
    Key([], 'XF86AudioRaiseVolume',
        lazy.spawn('sh -c $HOME/scripts/raiseVol.sh')),
    Key(['mod1'], 'XF86AudioMute',
        lazy.spawn('sh -c $HOME/scripts/audioSink.sh'))
])

# Groups name(for switching) label(for show)
groups = [
    Group(name='1', label='',
          matches=[Match(wm_class=['kitty'])]),
    Group(name='2', label='󰖟',
          matches=[Match(wm_class=['firefox'])]),
    Group(name='3', label='',
          matches=[Match(wm_class=['FreeTube'])]),
    Group(name='4', label='',
          matches=[Match(wm_class=['Pcmanfm'])]),
    Group(name='5', label=''),
    Group(name='6', label='󱕴',
          matches=[Match(wm_class=['KeePassXC', 'org.keepassxc.KeePassXC'])]),
    Group(name='7', label='󱊞'),
    Group(name='8', label='',
          matches=[Match(wm_class=['Virt-manager'])]),
    Group(name='9', label='',
          matches=[Match(wm_class=['Signal'])]),
    Group(name='0', label='',
          matches=[Match(wm_class=['Steam', 'steam'])], layout='tile')
]

# Switching workspace, move windows to a workspace
for i in groups:
    keys.extend([
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc='Switch to group {}'.format(i.name),
                ),
                Key(
                    [mod, 'shift'],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc='Switch to & move focused window to group.',
                )])

# Layout active
layouts = [
    layout.Columns(
        border_focus='FFFFFF',
        border_normal='222222',
        border_on_single=True,
        border_width=2,
        margin=[10, 10, 10, 10],
        margin_on_single=[10, 10, 10,10]
    ),
    layout.Floating(
        border_focus='FFFFFF',
        border_normal='222222',
        border_width=4
    ),
    layout.Tile(
        border_focus='FFFFFF',
        border_normal='222222',
        border_on_single=True,
        border_width=2,
        margin=[10, 10, 10, 10],
        margin_on_single=[10, 10, 10, 10],
        ratio=0.70
    )]

# Options for every widget
widget_defaults = dict(
    font='Hack Nerd Font',
    fontsize=14,
    padding=2
)
extension_defaults = widget_defaults.copy()

# Bar config
screens = [
    Screen(
        top=bar.Bar([
            widget.CurrentLayoutIcon(scale=0.5),
            widget.GroupBox(
                    fontsize=16,
                    active='666666',
                    inactive='111111',
                    borderwidth=2,
                    margin=3,
                    padding=4,
                    highlight_method='text',
                    this_current_screen_border='FFFFFF',
                    this_screen_border='FFFFFF',
                    urgent_alert_method='text',
                    urgent_border='FF0000',
                    urgent_text='FF0000'
                    ),
            widget.Sep(foreground='FFFFFF', linewidth=2, size_percent=100,padding=10),
            widget.WindowName(padding=4),
            widget.Sep(foreground='FFFFFF', linewidth=2, size_percent=100,padding=10),
            widget.DF(format='󰋊 {uf}{m}|{r:.0f}%', visible_on_warn=False, padding=4),
            widget.CPU(format='󰻠 {freq_current}GHz {load_percent}%', padding=4),
            widget.Memory(
                format='󰍛 {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm} '
                + '{MemPercent:.0f}%', measure_mem='G', padding=4),
            widget.Net(format='{down} | {up}', prefix='M', padding=4),
            widget.Sep(foreground='FFFFFF', linewidth=2, size_percent=100,padding=10),
            widget.StatusNotifier(padding=4),
            widget.Volume(fmt='󰕾 {}', padding=4),
            widget.Clock(format='%Y-%m-%d %a %H:%M', padding=4)
        ],
            30,
            opacity=1,
            border_width=2,
            border_color='FFFFFF',
            background='000000',
            margin=[0, 10, 0, 10]
        ))]

# Drag floating layouts.
mouse = [
    Drag([mod], 'Button1', lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], 'Button3', lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], 'Button2', lazy.window.bring_to_front()),
]


# Floating rules, and style
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(wm_class='Pinentry-gtk-2'),  # GPG key password entry
        Match(wm_class='gnome-calculator')
    ],
    border_focus='FFFFFF',
    border_normal='222222',
    border_width=2
)

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = 'smart'
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = 'LG3D'
