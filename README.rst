This fork adds better support for timecodes in DFXP/TTML subs:

- frameRate and frameRateMultiplier used to create framerate value. Defaults to 30fps. Allows for fraction fps, such as 29.97fps
- reworked timestamp code for readability
- added support for "f" offset metric
- added tests for 29.97, 30fps (via default), 25fps

py-caption
==========

|Build Status|

``pycaption`` is a caption reading/writing module. Use one of the given Readers
to read content into a CaptionSet object, and then use one of the Writers to
output the CaptionSet into captions of your desired format.

Tested with Python 3.4 and 3.5.
(for Python 2 use pycaption < 1.0.0)

For details, see the `documentation <http://pycaption.readthedocs.org>`__.

Changelog
---------

1.0.0
^^^^^
- Added Python 3 support

0.5.x
^^^^^
- Added positioning support
- Created documentation

License
-------

This module is Copyright 2012 PBS.org and is available under the `Apache
License, Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`__.

.. |Build Status| image:: https://travis-ci.org/pbs/pycaption.png?branch=master
   :target: https://travis-ci.org/pbs/pycaption
