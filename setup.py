#!/usr/bin/env python

from setuptools import setup


setup(
    name='pytest-patch',
    version='0.2.1',
    author='Igor Kaplounenko',
    author_email='icarus.aquinas.mj12@gmail.com',
    maintainer='Igor Kaplounenko',
    maintainer_email='icarus.aquinas.mj12@gmail.com',
    license='MIT',
    url='https://github.com/IcarusMJ12/pytest-patch',
    description='An automagic `patch` fixture that can patch '
                'objects directly or by name.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    py_modules=['pytest_patch'],
    python_requires='>=3.7',
    install_requires=['pytest>=7.0.0', 'mock'],
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
    entry_points={
        'pytest11': [
            'patch = pytest_patch',
        ],
    },
)
