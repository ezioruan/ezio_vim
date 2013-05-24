vimball.rb
==========

The vimball.rb ruby script that allows user to create, install, and list 
the contents of 
[vimballs](http://www.vim.org/scripts/script.php?script_id=1502).


Configuration
-------------

Configuration is done via yaml files:

* `VIMFILES/vimballs/config_${hostname}.yml`
* or `VIMFILES/vimballs/config.yml`

Example configuration file:

    --- 
    vimfiles: /home/foo/.vim/
    installdir: /home/foo/.vim/
    compress: false
    helptags: gvim --cmd "helptags %s|quit"
    username: foo
    password: bar
    history_fmt: Please see http://github.com/foo/%s_vim/commits/master/
    ignore_git_messages_rx: ^- (readme|docs|misc|meta|etc|minor)$
    roots:
      - /home/foo/.vim/bundle


Examples
--------

Create a vimball:

    vimball.rb vba myplugin.recipe

Create vimballs if a file has changed:

    vimball.rb -u vba myplugin.recipe

Create a vimball and upload it to vim.org with 
[vimscriptuploader.rb](http://github.org/tomtom/vimscriptuploader.rb):

    rm myplugin.yml || echo ignore error
    if vimball.rb -u --save-yaml -- vba myplugin.recipe | grep "vimball: Save as"; then
        vimscriptdef.rb --recipe myplugin.recipe
        vimscriptuploader.rb --user foo --password bar myplugin.yml
    fi

Install a vimball:

    vimball.rb install myplugin.vba

Install a vimball as a "bundle" (i.e. in its own directory under 
`~/.vim/bundle`):

    vimball.rb --repo install myplugin.vba


Dependencies
------------

* ruby 1.8


<!-- 2010-11-01; @Last Change: 2010-11-01. -->
<!--
vi: ft=markdown:tw=72:ts=4
-->
