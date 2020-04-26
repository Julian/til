=======
Firefox
=======

Copying to the Clipboard from the Console
-----------------------------------------

The Firefox Dev Tools console defines a ``copy()`` function which will copy
text to the clipboard.

For some reason, using ``navigator.clipboard.writeText("asdf")``, which `seems
to be the normal way to do this
<https://developer.mozilla.org/en-US/docs/Web/API/Clipboard/writeText>`_ fires
a rejected promise. Probably something to do with the console environment being
different and weird, or me not understanding the `permissions API
<https://developer.mozilla.org/en-US/docs/Web/API/Permissions_API/Using_the_Permissions_API>`_.
