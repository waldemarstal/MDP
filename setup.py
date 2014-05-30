from distutils.core import setup
from setuptools import find_packages


setup(
    name='mdp',
    version='1',
    author='Waldemar Stal',
    author_email='waldemar.stal@gmail.com',
    packages=find_packages(),
    description='mdp',
    long_description='README.md',
    install_requires=[],
    entry_points="""\
    [console_scripts]
    mdp = lib.script:main
    """,
)
