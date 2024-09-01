project = "aiocpa"
copyright = "2024, VoVcHiC"
author = "VoVcHiC"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
    "sphinxext.opengraph",
    "sphinx_autodoc_typehints",
]

templates_path = ["_templates"]

html_theme = "furo"
html_static_path = ["_static"]
html_copy_source = False
html_logo = "_static/logo.png"

ogp_site_url = "https://aiocpa.readthedocs.io/en/latest/"
ogp_site_name = "AsyncIOCryptoPayAPI documentation"
ogp_description_length = 0
ogp_social_cards = {"image_mini": "_static/rtd.ico"}

html_css_files = ["extra.css"]

html_theme_options = {
    "light_css_variables": {
        "color-header-text": "#3fa3dd",
        "color-brand-primary": "#3fa3dd",
        "color-brand-content": "#3fa3dd",
        "color-api-name": "#3fa3dd",
        "color-api-pre-name": "#3fa3dd",
        "color-link--visited": "#3fa3dd",
        "color-highlight-on-target": "#aaddff",
        "font-stack": "Inter, sans-serif",
        "font-stack--headings": "Inter, sans-serif",
    },
    "dark_css_variables": {
        "color-highlight-on-target": "#223355",
    },
}
