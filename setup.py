from setuptools import setup

setup(
    name='yaml-sandbox-cli',
    version='0.1',
    py_modules=['src'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        yaml-sandbox-cli=src.cli:cli
    ''',
)
