=========
coreutils
=========

``less +F``
-----------

Use ``less +F`` instead of ``tail -f``. It works the same, but supports
interrupting the stream with ``SIGINT`` to e.g. search around, and then can
resume tailing by hitting ``F`` again.

Doing so will even then highlight the search pattern in the future text.


``cp --parents``
----------------

``mkdir -p`` will create a directory with its parents. But ``cp`` takes a
parents option as well.

``cp --parents foo/bar/baz/quux.txt some/directory`` will create
``some/directory/foo/bar/baz/quux.txt`` without any of the other
directory structure from the original location.
