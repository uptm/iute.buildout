PYTHON=/Users/kim/Plone/Python-2.4/bin/python

all:
	cat Makefile

clean:
	rm -rf build dist

egg:
	$(PYTHON) setup.py bdist_egg

dist4:
	/usr/local/bin/python2.6 setup.py sdist bdist_egg upload -r ourbasket
