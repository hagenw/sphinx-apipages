from datetime import date

import toml

import audeer


config = toml.load(audeer.path("..", "pyproject.toml"))


# Project -----------------------------------------------------------------
project = config["project"]["name"]
copyright = f"2023-{date.today().year} audEERING GmbH"
author = ", ".join(author["name"] for author in config["project"]["authors"])
version = audeer.git_repo_version()
title = project


# General -----------------------------------------------------------------
master_doc = "index"
source_suffix = ".rst"
exclude_patterns = [
    "api-src",
    "build",
    "tests",
    "Thumbs.db",
    ".DS_Store",
]
pygments_style = None
extensions = [
    "sphinx.ext.napoleon",  # support for Google-style docstrings
    "sphinx_autodoc_typehints",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_apipages",
]

napoleon_use_ivar = True  # List of class attributes

# Exclude all non-generated files from autosummary
# to skip `usage.rst`
autosummary_generate = []

intersphinx_mapping = {
    "audb": ("https://audeering.github.io/audb/", None),
}
linkcheck_ignore = [
    "https://www.sphinx-doc.org/",
]

# HTML --------------------------------------------------------------------
html_theme = "sphinx_audeering_theme"
html_theme_options = {
    "display_version": True,
    "footer_links": False,
    "logo_only": False,
}
html_context = {
    "display_github": True,
}
html_title = title
