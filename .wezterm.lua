local wezterm = require 'wezterm'
if wezterm.config_builder then
  config = wezterm.config_builder()
end

-- Config
local config = {
    enable_wayland = false,
    font = wezterm.font('Hack'),
    font_size = 12.0,
    default_cursor_style = 'BlinkingUnderline',
    window_decorations = 'NONE',
    window_background_opacity = 0.8,
    term = 'wezterm',
    audible_bell = 'Disabled',
    keys = {
        {
          key = 'f',
          mods = 'SHIFT|CTRL',
          action = wezterm.action.ToggleFullScreen,
        },
    },
    colors = {
        foreground = '#FFFFFF',
        background = '#111111',

        cursor_fg = '#222222',
        cursor_bg = '#888888',
        cursor_border = '#666666',

        selection_bg = '#444444',
        selection_fg = '#999999',

        scrollbar_thumb = '#333333',
        split = '#333333',

        ansi = {
            'black',
            'maroon',
            'green',
            'olive',
            'navy',
            'purple',
            'teal',
            'silver',
            },
        brights = {
            'grey',
            'red',
            'lime',
            'yellow',
            'blue',
            'fuchsia',
            'aqua',
            'white',
            },
        compose_cursor = 'orange',
        tab_bar = {
            background = '#111111',
            active_tab = {
                bg_color = '#888888',
                fg_color = '#FFFFFF',
                },
            inactive_tab = {
                bg_color = '#444444',
                fg_color = '#888888'
            },
            new_tab = {
                bg_color = '#888888',
                fg_color = '#FFFFFF'
            },
        },
    },
}

return config
