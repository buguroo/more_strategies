from setuptools import setup, find_packages
import os
import sys


HERE = os.path.abspath(os.path.dirname(__file__))
README_PATH = os.path.join(HERE, 'README.rst')
CHANGELOG_PATH = os.path.join(HERE, 'CHANGELOG')

if sys.version_info.major == 3 and sys.version_info.minor == 4:
    README = open(README_PATH, encoding='utf-8').read()
    CHANGELOG = open(CHANGELOG_PATH, encoding='utf-8').read()
else:
    raise RuntimeError('Wrong Python version')


setup(
    name='more_strategies',
    version='0.0.1rc1',
    description='Util strategies for hypothesis.',
    long_description=README + '\n\n' + CHANGELOG,
    keywords='strategies, hypothesis',
    author='Samuel Herrero',
    author_email='sherrero@buguroo.com',
    packages=find_packages('more_strategies', exclude=["tests", "docs"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "hypothesis==1.6.1",
    ],
)
