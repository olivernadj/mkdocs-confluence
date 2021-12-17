from setuptools import setup, find_packages

setup(
    name="mkdocs-confluence",
    version="0.2.2",
    description="MkDocs plugin for uploading markdown documentation to Confluence via Confluence REST API",
    keywords="mkdocs markdown confluence documentation rest python",
    url="https://github.com/olivernadj/mkdocs-confluence/",
    author="Pawel Sikora",
    author_email="sikor6@gmail.com",
    license="MIT",
    python_requires=">=3.6",
    install_requires=["mkdocs>=1.1", "jinja2"],
    packages=find_packages(),
    entry_points={"mkdocs.plugins": ["mkdocs-confluence = mkdocs_confluence.plugin:MkdocsConfluence"]},
)
