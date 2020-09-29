# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Basic usage
- type `make website` in the base dir to launch the project website
- edit project website in `docs` using markdown
- git clone your Overleaf repo to `latex`

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── analysed       <- Output of scientific ana
    │   ├── external       <- Data from third party sources.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump, can also link to server data (e.g. UPdata)
    │
    ├── docs               <- A default `mkdocs` project; see `docs/living-docs.md` for details.
    │                         The mkdocs config is in `_/mkdocs/mkdocs.yml` file. 
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`. Use git lfs to track these
    │
    ├── latex              <- Generated analysis md, PDF, LaTeX, etc. Clone your Overleaf Git here
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so scripts can be imported
    ├── scripts            <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   ├── download_data.py
    │   │   └── make_dataset.py
    │   │
    │   ├── analysis       <- Scripts to do your scientific analysis that is not visualization
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the cookiecutter scientific-publication template (based on <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">data science project</a>) by [Luke Gregor](https://github.com/luke-gregor).</small></p>
