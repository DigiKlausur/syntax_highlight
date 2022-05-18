import os
from IPython.core.magic import register_cell_magic
from IPython import get_ipython


try:

    @register_cell_magic
    def syntax(line, cell):
        return None

except:
    pass


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
