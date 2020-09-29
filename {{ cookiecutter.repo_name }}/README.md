{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── analysed       <- Output of scientific ana
    │   ├── external       <- Data from third party sources.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump, can also link to server data (e.g. UPdata)
    │
    ├── docs               <- A default `mkdocs` project; see `writing/markdown/README.md` for details.
    │                         Only contains the `mkdocs.yml` file. Serve the website with `mkdocs serve` 
    │                         from the `docs` folder. 
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`. Use git lfs to track these
    │
    ├── writing            <- Generated analysis md, PDF, LaTeX, etc.
    │   ├── manuscript     <- Can be where you store your LaTeX manuscript and can also be a 
    │   │                     subgit directory from Overleaf. First create the document on 
    │   │                     overleaf and then clone to ./writing. Rename the folder to whatever 
    │   │                     you like. 
    │   ├── markdown       <- Markdown files that will be used in the creation of docs. Website 
    │   │                     will be built with the folder structure intact. 
    │   └── manuscript     <- Can be where you store your LaTeX manuscript and can also be a
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
    │   ├── docs           <- Scripts that are used to create documentation from markdown
    │   │   └── sphinx_index.py
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
