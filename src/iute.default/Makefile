all:
	cat Makefile
	@echo ""
	@echo "Don't forget to change the version number in setup.py and version.txt (profiles/default/metadata.xml changes only if the generic setup changed)"

clean:
	rm -rf build dist

egg:
	python2.4 setup.py bdist_egg

dist4:
	python2.6 setup.py sdist upload -r ourbasket
