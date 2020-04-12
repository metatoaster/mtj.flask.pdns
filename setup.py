from setuptools import setup, find_packages
import os

version = '0.1'

classifiers = """
Development Status :: 4 - Beta
Environment :: Web Environment
Framework :: Flask
Intended Audience :: Developers
License :: OSI Approved :: GNU Affero General Public License v3
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
""".strip().splitlines()

setup(
    name='mtj.flask.pdns',
    version=version,
    description="A simple flask endpoint interface to pdns",
    long_description=(
        open('README.rst').read() + "\n" +
        open('CHANGES.rst').read()
    ),
    classifiers=classifiers,
    keywords='',
    author='Tommy Yu',
    author_email='y@metatoaster.com',
    url='https://github.com/metatoaster/mtj.flask.pdns',
    license='AGPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['mtj', 'mtj.flask'],
    zip_safe=False,
    install_requires=[
        'setuptools',
        'sqlalchemy',
        'flask',
    ],
    include_package_data=True,
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*',
    entry_points={},
    test_suite="mtj.flask.pdns.tests.make_suite",
)
