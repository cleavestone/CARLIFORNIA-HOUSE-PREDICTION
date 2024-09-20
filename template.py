import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO, 
    format='[%(asctime)s]: %(message)s'
)

list_of_files=[
    "data/raw",
    "data/processed",
    "models",
    "src/__init__.py",
    "src/data_preprocessing.py",
    "src/model.py",
    "src/predict.py",
    "static/style.css",
    "static/images",
    "templates/index.html",
    "app.py",
    ".gitignore"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'creating directory: {filedir} for the file {filename}')

    if not os.path.exists(filepath) or (os.path.getsize(filename)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f'creating empty file {filename}')
    else:
        logging.info(f'{filename} already created')