#
# 7.3.4 has a nasty bug that broke requests.get for us; and other
# things for others: https://foss.heptapod.net/pypy/pypy/-/issues/3441
#
#FROM pypy:3.7-slim-buster
FROM debian:stable-slim

USER root

RUN \
  apt update \
  && apt install -y build-essential libpq-dev python3 python3-pip python3-virtualenv \
  && rm -rf /var/lib/apt/lists/* && virtualenv /app

WORKDIR /app

COPY requirements.txt .

ENV PATH="/app/bin:$PATH"

RUN \
  pip install --no-cache-dir -r requirements.txt \
  &&  mkdir -p logs

COPY searcch_backend ./searcch_backend
COPY setup.cfg setup.py run.py ./

ENV FLASK_INSTANCE_CONFIG_FILE=/app/config-production.py
ENV FLASK_APP=run:app

EXPOSE 80 5678

    
 CMD ["gunicorn","--config","gunicorn_conf.py","run:app"]
# CMD ["flask","run","--host=0.0.0.0","--port=80"]
# CMD ["pypy", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "-m", "flask","run","--host=0.0.0.0","--port=80", "--debugger"]
# CMD ["sleep", "infinity"]
