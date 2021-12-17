![PyPI](https://img.shields.io/pypi/v/mkdocs-confluence)
[![Build Status](https://travis-ci.com/olivernadj/mkdocs-confluence.svg?branch=main)](https://travis-ci.com/olivernadj/mkdocs-confluence)
[![codecov](https://codecov.io/gh/olivernadj/mkdocs-confluence/branch/master/graph/badge.svg)](https://codecov.io/gh/olivernadj/mkdocs-confluence)
![PyPI - Downloads](https://img.shields.io/pypi/dm/mkdocs-confluence)
![GitHub contributors](https://img.shields.io/github/contributors/olivernadj/mkdocs-confluence)
![PyPI - License](https://img.shields.io/pypi/l/mkdocs-confluence)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mkdocs-confluence)
# mkdocs-confluence 

MkDocs plugin that converts markdown pages into confluence markup
and export it to the Confluence page

## Setup
Install the plugin using pip:

`pip install mkdocs-confluence`

Activate the plugin in `mkdocs.yml`:

```yaml
plugins:
  - search
  - mkdocs-confluence
```

More information about plugins in the [MkDocs documentation: mkdocs-plugins](https://www.mkdocs.org/user-guide/plugins/).

## Usage

Use following config and adjust it according to your needs:

```yaml
  - mkdocs-confluence:
        host_url: https://<YOUR_CONFLUENCE_DOMAIN>/rest/api/content
        space: <YOUR_SPACE>
        parent_page_name: <YOUR_ROOT_PARENT_PAGE>
        username: <YOUR_USERNAME_TO_CONFLUENCE>
        password: <YOUR_PASSWORD_TO_CONFLUENCE>
        enabled_if_env: MKDOCS_TO_CONFLUENCE
        #verbose: true
        #debug: true
        dryrun: true
```

## Parameters:

### Requirements
- md2cf
- mimetypes
- mistune
