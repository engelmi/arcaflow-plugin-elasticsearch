FROM quay.io/centos/centos:stream8

RUN dnf -y module install python39 && dnf -y install python39 python39-pip git
RUN mkdir /app
ADD LICENSE /app
ADD es_plugin.py /app
ADD test_es_plugin.py /app
ADD requirements.txt /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "/app/es_plugin.py"]
CMD []

LABEL org.opencontainers.image.source="https://github.com/arcalot/arcaflow-plugin-elasticsearch"
LABEL org.opencontainers.image.licenses="Apache-2.0+GPL-2.0-only"
LABEL org.opencontainers.image.vendor="Arcalot project"
LABEL org.opencontainers.image.authors="Arcalot contributors"
LABEL org.opencontainers.image.title="Python Elasticsearch Plugin"
LABEL io.github.arcalot.arcaflow.plugin.version="1"