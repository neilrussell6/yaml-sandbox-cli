from setuptools import setup

setup(
    name='myapp',
    version='0.1',
    py_modules=['src'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        myapp=src.cli:cli
    ''',
)
