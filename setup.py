from setuptools import setup

setup(
    name='simbrief-commandline-app',
    install_requires=[
        'requests==2.24.0',
    ],
    py_modules=[
        'config',
        'simbrief',
    ],
)
