import os
from os.path import join as pjoin
from setuptools import setup, find_packages


def discover_nbextensions():
    src_path = "syntax_highlight"
    extension_files = []
    for (dirname, dirnames, filenames) in os.walk(pjoin(src_path, "nbextensions")):
        root = os.path.relpath(dirname, src_path)
        for filename in filenames:
            if filename.endswith(".pyc"):
                continue
            extension_files.append(pjoin(root, filename))
    return extension_files


setup_args = dict(
    name="syntax_highlight",
    version="0.1",
    packages=find_packages(),
    package_data={"syntax_highlight": discover_nbextensions()},
    description="Highlight code in notebooks via a magic",
    author="Tim Metzler",
    author_email="tim.metzler@h-brs.de",
    install_requires=["IPython"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: MIT",
        "Programming Language :: Python :: 3",
    ],
)

if __name__ == "__main__":
    setup(**setup_args)
