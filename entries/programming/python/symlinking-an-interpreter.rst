==================================
Symlinking Python (3) Interpreters
==================================

`PEP 405 <https://www.python.org/dev/peps/pep-0405/#id17>`_ introduced
a ``pyvenv.cfg`` file, useful for creating lightweight virtual
environments without the hacks done by ``virtualenv`` historically.
Doing so is much, much faster as well, since now creation of a virtual
environment is essentially just creating 2 files (one file and a symlink).

It also though changed the behavior of symlinking a Python interpreter binary.
Specifically, if you do::

    ln -s /a/python3 /some/other/directory/

then ``/some/other/directory/python`` is seen as an entirely different virtual
environment. It will have entirely different ``site-packages`` (i.e. will not
see packages installed to the original interpreter).

Full reproducer::

    $ python3.8 -m venv venv && \
      venv/bin/python -m pip install --quiet attrs && \
      echo 'in-place' && \
      venv/bin/python -c 'import attr' && \
      echo 'succeeded' && \
      ln -s venv/bin/python ./symlink && \
      echo 'symlink:' && \
      ./symlink -c 'import attr'; rm -rf venv symlink

It's unclear to me why this behavior is desireable -- to me, it seems a
lot more reasonable for the presence of a ``pyvenv.cfg`` file to
trigger the virtual environment behavior, not merely creating a symlink.
I.e., the behavior I would have expected is:

    * on startup of a Python interpreter, look for a ``pyvenv.cfg`` next
      to the absolute path of ``sys.argv[0]``

    * if you find it, this is a virtual environment, read and process it

    * otherwise, if ``sys.argv[0]`` is a symlink, ``readlink`` it and re-check
      for a ``pyvenv.cfg`` (following the behavior above) or otherwise
      terminating once a non-symlink is reached. But ``sys.argv[0]`` alone
      being a symlink does not change the isolation or behavior of the linked
      interpreter.

I'm not sure I have enough energy to investigate whether the above was
considered and/or has some critical issue I don't see, but the current
behavior is quite surprising (something I only notice now given that
``virtualenv`` just adopted it as of ``virtualenv>=20``).

If you know why the above was chosen, or want to argue it's better, let
me know :)
