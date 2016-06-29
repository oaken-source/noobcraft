
from os.path import join, dirname
from setuptools import setup


setup(
    name='noobcraft',
    version='0.0.0',

    description='RTS for AI',
    long_description=open(join(dirname(__file__), 'README.md')).read(),

    packages=[
        'noobcraft',
    ],

    install_requires=[],

    test_suite='tests',
    tests_require=[
        'pytest',
    ],

    setup_requires=['pytest_runner'],
)
