===
BGP
===

The `Border Gateway Protocol (BGP)
<https://en.wikipedia.org/wiki/Border_Gateway_Protocol>`_ is a
fundamental routing protocol of the internet which allows big networks
("autonomous systems") to decide which paths to use to route traffic
between each other [#]_.

Specifically, given some autonomous systems which connect to others, BGP
allows systems within an autonomous system to reach systems within any
other autonomous system, even ones that are not directly connected, via
"optimal" paths.

What is Best?
-------------

Each given router speaking BGP may implement its own prioritization
algorithm for deciding on a specific path to take to a non-peered
autonomous system.

As an example, `Cisco's best path algorithm is described here
<https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/13753-25.html#anc2>`_
and cascades through a number of rule sets to choose a path.


Centrality
----------

BGP relies on some autonomous systems being directly connected and
additional non-directly connected systems then being able to forward
traffic along this path if it is considered shortest or most optimal.

The "size" or "importance" of autonomous systems is not uniform (i.e. some
systems route more traffic than others).

Specifically, `CenturyLink/Level3
<https://en.wikipedia.org/wiki/CenturyLink>`_ routes an inordinately
large amount of internet traffic relative to other autonomous systems.


Looking Glasses
---------------

A `looking glass server
<https://en.wikipedia.org/wiki/Looking_Glass_server>`_ is a
server (run by the operator of an autonomous system) which
allows introspecting the state of the BGP routing table
for that autonomous system.  E.g., `Cogent's Looking Glass
<https://www.cogentco.com/en/network/looking-glass>`_ would indicate
which paths the corresponding router would recommend or take.


.. [#] When used between external systems, it is known more explicitly as
   external BGP (eBGP), as it can also be used within an individual network
   (autonomous system) itself as a way to define how nodes reach each other.


Other Resources
---------------

There are a number of resources which rank autonomous systems via one means or
another relative to others in the global BGP infrastructure:

    * `ASRank <https://asrank.caida.org/>`_

    * `CIDR Report <https://www.cidr-report.org/as2.0/>`_
