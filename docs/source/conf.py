# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sys
import os
from os.path import abspath, join, dirname
sys.path.insert(0, abspath(join(dirname(__file__))))

# -- RTD configuration ------------------------------------------------
# onRtd is whether we are on readthedocs.org
onRTD = os.environ.get('READTHEDOCS')
# This is used for linking the same version of the documentation through multiple projects
rtdVersion = os.environ.get('READTHEDOCS_VERSION', 'latest')
if rtdVersion not in ['stable', 'latest', 'develop']:
  rtdVersion = 'stable'


# -- Project information -----------------------------------------------------
project = 'Statistical Data and Metadata eXchange - sdmx-im'
copyright = '2019, sdmx-twg'
author = 'sdmx-twg'
# The short X.Y version
version = '0.1'
# The full version, including alpha/beta/rc tags
release = '0.0.1'

# The master toctree document.
master_doc = 'index'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinxcontrib.plantuml',
    'sphinx.ext.intersphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# enable the figure, table ... numbering
numfig=True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'sdmx-imdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'sdmx-im.tex', 'sdmx-im Documentation', 'sdmx-twg', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'sdmx-im', 'sdmx-im Documentation', [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------
# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'sdmx-im', 'SDMX Information model', author,
     'sdmx-im', 'SDMX Information model.', 'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------
# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------
# -- Options for plandUML command line setup ---------------------------------
# headless            @see: https://github.com/readthedocs/readthedocs.org/issues/3885
# os environment var  @see: https://docs.readthedocs.io/en/stable/builds.html#build-environment
#                     @see: https://docs.readthedocs.io/en/stable/guides/environment-variables.html
if onRTD:
  print ('**Building done on readthedocs container... ')
  plantuml = 'java -Djava.awt.headless=true -jar /usr/share/plantuml/plantuml.jar -config ../plantuml.conf'
else:
  print ('**Building done locally... ')
  plantuml = 'java -Djava.awt.headless=true -jar C:/Users/Leroy/Documents/dev/sdmx/plantuml.jar -config ../plantuml.conf'

plantuml_output_format = 'png'
plantuml_syntax_error_image = True


# -- Options for intersphinx extension ---------------------------------------
# @see: http://www.virtualroadside.com/blog/index.php/2017/01/14/integrated-subproject-sites-on-readthedocs-org/
# Checking objects.inv content (debugging):
# > python -msphinx.ext.intersphinx https://sdmx-ml.readthedocs.io/en/develop/objects.inv
# please do not include final '/' so the sidebar generation works correctly.
# FIXME: correct sidebargen script to remove double '//' occurences if final '/' is forgotten below.
intersphinx_mapping = {
    'sdmx-ml': ('http://docs.sdmx.org/projects/sdmx-ml/en/%s' % rtdVersion, None),
}


# -- sidebar generation ------------------------------------------------------
# uses intersphinx definitions
from sidebarGenerator import SidebarGenerator

s = SidebarGenerator(globals(), "sdmx-im")

s.toctree("Technical Specification", 3) \
  .sdmxLocalToc("Framework", "Sections/Section1/SDMX_2-1_SECTION_1_Framework") \
  .sdmxLocalToc("Information Model", "Sections/Section2/SDMX_2_1_SECTION_2_InformationModel") \
  .newLine()

s.toctree("Formats") \
  .subPrjToc("sdmx-ml", "SDMX ML")  \
  .subPrjToc("sdmx-csv", "SDMX CSV (TBD)")  \
  .subPrjToc("sdmx-json", "SDMX JSON (TBD)")  \
  .newLine()

s.toctree("Web service APIs") \
  .subPrjToc("sdmx-rest", "ReST API")  \
  .subPrjToc("sdmx-soap", "SOAP API")  \
  .newLine()

s.toctree("Tools & applications") \
  .subPrjToc("sdmx-tck", "TCK")  \
  .newLine()

#s.toctree("Older versions") \
#  .subPrjToc("sdmx-ml-v2_1", "SDMX-ML v2.1")  \
#  .subPrjToc("sdmx-ml-v2_0", "SDMX-ML v2.0")  \
#  .newLine()

s.writeIfChanged("_sidebar.rst.inc")
