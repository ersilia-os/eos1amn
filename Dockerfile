FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit=2020.03
RUN pip install networkx==2.0
RUN pip install pmapper==0.4.0

WORKDIR /repo
COPY ./repo
