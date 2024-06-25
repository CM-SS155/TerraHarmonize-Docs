# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import sphinx_pdj_theme

# sys.path.insert(0, os.path.abspath('E:\Satsure\SAGE\codes\PYTHON\codes-part2\Packaging_class\src\TerraHarmonize'))

def setup(app):
    app.add_css_file('my_style.css')

project = 'TerraHarmonize'
copyright = '2024, chandramohan'
author = 'chandramohan'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    
    ]

autodoc_typehints = 'none'
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


if os.getenv('READTHEDOCS'):
    html_build_dir = os.environ.get('READTHEDOCS_OUTPUT', '_build/html')
    # html_output_dir = os.getenv('READTHEDOCS_OUTPUT', '_build/html')

# html_build_dir = os.environ.get('READTHEDOCS_OUTPUT', '_build/html')
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
# html_theme_path = [sphinx_pdj_theme.get_html_theme_path()]
html_static_path = ['_static']
html_show_sourcelink = False
