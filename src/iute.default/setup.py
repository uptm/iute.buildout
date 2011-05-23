from setuptools import setup, find_packages
import os

version = '0.4.4'

setup(name='iute.default',
      version=version,
      description="default settings for iute plone sites",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://plone-ve.googlecode.com/svn/trunk/PloneEduIUTE/src/iute.default',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['iute'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'iute.requirements>=0.2b1',
        'iute.core>=0.3.4b1',
        'plone.browserlayer'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
