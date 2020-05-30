===
BPF
===


JIT
---

A restricted subset of C is compiled via ``clang`` to eBPF bytecode, and the
Linux kernel contains a JIT (and of course a VM) to execute it.


``bcc``
-------

`bcc <https://github.com/iovisor/bcc>`_ is a higher level toolkit for
interacting with eBPF (including via Python). For example:

.. code-block:: python

    from bcc import BPF

    BPF(
        text="""
            int kprobe__sys_clone(void *ctx) {
                bpf_trace_printk("Hello, World!\\n");
                return 0;
            }
        """,
    ).trace_print()

will attach a simple print callback whenever a new process is spawned (via
``clone(2)``).


BPF-based tools
---------------

Brendan Gregg has a great `diagram and post
<http://www.brendangregg.com/ebpf.html>`_ of the various BPF-using
tools, and which part of the stack they trace.


More Tracing
------------

Julia Evans's `Linux tracing systems & how they fit together
<https://jvns.ca/blog/2017/07/05/linux-tracing-systems/>`_ is pretty great
reading & reference for context beyond just BPF.
