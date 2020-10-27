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
    │   ├── raw            <- The original, immutable data dump, can also link to local server data
    │   ├── in             <- The final, canonical data sets for modeling.
    │   ├── out            <- Output of scientific ana
    │   ├── validation     <- Data from third party sources for validation
    │   └── models         <- Machine learning models (delete if not necessary)
    │
    ├── docs               <- A default `mkdocs` project; see `docs/living-docs.md` for details.
    │                         The mkdocs config is in `mkdocs.yml` file. This forms the 
    │
    ├── notebooks          <- Jupyter notebooks. 
    │
    ├── latex              <- Generated analysis md, PDF, LaTeX, etc. Clone your Overleaf Git here 
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`. Run `make requirements`
    │                         to install dependencies in existing environment. Run `make environment`
    │                         to create a new environment using conda. 
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so scripts can be imported
    │                         using `import scripts`
    │
    ├── scripts            <- Source code for use in this project.
    │   ├── __init__.py    <- Makes scripts a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   ├── downloads  <- Directory where download scripts are kept. Data might not be saved to
    │   │   │                 the project/publication directory. Usernames and passwords for  
    │   │   │                 should be stored in the `.env` file. 
    │   │   └── make_dataset.py
    │   │
    │   ├── analysis       <- Scripts to do your scientific analysis that is not visualization
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions if it is a machine learning project. Otherwise,
    │   │   │                 delete this folder. 
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the cookiecutter scientific-publication template (based on <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">data science project</a>) by [Luke Gregor](https://github.com/luke-gregor).</small></p>
