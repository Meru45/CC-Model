FROM python:3.9

WORKDIR /app

RUN pip install deepchem torch 

COPY model_cell_counting/checkpoint1.pt /app/

