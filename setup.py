from setuptools import setup, find_packages

__name__ = 'flask_router'
__version__ = '0.1.dev0' # TODO: Adopt a standard versioning

__author__ = 'Tarcisio Cantalice'
__author_email__ = 'tarcisiocantalice@gmail.com'

__requirements__ = ['flask']

__license__ = 'GNU GPLv3'

setup(
    name=__name__,
    version=__version__,
    packages=find_packages('src'),
    install_requires=__requirements__,
    author=__author__,
    author_email=__author_email__,
    license=__license__,
)