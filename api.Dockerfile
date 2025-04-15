FROM python:3.13-alpine

RUN apk update && apk upgrade
RUN apk add --no-cache --virtual build-deps build-base gcc
RUN pip install aws-sam-cli
RUN apk del build-deps

WORKDIR /app
COPY . .
RUN /usr/local/bin/sam build

CMD ["/usr/local/bin/sam", "local", "start-api", "--host", "0.0.0.0", "--docker-network", "dev_network"]