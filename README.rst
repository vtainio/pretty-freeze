=============
pretty-freeze
=============

Pip freeze that shows detailed descriptions of the packages.

-------
Example
-------

This tool will transform your regular `pip freeze` from::

  dj-database-url==0.3.0
  dj-static==0.0.6
  Django==1.6.11
  static3==0.6.1
  wheel==0.24.0

into::

  # dj-database-url
  # License: BSD
  # Homepage: https://github.com/kennethreitz/dj-database-url
  # Author: Kenneth Reitz
  dj-database-url==0.3.0
  
  # dj-static
  # License: BSD
  # Homepage: https://github.com/kennethreitz/dj-static
  # Author: Kenneth Reitz
  dj-static==0.0.6
  
  # Django
  # License: BSD
  # Homepage: http://www.djangoproject.com/
  # Author: Django Software Foundation
  Django==1.6.11
  
  # static3
  # License: LGPL
  # Homepage: https://github.com/rmohr/static3
  # Author: Roman Mohr
  static3==0.6.1
  
  # wheel
  # License: MIT
  # Homepage: http://bitbucket.org/pypa/wheel/
  # Author: Daniel Holth
  wheel==0.24.0

-----
Usage
-----

You can run the program with::

  $ pretty-freeze

This package won't show itself in the freeze, so no unnecessary requirements will be added. You can use it with a requirements.txt file just as you would use pip freeze.

-------
Install
-------
::

  $ pip install pretty-freeze

-----
Legal
-----

This application is licensed under the `MIT License <https://github.com/Wisheri/pretty-freeze/blob/master/LICENSE>`_.
