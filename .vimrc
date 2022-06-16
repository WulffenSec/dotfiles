" Show color syntax
syntax on

" Ecoding and stuff
set encoding=utf-8
set t_Co=256
set fillchars+=stl:\ ,stlnc:\

" Powerline
set laststatus=2
set rtp+=/home/wulffen/.vim/plugged/powerline/powerline/bindings/vim/
let g:Powerline_symbols = "fancy"

" Save with sudo
command! W execute 'w !sudo tee % > /dev/null' <bar> edit!

" Map leader
let mapleader = ","

" Hitory remembered
set history=500

" Tab width
set tabstop=4
set shiftwidth=4
set softtabstop=4

" Smart tabs
set smarttab

" Line break
set lbr
set tw=500
set ai " Auto indent
set si " Smart indent
set wrap " Wrap lines

" Use spaces instead of tabs
set expandtab

" Show numbers next to line
set number

" CMD settings
set showcmd
set cmdheight=1

" Show line where the cursor is
set cursorline

" Enable filetype plugins
filetype plugin indent on

" Set wildmenu
set wildmenu

" Don't redraw when executing macros
set lazyredraw

" Make better search
set showmatch
set incsearch

" Foldable tabs
set foldenable
set foldmethod=indent
set foldcolumn=1
set foldlevel=99

" Maps space to fold/unfold tabs
noremap <space> za

" Always show current position
set ruler

" Ignore case when searching
set ignorecase

" Be smart about case when searching
set smartcase

" Time it blinks when matching brackets
set mat=2

" No sound on erros
set noerrorbells
set novisualbell
set t_vb=
set tm=500

"  Tabs
nnoremap <leader>tn :tabnew<cr>
nnoremap <leader>to :tabonly<cr>
nnoremap <leader>tc :tabclose<cr>
nnoremap <leader>tm :tabmove
nnoremap <leader>t<leader> :tabnext

" Split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" Nerd Tree
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>

" Plugins
call plug#begin('~/.vim/plugged')
Plug 'powerline/powerline'
Plug 'rust-lang/rust.vim'
Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'tmhedberg/SimpylFold'
Plug 'preservim/nerdtree'
call plug#end()
