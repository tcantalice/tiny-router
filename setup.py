from setuptools import setup, find_packages

__name__ = 'tiny_router'
__version__ = '0.1.dev0' # TODO: Adopt a standard versioning

__author__ = 'Tarcisio Cantalice'
__author_email__ = 'tarcisiocantalice@gmail.com'

__requirements__ = ['flask']

with open('README.md', 'r') as readme:
    __long_description__ = readme.read()

__license__ = 'GNU GPLv3'
setup(
    name=__name__,
    version=__version__,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=__requirements__,
    author=__author__,
    author_email=__author_email__,
    long_description=__long_description__,
    license=__license__,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Flask',
        'License :: GNU GLPv3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)