from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mkdocs-confluence",
    version="0.2.3.dev3",
    description="MkDocs plugin for uploading markdown documentation to Confluence via Confluence REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="mkdocs markdown confluence documentation rest python",
    url="https://github.com/olivernadj/mkdocs-confluence/",
    author="Oliver Nadj",
    author_email="mr.oliver.nadj@gmail.com",
    license="MIT",
    python_requires=">=3.6",
    install_requires=["mkdocs>=1.1", "jinja2"],
    packages=find_packages(),
    entry_points={"mkdocs.plugins": ["mkdocs-confluence = mkdocs_confluence.plugin:MkdocsConfluence"]},
)
