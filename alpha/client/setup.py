#!/usr/bin/env python

from setuptools import setup

setup(
    name='tildemush-client',
    version='1.0.0',
    description='a modern mush primarily designed for tilde.town',
    url='https://github.com/vilmibm/tildemush',
    author='vilmibm',
    author_email='vilmibm@protonmail.ch',
    license='AGPL',
    classifiers=[
        'Topic :: Artistic Software',
        'License :: OSI Approved :: Affero GNU General Public License v3 (AGPLv3)',
    ],
    keywords='mush',
    packages=['tmclient'],
    # TODO we use a forked urwid that patches a bug which causes errors to be swallowed
    #      when using asyncio+urwid. Hopefully we can switch back to the main urwid before 
    #      too long.
    install_requires=[
        'click==6.7',
        'urwid @ https://api.github.com/repos/tildetown/urwid/tarball',
        'websockets==6.0.0',
    ],
    extras_require={
        'testing': [
            'pytest==3.5.0',
        ]
    },
    include_package_data=True,
    entry_points={
          'console_scripts': [
              'tmclient = tmclient.__init__:main',
          ]
    },
)
