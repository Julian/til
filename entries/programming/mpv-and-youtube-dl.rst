==========================
``mpv`` and ``youtube-dl``
==========================

``mpv`` and ``youtube-dl`` can talk directly to each other.

Specificaly:

.. code-block:: sh

   $ mpv --ytdl-format=bestaudio ytdl://ytsearch:'think about things'

will immediately start ``mpv`` off playing the audio results of the
``youtube-dl`` search.
