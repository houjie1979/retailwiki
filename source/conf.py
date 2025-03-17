# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RetailWiki'
copyright = '2025, jiehou'
author = 'jiehou'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_simplepdf','docxbuilder']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme' # default:alabaster
html_static_path = ['_static']
html_css_files=[
    'css/custom.css',
]
html_theme_options = {
    # 'collapse_navigation': False,  # 确保导航栏不会折叠
    # 'navigation_depth': 4,        # 导航栏的深度
    # 'includehidden': True,        # 显示隐藏的文档
    # 'collapse_navigation': False,  # 确保导航栏不会折叠
    # 'titles_only': False,         # 显示完整的目录结构，而不仅仅是标题
    # 'sidebar_localtoc': True,     # 在左侧导航栏中显示当前页面的目录    
}