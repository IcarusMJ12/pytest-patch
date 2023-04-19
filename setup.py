#!/usr/bin/env python

from setuptools import setup


setup(
    name='pytest-patch',
    version='0.1.0',
    author='Igor Kaplounenko',
    author_email='megawidget@gmail.com',
    maintainer='Igor Kaplounenko',
    maintainer_email='megawidget@gmail.com',
    license='MIT',
    url='https://github.com/megawidget/pytest-patch',
    description='An automagic `patch` fixture that can patch '
                'objects directly or by name.',
    long_description=open('README.md').read(),
    py_modules=['pytest_patch', 'pytest_patch_testmodule'],
    python_requires='>=3.5',
    install_requires=['pytest>=3.5.0', 'mock'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'patch = pytest_patch',
        ],
    },
)
