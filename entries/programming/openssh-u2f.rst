===============
U2F and OpenSSH
===============

`As of OpenSSH 8.2 <http://www.openssh.com/txt/release-8.2>`_, OpenSSH
now supports U2F for authentication.

This is a totally separate authentication mechanism entirely from say,
ED25519 host keys with a second factor; here, the U2F (e.g. Yubikey)
*is* / *has* the key on it.

To use it though, both sides (server and client) have to be recent
enough to support this form of login.
