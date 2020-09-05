================
Units of Measure
================

The F# language has built in support for `annotating numeric values with units
<https://docs.microsoft.com/en-us/dotnet/fsharp/language-reference/units-of-measure>`_,
and for such values it appears will do some `dimensional analysis
<https://en.wikipedia.org/wiki/Dimensional_analysis>`_ and statically complain
if units are incorrect.

It's unclear if there's a large benefit in having this functionality in
the core language rather than a library, which is more common across
other languages, but anecdotally in those other languages (e.g. Python)
it certainly isn't common to use these libraries in arbitrary code.
