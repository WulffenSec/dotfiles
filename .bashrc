#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# PS1 Modded
export PS1="\[$(tput bold)\]\[\033[32m\][\[$(tput bold)\]\[\033[0m\]\u\[$(tput bold)\]\[\033[32m\]@\[$(tput bold)\]\[\033[0m\]\h\[$(tput bold)\]\[\033[32m\]][\[$(tput bold)\]\[\033[0m\]\w\[$(tput bold)\]\[\033[32m\]]\[$(tput bold)\]\[\033[0m\]\$(git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/')\[$(tput bold)\]\[\033[32m\][\[$(tput bold)\]\[\033[0m\]\$?\[$(tput bold)\]\[\033[32m\]]\[$(tput bold)\]\n\[$(tput bold)\]\[$(tput bold)\]\[\033[32m\][\[$(tput bold)\]\[\033[0m\]\\$\[$(tput bold)\]\[\033[32m\]]>>\[$(tput bold)\] \[$(tput bold)\]\[\033[0m\]"

# History
HISTCONTROL=ignoreboth
HISTTIMEFORMAT="%m/%d/%Y - %T "
HISTSIZE=10000
HISTFILESIZE=10000

# Path inclusion
export PATH=$PATH:$HOME/.local/bin:$HOME/.npm-global/bin:$HOME/go/bin
export PATH=$PATH:$HOME/android/sdk/build-tools/34.0.0:$HOME/android/sdk/platform-tools
export PATH=$PATH:$HOME/android/sdk/emulator:$HOME/android/cmdline-tools/bin

# Quick server
# TODO: Needs redo.
server() {
    python3 -m http.server
}

# Conda evironment
penv() {
    if [[ $PENV != True ]]; then
        if [[ ! -d .env ]]; then
            echo "No virtual environment detected. Creating one."
            python -m venv .env
            source .env/bin/activate
            PENV=True
        else
            echo "Activating virtual environment."
            source .env/bin/activate
            PENV=True
        fi
    else
        echo "Deactivating virtual environment."
        deactivate
        PENV=FALSE
    fi
}

wallpaper() {
    sed -i "s|WALLPAPER=.*|WALLPAPER=$1|" $HOME/scripts/autostart.sh
    sed -i "s|WALLPAPER=.*|WALLPAPER=$1|" $HOME/scripts/wallpaper.sh
    sh -c ~/scripts/wallpaper.sh
}

share() {
    kdeconnect-cli -n Edge --share "$1"
}

# Aliases
alias ls='ls -hop --group-directories-first --color=always'
alias grep='grep --color=always -Hn -iE'
alias mkdir='mkdir -pv'
alias diff='diff -r --color=always'
alias ip='ip -h --color=always'
alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'
alias df='df -Thx tmpfs -x devtmpfs'
alias du='du -x'
alias reinstall='pacman -Qknq | cut -d " " -f1 | sort -u | sudo pacman -S - --noconfirm --overwrite "*"'
alias yt-mp3='yt-dlp --extract-audio --audio-format mp3 --audio-quality 0'
alias ping='ping -c 3'
alias rsync="bash -e $HOME/scripts/rsync.sh"

source $HOME/.ls_colors.sh

# Kitty Shell integration
if [ -x "$(command -v kitty)" ]; then
    if test -n "$KITTY_INSTALLATION_DIR" -a -e "$KITTY_INSTALLATION_DIR/shell-integration/bash/kitty.bash"; then
        source "$KITTY_INSTALLATION_DIR/shell-integration/bash/kitty.bash";
        alias ssh='kitty +kitten ssh'
    fi
fi

# Shell options
shopt -s extglob

# GPG
export GPG_TTY=$(tty)

export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

if [[ $(cat $HOME/TODO.md | wc -l) > 1 ]]; then
    glow $HOME/TODO.md
fi
