" Auto Plug
let data_dir = has('nvim') ? stdpath('data') . '/site' : '~/.vim'
if empty(glob(data_dir . '/autoload/plug.vim'))
  silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

" Show color syntax
syntax on

" Colors
set background=dark
colorscheme solarized8

" Ecoding and stuff
set encoding=utf-8
set t_Co=256
set fillchars+=stl:\ ,stlnc:\

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
nnoremap <C-;> :tabnew<cr>
nnoremap <C-'> :tabclose<cr>
nnoremap <C-[> :tabprevious<cr>
nnoremap <C-]> :tabnext<cr>

" Split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" Nerd Tree
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>

" Lightline
let g:lightline = {
      \ 'colorscheme': 'solarized',
      \ }

" coc
function! CheckBackspace() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

inoremap <silent><expr> <TAB>
      \ coc#pum#visible() ? coc#pum#next(1) :
      \ CheckBackspace() ? "\<Tab>" :
      \ coc#refresh()
inoremap <expr><S-TAB> coc#pum#visible() ? coc#pum#prev(1) : "\<C-h>"

inoremap <silent><expr> <CR> coc#pum#visible() ? coc#pum#confirm()
                              \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"
" Ale
let b:ale_fixers = {'python': ['autopep8']}

" Plugins
call plug#begin('~/.vim/plugged')
Plug 'tmhedberg/SimpylFold'
Plug 'preservim/nerdtree'
Plug 'itchyny/lightline.vim'
Plug 'ryanoasis/vim-devicons'
Plug 'joshdick/onedark.vim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'dense-analysis/ale'
Plug 'mhinz/vim-startify'
Plug 'lifepillar/vim-solarized8'
call plug#end()
