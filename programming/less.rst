====
less
====


``less -S``
-----------

``-S`` will disable soft line breaks within ``less``, allowing horizontal
scrolling.


Tailing Files
-------------

Use ``less +F`` instead of ``tail -f``. It works the same, but supports
interrupting the stream with ``SIGINT`` to e.g. search around, and then can
resume tailing by hitting ``F`` again.

Doing so will even then highlight the search pattern in the future text.


``less +command``
-----------------

Passing ``+command`` will run the given command each time a new file is opened
by ``less``.


Filtering Lines
---------------

``&pattern`` will filter lines only matching the given pattern.


Opening EDITOR
--------------

Hitting ``v`` will open the file in an editor.
