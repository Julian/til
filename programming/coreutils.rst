=========
coreutils
=========


``cp --parents``
----------------

``mkdir -p`` will create a directory with its parents. But ``cp`` takes a
parents option as well.

``cp --parents foo/bar/baz/quux.txt some/directory`` will create
``some/directory/foo/bar/baz/quux.txt`` without any of the other
directory structure from the original location.
