#!/usr/bin/env python

from distutils.core import setup

setup(name='YoutubeDL',
      version='1.0',
      description='Python Youtube downloader',
      author='Renzo Westerbeek',
      author_email='renzowesterbeek@gmail.com',
      py_modules = ['YoutubeDL', 'pafy', 'ui']
      data_files=[('urlfile', ['urlfile.txt'])]
     )