from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='pyslack',
    packages=['pyslack'],
    version='0.0.1',
    license='MIT',
    install_requires=_requires_from_file('requirements.txt'),
    author='sho-gun',
    author_email='',
    url='https://github.com/sho-gun/pyslack',
    description='Push start/end notifications of Python scripts to slack channel.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='pyslack py-slack slack',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      pyslack = pyslack.__main__:main
    """,
)
