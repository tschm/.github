# .github

Reusable workflows for cvxgrp

[Workflows](https://docs.github.com/en/actions/using-workflows/creating-starter-workflows-for-your-organization#creating-a-starter-workflow)

## Action workflows

Github workflows can help to robustify and to automate the process of creating software and documents.
We recommend to [Github introduction](https://docs.github.com/actions).

We go through an incomplete list of example actions created for cvxgrp:

### latex

### release

### [setup-environment](https://github.com/cvxgrp/.github/blob/main/actions/setup-environment/action.yml)

This workflow installs python and poetry. It then proceeds to construct the virtual environment using poetry.
It can rely on cached versions of the virtual environment.

### [sphinx](https://github.com/cvxgrp/.github/blob/main/actions/sphinx/action.yml)

This workflow builds a sphinx documentation based on your docstrings. 

### test

