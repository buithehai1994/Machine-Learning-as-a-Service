# at2_ml_as_a_service_experiments

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

A short description of the project.

## Project Organization

```
at2_ml_as_a_service/
├── data/                         <- Directory for datasets.
│   └── processed/                <- Folder for processed data.
│       └── text.txt              <- Processed data file (now deleted).
│
├── docs/                         <- Documentation files (e.g., for mkdocs).
│
├── models/                       <- Directory for storing trained models.
│   ├── forecasting/              <- Models related to forecasting.
│   │   ├── prophet.pkl           <- Trained Prophet model.
│   │   ├── prophet_event.pkl     <- Prophet model incorporating event data.
│   │   ├── prophet_holiday.pkl   <- Prophet model for holiday-specific data.
│   │   ├── prophet_month.pkl     <- Prophet model for monthly forecasting.
│   │
│   └── predictive/               <- Models related to predictive tasks.
│       ├── predictive_lgbm.pkl   <- LightGBM model for predictive tasks.
│       └── .gitkeep              <- File to ensure the directory is versioned in Git.
│
├── notebooks/                    <- Directory for Jupyter notebooks.
│   ├── forecasting/              <- Forecasting-related notebooks.
│   │   └── thehai_bui-24683423-forecasting-prophet.ipynb   <- Prophet forecasting notebook.
│   │
│   └── predictive/               <- Predictive modeling notebooks.
│       └── thehai-bui-24683423-predictive-lgbm.ipynb       <- LightGBM predictive modeling notebook.
│
├── references/                   <- Resources like data dictionaries or manuals.
│
├── reports/                      <- Reports, such as analysis results or visualizations.
│
├── src/                          <- Source code for data preparation and modeling.
│   └── preparation.py            <- Script for data preparation
│
├── .gitignore                    <- Files and directories to ignore in version control.
├── Makefile                      <- File for automating tasks.
├── README.md                     <- Project description and setup instructions.
├── github.txt                    <- Recently added file, potentially for GitHub configurations.
├── pyproject.toml                <- Project configuration file (e.g., package metadata).
├── requirements.txt              <- Python dependencies list (recently updated).
├── setup.cfg                     <- Configuration for code quality tools like flake8.
```

--------

