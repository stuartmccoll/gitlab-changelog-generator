FROM python:3.7-alpine

RUN apk add --no-cache bash build-base gcc
RUN pip install pytest mock requests python-dateutil

COPY . /gitlab-changelog-generator
WORKDIR /gitlab-changelog-generator
RUN python setup.py install

ENV SRC_PATH /usr/local/src/your-app
RUN mkdir -p $SRC_PATH

VOLUME [ "$SRC_PATH" ]
WORKDIR $SRC_PATH

CMD ["--help"]
ENTRYPOINT ["changegen"]
