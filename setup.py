###############################################################################
##
##  Copyright (C) 2014 Greg Fausak
##
##    This file is part of abroute.
##
##    abroute is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    abroute is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with abroute.  If not, see <http://www.gnu.org/licenses/>.
##
###############################################################################

from __future__ import absolute_import
from glob import glob
from setuptools import setup, find_packages

LONGSDESC = """
abroute|Autobahn experiments in router to router delivery

More information:

* `abroute Site <http://github.com/lgfausak/abroute>`__
"""

## get version string from "__init__.py"
## See: http://stackoverflow.com/a/7071358/884770
##
import re
VERSIONFILE="abroute/__init__.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
   verstr = mo.group(1)
else:
   raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


## Now install abroute ..
##
setup(
   name = 'abroute',
   version = verstr,
   description = 'Autobahn based router networking.  Connect Autobahn routed networks together.',
   long_description = LONGSDESC,
   license = 'GNU AFFERO GENERAL PUBLIC LICENSE',
   author = 'Greg Fausak',
   author_email = 'lgfausak@gmail.com',
   url = 'https://github.com/lgfausak/abroute',
   platforms = 'Any',
   install_requires = ['autobahn==0.9.3', 'twisted>=14.0.2', 'sqlbridge[postgres]>=0.1.44', 'sqlauth>=0.0.0'],
   entry_points = {
      'console_scripts': [
         'abroute = abroute.scripts.abroute:run',
      ]},
   packages = find_packages(),
   include_package_data = True,
   package_data = {
       ".": [ "LICENSE" ]
   },
   data_files=[('abroute', glob('config/*.conf') + glob('config/*.sql'))],
   zip_safe = True,
   ## http://pypi.python.org/pypi?%3Aaction=list_classifiers
   ##
   classifiers = ["License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
                  "Development Status :: 2 - Pre-Alpha",
                  "Environment :: No Input/Output (Daemon)",
                  "Framework :: Twisted",
                  "Intended Audience :: Developers",
                  "Operating System :: OS Independent",
                  "Programming Language :: Python",
                  "Programming Language :: Python :: 2",
                  "Programming Language :: Python :: 2.6",
                  "Programming Language :: Python :: 2.7",
                  "Programming Language :: Python :: Implementation :: CPython",
                  "Programming Language :: Python :: Implementation :: PyPy",
                  "Programming Language :: Python :: Implementation :: Jython",
                  "Topic :: Internet",
                  "Topic :: Internet :: WWW/HTTP",
                  "Topic :: Communications",
                  "Topic :: System :: Distributed Computing",
                  "Topic :: Software Development :: Libraries",
                  "Topic :: Software Development :: Libraries :: Python Modules",
                  "Topic :: Software Development :: Object Brokering"],
   keywords = 'autobahn websocket wamp rpc pubsub twisted database sql postgres mysql sqlite network message routing'
)
