=====
namei
=====

``namei(1)`` (provided by ``util-linux`` on macOS) is a nifty utility for fully
resolving symbolic links.

Given a chain of links, it will show e.g.:

.. code-block:: console


    ⊙  namei =python                                     julian@Air ●
    f: /Users/julian/.local/bin/python
    d /
    d Users
    d julian
    l .local -> /Users/julian/.dotfiles/.local
    d /
    d Users
    d julian
    d .dotfiles
    d .local
    d bin
    l python -> /Users/julian/.local/share/virtualenvs/dev/bin/python
    d /
    d Users
    d julian
    l .local -> /Users/julian/.dotfiles/.local
        d /
        d Users
        d julian
        d .dotfiles
        d .local
    d share
    d virtualenvs
    d dev
    d bin
    l python -> pypy
        - pypy

which fully walks the chain and shows its nodes.
