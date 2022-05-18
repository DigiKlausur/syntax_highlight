import os
from .syntax_highlight import syntax


def _jupyter_nbextension_paths():
    root = os.path.dirname(__file__)
    base_path = os.path.join(root, "nbextensions")

    paths = [
        dict(
            section="notebook",
            src=os.path.join(base_path, "syntax_highlight"),
            dest="syntax_highlight",
            require="syntax_highlight/main",
        )
    ]

    return paths


"""
def load_ipython_extension(ipython):
    ipython.register_magics(syntax)
    """
