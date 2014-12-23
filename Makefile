##############################################################################
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
##############################################################################
MODULE=abroute
TFILE=/tmp/make_$$.tmp
VFILE=$(MODULE)/__init__.py
VNUM=/tmp/vnum_$$.tmp

all:
	echo 'done'

#
# this will increment the __version__ number in the module's __init__.py file
#
incver:
	( grep -v '^__version__' $(VFILE); nv=`(cat $(VFILE); echo 'p = __version__.split(".")'; echo 'p[len(p)-1]=str(int(p[len(p)-1])+1)'; echo 'print ".".join(p)';)   | python`; echo '__version__ = "'$$nv'"') > $(TFILE); mv $(TFILE) $(VFILE)

#
# this will increment the __version__ number in the module's __init__.py file
# also, the file will be uploaded to pypi with the new version
#
pypi:
	( cd config; make )
	( grep -v '^__version__' $(VFILE); nv=`(cat $(VFILE); echo 'p = __version__.split(".")'; echo 'p[len(p)-1]=str(int(p[len(p)-1])+1)'; echo 'print ".".join(p)';)   | python`; echo '__version__ = "'$$nv'"'; echo $$nv > $(VNUM)) > $(TFILE); mv $(TFILE) $(VFILE)
	python setup.py sdist upload
	git commit -m 'sync with pypi version: '`cat $(VNUM)` .
	git push

#
# register, only do this once per project
#
register:
	python setup.py register
