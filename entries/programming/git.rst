===
Git
===

*git you magnificent beast...*


Finding the History of a Function or Object
-------------------------------------------

``log -L :foo`` will show you the history of the function/object called
``foo``. This is a smarter version of normal ``log -L`` which just knows about
lines.

But because I'm lazy to even type this out, I made `git pylog
<https://github.com/Julian/dotfiles/blob/master/bin/git-pylog>`_ to just
be able to type ``g pylog foo.bar.baz`` and find the history of the FQON
there.


Finding Commits by Message
--------------------------

``git show :/foo`` will find the last commit whose message contains ``foo``.
It accepts a regex.

Specifically, ``git show :^Merge`` should generally find the last merge commit.


Showing Various Parts of a Merge Conflict
-----------------------------------------

``git show :N:foo.txt`` will show foo.txt from "stage" number N, which is
useful during conflict resoluton.


Custom Bisect Terms
-------------------

Using ``git bisect good`` sometimes hurts my brain if "good" isn't the
right term for the commit being marked. ``git bisect`` however has
``--term-old`` and ``--term-new`` arguments for changing ``good`` and
``bad`` to whatever you want, so e.g.:

.. code-block:: sh

    $ git bisect start --term-old fast --term-new slow

will allow using ``git bisect fast`` and ``git bisect slow`` instead
for the current bisection (e.g. for finding commits which introduced
performance issues).


``git name-rev``
----------------

``name-rev`` can append info about the position of a commit relative to tags.

It can do this even interspersed in other prose text.

E.g., given say a comment saying:

    I think this bug was caused by dc9061e8ffb5002e33688ae97d0d953818e89bae
    and fixed in d099d7e84d1ce3cf9737e9785be339c917f4a3e3.

piping that to ``git name-rev --stdin`` will output:

    I think this bug was caused by dc9061e8ffb5002e33688ae97d0d953818e89bae
    (v1.0.0~2) and fixed in d099d7e84d1ce3cf9737e9785be339c917f4a3e3 (v1.0.1).

See its man page for more stuff.


Tags Matching a Pattern
-----------------------

``git tag -l`` doesn't just list all tags, it can take a pattern and show only
matching ones, e.g.::

    $ g tag -l v*

for showing version tags.


``git shortlog``
----------------

``shortlog`` gives a nice summarized version of the log, e.g. for release
notes.


Listing or Looping Over Revisions
---------------------------------

``git for-each-ref`` will loop over given revisions.

``git rev-list`` will simply list them (in reverse order).


Sending Patches Over Email
--------------------------

``format-patch`` turns commits into patches as a file, and formatted for
sending via email or applying with ``git am``.


Rebasing... All the Way
-----------------------

``rebase -i --root`` will rebase all the way to the empty tree (e.g.
will allow ``fixup``ing something onto the very first commit in a
repo).
