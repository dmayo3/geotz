import os

project = "geotz"

release = "0.1"
version = "0.1.0"

extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

html_theme = "sphinx_rtd_theme"

doctest_global_setup = """
import geotz
"""

data_file = "../geotz/data/geonames_all_countries_sorted.tsv"
if not os.path.exists(data_file):
    raise ValueError(
        f"ERROR: need to ensure {data_file} is extracted by running `tox -e extract_data`",
    )
