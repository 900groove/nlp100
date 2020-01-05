FROM python:3.7

RUN pip install -U pip && \
    pip install \
    jupyter \
    matplotlib \
    japanize-matplotlib \
    pytest
