#-* coding:UTF-8 -*
#!/usr/bin/env python

import os

here = os.path.dirname(__file__)

vim_dictory = os.path.abspath(os.path.join(here,'_vim'))
vimrc_file = os.path.abspath(os.path.join(here,'_vimrc'))

home = os.environ['HOME']
user_vim_dictory = os.path.abspath(os.path.join(home,'.vim/'))
user_vim_rc = os.path.abspath(os.path.join(home,'.vimrc'))

if os.path.islink(user_vim_dictory):
    print('%s exists, will be detele' % user_vim_dictory)
    os.unlink(user_vim_dictory)
if os.path.islink(user_vim_rc):
    print('%s exists, will be delete' % user_vim_rc)
    os.unlink(user_vim_rc)




print(vim_dictory,user_vim_dictory)
os.symlink(vim_dictory,user_vim_dictory)
print('success to install vim')
os.symlink(vimrc_file,user_vim_rc)
print('success to install vimrc')











