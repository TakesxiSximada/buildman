#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import (
    setup,
    find_packages,
    )

src = 'src'
here = lambda path: os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
get_requires = lambda path: open(here(path), 'rt').readlines()

readme_path = here('README.rst')

requirements_txt = 'requirements/install.txt'
install_requirements = get_requires(requirements_txt)
test_requirements = get_requires('requirements/test.txt')


def find_version():
    for root, dirs, files in os.walk(here(src)):
        for filename in files:
            if filename == 'version.txt':
                version_file = os.path.join(root, filename)
                with open(version_file, 'rt') as fp:
                    for line in fp:
                        line = line.strip()
                        if line:
                            return line
    raise ValueError('unkown version')

version = find_version()

setup(
    name='buildman',
    version=version,
    url='https://github.com/TakesxiSximada/buildman',
    download_url='https://github.com/TakesxiSximada/buildman/master.zip',
    license='See http://www.python.org/3.4/license.html',
    author='TakesxiSximada',
    author_email='takesxi.sximada@gmail.com',
    description="zc.buildout helper",
    long_description=open(readme_path, 'rt').read(),
    zip_safe=False,
    classifiers=[  # see: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        ],
    platforms='any',
    packages=find_packages(src),
    package_dir={'': src},
    namespace_packages=[
        ],
    package_data={},
    include_package_data=True,
    install_requires=install_requirements + test_requirements,
    tests_requires=test_requirements,
    entry_points='''
    [console_scripts]
    '''
    )
