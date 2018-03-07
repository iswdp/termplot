import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "termplot",
    version = "0.0.2",
    author = "William Powell",
    author_email = "iswdp@hotmail.com",
    description = ("A simple terminal plotting package."),
    license = "MIT",
    keywords = "terminal plotting plot plotter bar graph bargraph",
    url = "https://github.com/iswdp/termplot",
    packages=['termplot'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: MIT License",
    ],
)