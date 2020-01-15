FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y \
        software-properties-common \
        libssl-dev \
        libmysqlclient-dev

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update && \
    apt-get install -y \
        python3.8 \
        python3.8-dev \
        python3-pip

RUN mkdir -p /opt/dashi
COPY . /opt/dashi

RUN python3.8 -m pip install /opt/dashi/dist/dashi-0.1.0-py3-none-any.whl

CMD python3.8 -m dashi
