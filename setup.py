import os
from os.path import join as pjoin
from distutils.core import setup


def discover_nbextensions():
    src_path = pjoin("nbextensions")
    extension_files = []
    for (dirname, dirnames, filenames) in os.walk(src_path):
        root = os.path.relpath(dirname, src_path)
        for filename in filenames:
            if filename.endswith(".pyc"):
                continue
            extension_files.append(pjoin(src_path, root, filename))
    return extension_files


setup(
    name="syntax highlight magic",
    version="0.1",
    packages=["syntax_highlight"],
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
