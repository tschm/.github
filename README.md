# .github

Reusable workflows for cvxgrp

[Workflows](https://docs.github.com/en/actions/using-workflows/creating-starter-workflows-for-your-organization#creating-a-starter-workflow)

## Action workflows

Github workflows can help to robustify and to automate the process of creating software and documents.
We recommend to [Github introduction](https://docs.github.com/actions).

We go through an incomplete list of example actions created for cvxgrp:

### [latex](https://github.com/cvxgrp/.github/blob/main/actions/latex/action.yml)

This workflow is used to compile *.tex files. It uploads the generated documents to the draft branch.

### [release](https://github.com/cvxgrp/.github/blob/main/actions/release/action.yml)

This workflow is used to released the package to pypi. It assumes the project is built with poetry.

### [setup-environment](https://github.com/cvxgrp/.github/blob/main/actions/setup-environment/action.yml)

This workflow installs python and poetry. It then proceeds to construct the virtual environment using poetry.
It can rely on cached versions of the virtual environment. It assumes the project is built with poetry.

### [sphinx](https://github.com/cvxgrp/.github/blob/main/actions/sphinx/action.yml)

This workflow builds a sphinx documentation based on your docstrings. 

### [test](https://github.com/cvxgrp/.github/blob/main/actions/test/action.yml)

This workflow install pytest and some its friends. It uploads the test results are artifacts.
It assumes the project is built with poetry.

## Using workflows

Please follow:

* Create the '.github/workflows' folder.
  
