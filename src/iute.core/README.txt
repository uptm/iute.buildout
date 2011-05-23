Introduction
============
This package is used for placing utilities that can be
used across all iute plone projects.

For instance, there are many helper functions that make
normal plone type things much more simple and easier to
read.

For instance, to install dependencies for a product,
from iute.core.utils import install
install.these(['iute.default']).dependencies()

Much easier to do and read isn't it?

Take a look at the code to see how it is done.



Using iute_tools object in a product
==============
First off, make this package a dependency.

In the configure.zcml of your package do this,

	>>> <include package="iute.core" />
	
This will make sure the iute_tools is registered

Now in code you can do something like,

	>>> iute_tools = getMultiAdapter((self.context, self.request), name=u'iute_tools')
	
Or in a tal expression you can do something like this,

	>>> python:portal.restrictedTraverse('@@iute_tools')
