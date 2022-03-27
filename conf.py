#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))
# import sphinx_bootstrap_theme


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autosectionlabel','docxbuilder']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst']

# The master toctree document.
master_doc = 'index'

# Section label prefix
# autosectionlabel_prefix_document = True


# General information about the project.
project = 'Writing samples'
copyright = '2022, Denis Mashutin'
# author = 'CMA Small Systems AB'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
#version = '006'
# The full version, including alpha/beta/rc tags.
#release = '006'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
# exclude_patterns = ['cv.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = "sphinx_book_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
templates_path = ['./_templates']
html_static_path = ['./_static']
html_logo = './_static/tpwrtr.jpg'
html_favicon = './_static/favicon.ico'
html_title = 'Writing Samples'

# Options for BOOK theme
html_theme_options = {
   "show_navbar_depth": 1,
   "toc_title": "ON THIS PAGE",
   "extra_navbar":"",
   "logo_only": True
}
html_sidebars = {
   "**": ["sidebar-logo.html", "sbt-sidebar-nav.html", "sbt-sidebar-footer.html"]
}

#This one is intended to fix the search issue
html_js_files = [ 'language_data.js']

# -- Options for DOCX BUILDER ----------------------------------------------
docx_documents = [
    ('index', 'Denis Mashutin.docx', {
        'title': '',
        'subject': '',
        'category': '',
        'keywords': '',
        'company': '',
        'contentStatus': '',
        'creator': ''
    }, True)
]
docx_style = './_word templates/4CV.docx'
# docx_pagebreak_before_section = 0
# docx_update_fields = True

def setup(app):
    app.add_css_file("custom.css")