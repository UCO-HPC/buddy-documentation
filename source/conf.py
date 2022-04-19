# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Parts of this document are adapted from: https://github.com/godotengine/godot-docs

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'buddy-documentation'
copyright = '2022, CREIC'
author = 'CREIC'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    #'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    'sphinx_copybutton',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Syntax hilighting -------------------------------------------------------

from pygments.lexers.shell import BashLexer
from sphinx.highlighting import lexers

pygments_style = "sphinx"

# custom lexers: https://stackoverflow.com/questions/16469869/custom-syntax-highlighting-with-sphinx
# bash
lexers['bash'] = BashLexer()

# slurm
lexers['slurm_bash'] = BashLexer()


# -- Options for HTML output -------------------------------------------------

html_copy_source = False
html_show_sourcelink = False

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    # if we have a html_logo below, this shows /only/ the logo with no title text
    "logo_only": True,
    # Collapse navigation (False makes it tree-like)
    "collapse_navigation": False,
    # Scroll navigation with page
    "sticky_navigation": True,
    
}

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

#must be a png to support transparency
html_logo = "_static/img/logo.png"

html_favicon = "_static/img/favicon.ico"

# These paths are either relative to html_static_path
# or fully qualified paths (e.g. https://...)
html_css_files = [
    "css/custom.css",
]

#html_js_files = []
