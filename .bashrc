#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# PS1 Modded
export PS1="\[$(tput bold)\]\[\033[31m\][\[$(tput bold)\]\[\033[0m\]\u\[$(tput bold)\]\[\033[31m\]@\[$(tput bold)\]\[\033[0m\]\h\[$(tput bold)\]\[\033[31m\]][\[$(tput bold)\]\[\033[0m\]\w\[$(tput bold)\]\[\033[31m\]]\[$(tput bold)\]\[\033[0m\]\$(git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/')\[$(tput bold)\]\[\033[31m\][\[$(tput bold)\]\[\033[0m\]\$?\[$(tput bold)\]\[\033[31m\]]\[$(tput bold)\]\n\[$(tput bold)\]\[$(tput bold)\]\[\033[31m\][\[$(tput bold)\]\[\033[0m\]\\$\[$(tput bold)\]\[\033[31m\]]>>\[$(tput bold)\] \[$(tput bold)\]\[\033[0m\]"

# History
HISTCONTROL=ignoreboth
HISTTIMEFORMAT="%m/%d/%Y - %T "
HISTSIZE=10000
HISTFILESIZE=10000

# Path inclusion
export PATH=$PATH:$HOME/.local/bin
export PATH=~/.npm-global/bin:$PATH
export PATH=~/anaconda3/bin:$PATH
export PATH=$PATH:$HOME/go/bin

# Quick server
# TODO: Needs redo.
server() {
    python3 -m http.server
}

penv() {
    if [ -z "$VIRTUAL_ENV" ]; then
        if [[ -d .env ]]; then
            source .env/bin/activate
        else
            python -m venv .env && source .env/bin/activate
        fi
    else
       VIRTUAL_ENV=""
       deactivate 
    fi
}

# Aliases
alias ls='ls -Ahop --group-directories-first --color=always'
alias grep='grep --color=always -Hn'
alias mkdir='mkdir -pv'
alias diff='diff -r --color=always'
alias ip='ip -h --color=always'
alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'
alias df='df -Thx tmpfs -x devtmpfs'
alias du='ncdu'

# LS COLORS
LS_COLORS='no=00;00:fi=00;00:di=04;93:ln=04;36:pi=01;31:do=01;95:bd=41;30:cd=43;30:or=04;94:so=01;34:su=45;97:sg=44;97:tw=30;42:ow=30;42:st=30;44:ex=01;32:mi=04;37:*.tar=01;33:*.tgz=01;33:*.arc=01;33:*.arj=01;33:*.taz=01;33:*.lha=01;33:*.lz4=01;33:*.lzh=01;33:*.lzma=01;33:*.tlz=01;33:*.txz=01;33:*.tzo=01;33:*.t7z=01;33:*.zip=01;33:*.z=01;33:*.dz=01;33:*.gz=01;33:*.lrz=01;33:*.lz=01;33:*.lzo=01;33:*.xz=01;33:*.zst=01;33:*.tzst=01;33:*.bz2=01;33:*.bz=01;33:*.tbz=01;33:*.tbz2=01;33:*.tz=01;33:*.deb=01;33:*.rpm=01;33:*.jar=01;33:*.war=01;33:*.ear=01;33:*.sar=01;33:*.rar=01;33:*.alz=01;33:*.ace=01;33:*.zoo=01;33:*.cpio=01;33:*.7z=01;33:*.rz=01;33:*.cab=01;33:*.wim=01;33:*.swm=01;33:*.dwm=01;33:*.esd=01;33:*.avif=01;36:*.jpg=01;36:*.jpeg=01;36:*.mjpg=01;36:*.mjpeg=01;36:*.gif=01;36:*.bmp=01;36:*.pbm=01;36:*.pgm=01;36:*.ppm=01;36:*.tga=01;36:*.xbm=01;36:*.xpm=01;36:*.tif=01;36:*.tiff=01;36:*.png=01;36:*.svg=01;36:*.svgz=01;36:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;31:*.au=00;31:*.flac=00;31:*.m4a=00;31:*.mid=00;31:*.midi=00;31:*.mka=00;31:*.mp3=00;31:*.mpc=00;31:*.ogg=00;31:*.ra=00;31:*.wav=00;31:*.oga=00;31:*.opus=00;31:*.spx=00;31:*.xspf=00;31:*~=04;90:*#=04;90:*.bak=04;90:*.old=04;90:*.orig=04;90:*.part=04;90:*.rej=04;90:*.swp=04;90:*.tmp=04;90:*.dpkg-dist=04;90:*.dpkg-old=04;90:*.ucf-dist=04;90:*.ucf-new=04;90:*.ucf-old=04;90:*.rpmnew=04;90:*.rpmorig=04;90:*.rpmsave=04;90:*.txt=00;00:*.md=00;00:*.docx=00;00:*.pdf=00;00:*.stl=00;35:*.apk=00;35:*.img=00;35:*.ova=04;35:*.vmdk=04;35:*.vdi=04;35:*.qcow2=04;35:*.py=01;34:*.go=01;36:*.js=01;33:*.json=01;36'
export LS_COLORS

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

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/wulffen/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/wulffen/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/wulffen/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/wulffen/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
