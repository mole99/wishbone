# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'WISHBONE System-on-Chip (SoC) Interconnection Architecture for Portable IP Cores'
copyright = '2019, WISHBONE specification authors'
author = 'WISHBONE specification authors'

# The full version, including alpha/beta/rc tags
release = 'B4.1'

master_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.wavedrom',
    'sphinx.ext.todo'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

numfig=True
numfig_format={ 'figure': "Figure %s", 'table': "Table %s", 'code-block': "Listing %s", 'section': "Section" }

todo_include_todos=True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_title = "WISHBONE B4"

wavedrom_html_jsinline = False

# -- Options Latex

latex_elements = { 'pointsize': '12pt' }

latex_documents = [
    (master_doc, 'wishbone-b4-1.tex', '', '', 'manual')
]
