=========================
"New" Objects in Problems
=========================

`This 3b1b video <https://www.youtube.com/watch?v=OkmNXy7er84>`_ points out a
nice heuristic for how to find solutions to a general problem.

The "source" problem there is about randomly choosing points on a sphere and
asking what the probability is that the induced tetrahedron contains the center
of the sphere.

But the "algorithm" to find a solution is nice:

    * Simplify the problem to a simpler environment (2D circles and triangles
      in this case)

    * In that environment, notice that a new object simplifies the way to view
      the problem (in this case, noticing that instead of considering 3 random
      points, consider 2 random *lines* being drawn through the circle, and
      then an assignment of 2 base points from the 4 possible intersection
      points, and therefore to the answer of 1/4 probability)

    * Regeneralize to the initial environment


In short: simplify, then notice whether a new object is used, then recast the
problem in terms of the new object, then re-generalize the recasted problem.

Also -- combinatorics is great.
