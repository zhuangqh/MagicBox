# -*- coding: utf-8 -*-
# Author: zhuangqh
# Create on: 2015-10-6
# Last modify on: 2015-10-9
# setup software in a fresh installed linux

import os

# setup emacs
os.system("sudo apt-get install emacs24")
os.system("rm ~/.emacs.d -rf")
os.system("git clone http://github.com/purcell/emacs.d ~/.emacs.d")
# open emacs to config
os.system("emacs &disown")

# install chrome
os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
os.system("sudo dpkg -i google-chrome-stable_current_amd64.deb")

#install sublime-text-3
os.system("sudo add-apt-repository ppa:webupd8team/sublime-text-3")
os.system("sudo apt-get update")
os.system("sudo apt-get install sublime-text")

# swap ctrl and caps
os.system("echo 'setxkbmap -option ctrl:swapcaps' >> ~/.bashrc")


# --- install and custom zsh ---

os.system("sudo apt-get install zsh")

# set zsh for current user
os.system("chsh -s /bin/zsh")

# install oh my zsh
os.system("wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh")

# install autojump
os.system("sudo apt-get install autojump")
os.system("echo '[[ -s ~/.autojump/etc/profile.d/autojump.sh ]] && . ~/.autojump/etc/profile.d/autojump.sh' >> ~/.zshrc")
