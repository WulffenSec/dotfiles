#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Starship
#eval "$(starship init bash)"

# Powerline
#. /home/wulffen/.local/lib/python3.10/site-packages/powerline/bindings/bash/powerline.sh

# colorscript
#colorscript -r

# PS1 Mod
PS1='[\u@\h \W]\$ '

# History
HISTCONTROL=ignoreboth
HISTTIMEFORMAT="%d/%m/%Y - %T "

if [ -x "$(command -v pacman)" ]; then
    alias update='sudo pacman -Syu && paru -Syu'
elif [ -x "$(command -v apt)" ]; then
    alias update='sudo apt update && sudo apt upgrade'
elif [ -x "$(command -v dnf)" ]; then
    alias update='sudo dnf update'
else
    echo "Fail to find package manager"
fi

# Aliases
alias ls='exa --icons --color=always --group-directories-first'
alias ll='exa --icons -lah --color=always --group-directories-first'
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias cp='cp -i'
alias mv='mv -i'
alias rm='rm -i'
alias mkdir='mkdir -pv'
alias find='fdfind --hidden'
alias cat='batcat --color=always'
alias diff='diff --color=auto'
alias grep='rg --color=always --hidden'
alias ip='ip --color=auto'
alias ssh='kitty +kitten ssh'
alias myip='dog +short myip.opendns.com @resolver1.opendns.com'
alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'


# BEGIN_KITTY_SHELL_INTEGRATION
if test -n "$KITTY_INSTALLATION_DIR" -a -e "$KITTY_INSTALLATION_DIR/shell-integration/bash/kitty.bash"; then source "$KITTY_INSTALLATION_DIR/shell-integration/bash/kitty.bash"; fi
# END_KITTY_SHELL_INTEGRATION
