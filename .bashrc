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

# PS1 Modded
PS1="\[$(tput bold)\]\[\033[38;5;118m\]\u\[$(tput sgr0)\]\[\033[38;5;255m\]@\[$(tput bold)\]\[\033[38;5;118m\]\h\[$(tput sgr0)\] \[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;255m\]\A\[$(tput sgr0)\] - \[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;118m\]\\$\[$(tput sgr0)\] \[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;255m\]\$(git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/')\[$(tput sgr0)\]\n\[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;118m\][\[$(tput bold)\]\[\033[38;5;255m\]\w\[$(tput sgr0)\]\[\033[38;5;118m\]]\[$(tput sgr0)\] \[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;118m\][\[$(tput sgr0)\]\[\033[38;5;255m\]\$?\[$(tput sgr0)\]\[\033[38;5;118m\]]\[$(tput sgr0)\]\n\[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;118m\]>>\[$(tput sgr0)\] \[$(tput sgr0)\]"

# History
HISTCONTROL=ignoreboth
HISTTIMEFORMAT="%m/%d/%Y - %T "

# Path inclusion
export PATH=~/.local/bin:$PATH

# Update system
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
alias find='fd --hidden'
alias cat='bat --color=always'
alias diff='diff --color=auto'
alias grep='rg --color=always --hidden'
alias ip='ip --color=auto'
alias ssh='kitty +kitten ssh'
alias myip='dog +short myip.opendns.com @resolver1.opendns.com'
alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'

# BEGIN_KITTY_SHELL_INTEGRATION
if test -n "$KITTY_INSTALLATION_DIR" -a -e "$KITTY_INSTALLATION_DIR/shell-integration/bash/kitty.bash"; then source "$KITTY_INSTALLATION_DIR/shell-integration/bash/kitty.bash"; fi
# END_KITTY_SHELL_INTEGRATION
