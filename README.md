# .github

Reusable workflows for cvxgrp

[Workflows](https://docs.github.com/en/actions/using-workflows/creating-starter-workflows-for-your-organization#creating-a-starter-workflow)

## :warning: 
Be careful when using actions in private repositories. The group has a limited number of minutes per month.
In public repositories, actions are free. 

## Poetry

To take full advantage of those actions we recommend moving to [poetry](https://python-poetry.org/).
Poetry is a python package manager that allows to create virtual environments and to manage dependencies.
It is also a build tool that can be used to create packages and to run tests. 

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

In this folder create a yml file with the name of the workflow you want to use, e.g. basic.yml.

```yaml
name: "basic"

on:
  push:

jobs:
  basic:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - uses: pre-commit/action@v3.0.0
    - uses: cvxgrp/.github/actions/test@main
```

Every push to the repository will trigger the workflow. 
It will run all jobs in the workflow. The first job is called basic. It will run on a ubuntu machine.
The steps are the actions that will be executed. The first step is to checkout the repository. 
The second step is to run the pre-commit action. The third step is to run the cvxgrp test action defined in 
this repository.

There are many more examples of such workflow files in the repositories:
* 
* [cvxmarkowitz](https://github.com/cvxgrp/cvxmarkowitz/tree/main/.github/workflows)
* [cvxsimulator](https://github.com/cvxgrp/simulator/tree/main/.github/workflows)

Note the strong overlap between both projects. The jobs are essentially all the same.

For paper repository we use the LaTeX workflow. For an example

* [cov_pred_finance](https://github.com/cvxgrp/cov_pred_finance_paper/tree/main/.github/workflows)

