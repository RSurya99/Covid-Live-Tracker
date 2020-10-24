# Covid Live Tracker

Simple website using flask to track live covid19_data

## Installation & Requirements
create virtual environment using virtualenv

```bash
virtualenv env
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flask and covid19_data.

```bash
pip install flask
pip install covid19_data
```

## Usage

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import covid19_data
```
