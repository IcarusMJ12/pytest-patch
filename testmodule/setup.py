#!/usr/bin/env python

from setuptools import setup


setup(
    name='pytest-patch-testmodule',
    version='0.2.0',
    author='Igor Kaplounenko',
    author_email='megawidget@gmail.com',
    maintainer='Igor Kaplounenko',
    maintainer_email='megawidget@gmail.com',
    license='MIT',
    url='https://github.com/megawidget/pytest-patch',
    description='Test module for pytest-patch',
    py_modules=['pytest_patch_testmodule'],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
)
