from setuptools import setup,find_packages
from sys import exit
from platform import python_version

with open("README") as file:
    longdesc=file.read()

if python_version() < "3.6.0":
	exit(1)

setup(
    name="weak",
    version="1.0",
    description="WEAK Encrypts Anything Known.",
    long_description=longdesc,
    url="https://github.com/apple502j/weak",
    author="Apple502j",
    license="GPLv3",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: Japanese',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    keywords='weak encrypt string',
    packages=find_packages(),
    install_requires='',
    python_requires='>=3.6'
)
