# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# The master toctree document.
master_doc = 'index'


# -- Project information -----------------------------------------------------

project = u'Ardupilot Cloud EcoSystem'
copyright = u'2024, Ardupilot.org (Powered by Andruav.com)'
author = u'Mohammad Said Hefny'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.imgconverter',
    #'recommonmark',
    #https://sphinxcontrib-youtube.readthedocs.io/en/latest/
    'sphinxcontrib.youtube', #For youtube embedding
    #'sphinxcontrib.vimeo', #For vimeo embedding
    'sphinx.ext.autosectionlabel'
]
# Add any paths that contain templates here, relative to this directory.
templates_path = ['']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

[extensions]
todo_include_todos=True
rst_prolog = """
.. |br| raw:: html

   <br />
"""

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    #show [+] in side menu
    "collapse_navigation" : False
}

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    './css/common_theme_override.css',
]


# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'



# A shorter title for the navigation bar.  Default is the same as html_title.
# DO NOT CHANGE. This is used by theme in "Edit on Github" links
html_short_title = 'Andruav_AP'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = './images/ardupilot_logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = './images/andruav.ico'


html_additional_pages = {
    'eula': '_static/eula.html',
    'eula_team': '_static/eula_team.html',
    'andruavweb': '_static/andruavweb.html',
}
