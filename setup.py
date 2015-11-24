from os.path import join, dirname

from setuptools import setup, find_packages

from version import get_version

setup(
    name='miss',
    version=get_version(),
    description='A collection of generic functions and classes',
    author='Changaco',
    author_email='changaco@changaco.oy.lc',
    url='https://github.com/Changaco/python-miss',
    license='LGPLv3+',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
)
