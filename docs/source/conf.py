# Customized Sphinx configuration
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import datetime

import pkg_resources

# Project name
project = 'Strawberry'
# Project author
author = 'Stefano Pigozzi, Lorenzo Balugani'
# Project copyright
project_copyright = f'{datetime.date.today().year}, {author}'
# Project short version
version = pkg_resources.get_distribution(project.lower()).version
# Project long version
release = pkg_resources.get_distribution(project.lower()).version

# Sphinx language
language = "en"
# Sphinx extensions
extensions = [
    "sphinx.ext.intersphinx",
]

# Source files encoding
source_encoding = "UTF-8"
# Source file extensions
source_suffix = {
    ".rst": "restructuredtext",
}
# Source files parsers
source_parsers = {}

# The doc from which to start rendering
root_doc = "index"
# Files to ignore when rendering
exclude_patterns = [
    "build",
    "_build",
    "Thumbs.db",
    ".DS_Store",
]
# Sphinx template files
templates_path = [
    '_templates',
]

# Prologue of all rst files
rst_prolog = ""
# Epilogue of all rst files
rst_epilog = ""

# Default domain
primary_domain = None
# Default role
default_role = None

# Print warnings on the page
keep_warnings = False
# Display more warnings than usual
nitpicky = False

# Intersphinx URLs
intersphinx_mapping = {
    "python": ("https://docs.python.org/3.8", None),
}
# Manpages URL
manpages_url = "https://man.archlinux.org/"

# HTML builder theme
html_theme = 'sphinx_rtd_theme'
# Configuration for the theme
html_theme_options = {
    "style_nav_header_background": "#D72929",
    "github_url": "https://github.com/Steffo99/strawberry/tree/main/docs/source",
}
# Title of the HTML page
html_title = f"{project}"
# Short title of the HTML page
html_short_title = f"{project}"
# Path of the documentation static files
html_static_path = [
    "_static",
]
# Path of extra files to add to the build
html_extra_path = [
    "_extra",
]
