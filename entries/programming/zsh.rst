===
zsh
===


``&|``
------

Piping using ``foo &| bar`` will pipe both stdout *and* stderr to ``bar``.


``MULTIOS``
-----------

With ``MULTIOS`` enabled, multiple outputs to the same file descriptor can be
provided, similar to using ``tee``.

In other words::

    $ date >foo >bar

will output ``date`` to both ``foo`` and ``bar``. (Piping it will also work
since it implicitly is like redirecting).


``cd old new``
--------------

``cd old new`` will substitute ``new`` into ``old``.

I.e. ``cd foo bar`` in a working directory like ``/a/b/foo/c`` will change to
``/a/b/bar/c``.


``vared``
---------

``vared SOME_ENVIRONMENT_VARIABLE`` will load the environment variable into a
line editor, with the output saved back to the environment variable.


``mailpath``
------------

``mailpath`` specifies the set of paths to look at for new mail.
