# Machine-Learning-as-a-Service repo

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

The project develops two machine learning models for an American retailer with 10 stores across California, Texas, and Wisconsin, including:

1. Predictive Model: To predict the sales revenue for a specific item in a particular store on a given date.
2. Forecasting Model: To forecast the total sales revenue across all stores and items for the next 7 days.

Each shop sells items from 3 different categories: hobbies, foods and household.

### You can access the deployed application at: 

[Machine Learning As A Service API](https://machine-learning-as-a-service-api.onrender.com/docs)

[Machine Learning As A Service Streamlit](https://machine-learning-as-a-service-streamlit.onrender.com/)

## Project Organization

```
Machine-Learning-as-a-Service/
├── at2_ml_as_a_service_api/
│   ├── app/                      # Main application directory
│
│   ├── backend/                  # Backend services
│   │   ├── Dockerfile            # Dockerfile for backend
│   │   ├── api.py                # API definitions
│   │   └── model.pkl             # Saved model in PKL format
│
│   ├── frontend/                 # Frontend services
│   │   ├── app.py                # Streamlit application
│   │   └── Dockerfile            # Dockerfile for frontend
│
│   ├── data/                     # Directory for datasets
│   │   └── processed/            # Folder for processed data
│   │       └── text.txt          # Processed data file
│
│   ├── docs/                     # Documentation files
│
│   ├── models/                   # Directory for storing trained models
│   │   ├── forecasting/          # Models related to forecasting
│   │   │   ├── prophet.pkl       # Trained Prophet model
│   │   │   ├── prophet_event.pkl  # Prophet model with event data
│   │   │   ├── prophet_holiday.pkl # Prophet model for holidays
│   │   │   ├── prophet_month.pkl  # Prophet model for monthly forecasting
│   │   │
│   │   └── predictive/           # Predictive modeling directory
│   │       ├── predictive_lgbm.pkl # LightGBM model for predictive tasks
│   │       └── .gitkeep          # Placeholder for empty directories
│
│   ├── notebooks/                # Jupyter notebooks for different tasks
│   │   ├── forecasting/          # Forecasting notebooks
│   │   │   └── forecasting-prophet.ipynb   # Prophet forecasting notebook
│   │   │
│   │   └── predictive/           # Predictive notebooks
│   │       └── predictive-lgbm.ipynb # LightGBM predictive notebook
│
│   ├── references/               # Resource documents like data dictionaries
│
│   ├── reports/                  # Reports, such as analysis results or visualizations
│
│   ├── src/                      # Source code for data processing and modeling
│   │   └── preparation.py        # Data preparation script
│
│   ├── .gitignore                # Files and directories to ignore in version control
│   ├── .gitkeep                  # Ensure version control for empty directories
│   ├── Makefile                  # File for automating tasks
│   ├── README.md                 # Project documentation
│   ├── github.txt                # GitHub-specific documentation
│   ├── render.txt                # Render-related configuration notes
│   ├── render.yaml               # Render configuration file
│   ├── pyproject.toml            # Project configuration file
│   ├── requirements.txt          # Project dependencies
│   └── setup.cfg                 # Configuration for code quality and packaging
│
└── at2_ml_as_a_service_experiments/
    ├── data/                     # Directory for datasets
    │   └── processed/            # Folder for processed data
    │       └── text.txt          # Processed data file (now deleted)
    │
    ├── docs/                     # Documentation files (e.g., for mkdocs)
    │
    ├── models/                   # Directory for storing trained models
    │   ├── forecasting/          # Models related to forecasting
    │   │   ├── prophet.pkl       # Trained Prophet model
    │   │   ├── prophet_event.pkl  # Prophet model incorporating event data
    │   │   ├── prophet_holiday.pkl # Prophet model for holiday-specific data
    │   │   ├── prophet_month.pkl  # Prophet model for monthly forecasting
    │   │
    │   └── predictive/           # Models related to predictive tasks
    │       ├── predictive_lgbm.pkl # LightGBM model for predictive tasks
    │       └── .gitkeep          # File to ensure the directory is versioned in Git
    │
    ├── notebooks/                # Directory for Jupyter notebooks
    │   ├── forecasting/          # Forecasting-related notebooks
    │   │   └── thehai_bui-24683423-forecasting-prophet.ipynb   # Prophet forecasting notebook
    │   │
    │   └── predictive/           # Predictive modeling notebooks
    │       └── thehai-bui-24683423-predictive-lgbm.ipynb       # LightGBM predictive modeling notebook
    │
    ├── references/               # Resources like data dictionaries or manuals
    │
    ├── reports/                  # Reports, such as analysis results or visualizations
    │
    ├── src/                      # Source code for data preparation and modeling
    │   └── preparation.py        # Script for data preparation
    │
    ├── .gitignore                # Files and directories to ignore in version control
    ├── Makefile                  # File for automating tasks
    ├── README.md                 # Project description and setup instructions
    ├── github.txt                # Recently added file, potentially for GitHub configurations
    ├── pyproject.toml            # Project configuration file (e.g., package metadata)
    ├── requirements.txt          # Python dependencies list (recently updated)
    └── setup.cfg                 # Configuration for code quality tools like flake8
