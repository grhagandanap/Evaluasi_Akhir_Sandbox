# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import django

sys.path.insert(0, os.path.abspath('..'))
os.environ["DJANGO_SETTINGS_MODULE"] = "tugasakhir.settings"
django.setup()

project = 'Evaluasi Akhir Sandbox'
copyright = '2025, Grha Gandana Putra'
author = 'Grha Gandana Putra'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon', 
              'sphinx.ext.viewcode']

templates_path = ['_templates']
# Exclude patterns: Add these for nested migrations and generated RSTs
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'venv',
    '__pycache__',
    # Exclude any migrations dirs recursively (catches eas/migrations, etc.)
    '**/migrations',
    # Also exclude any generated .rst files for migrations modules
    '**/migrations.*.rst',
    '**/eas.migrations.*',
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
