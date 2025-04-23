# dev


## Setup

Requirements 

- Docker & Docker Compose
- AWS SAM
- python3

To get started clone this repository and run the following command:

```bash
git submodule update --init --recursive
```
this will initalize all the submodules in this repo.

### Environment variables:

Create a .env file with the following values, values with <> surrounding them will require you to fill them in.
```
VITE_GATEWAY_API_URL=http://localhost:3000/dummy
VITE_COGNITO_USER_POOL_ENDPOINT=http://localhost:9229
VITE_COGNITO_USER_POOL_ID=local_2EfVJC8K
VITE_COGNITO_CLIENT_ID=1r4k4b23bva9jj3kxgd28zcc3
VITE_LOCAL=true

ENVIRONMENT=local
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<enter a secure password>
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
OPENSEARCH_INITIAL_ADMIN_PASSWORD=<enter a secure password (requires numbers, special characters and capitals)>
OPENSEARCH_HOST=opensearch-node1
OPENSEARCH_PORT=9200

AWS_DEFAULT_REGION=us-east-1
```

then run the `createEnvJson.py` file to create a .env.json file for the lambdas to use. 


### Initializing the Databases
**THIS ONLY NEEDS TO BE DONE ON THE INITIAL SETUP**

- start the databases with `docker compose up -d --build postgres opensearch-node1 opensearch-node2`

#### Postgres
1. cd into `data_product_kit`
2. setup a python virtual environment
    1. create a virtual environment with `python3 -m venv .venv`
    2. activate the virtual environment with `source .venv/bin/activate`
    3. install the requirements file with `pip install -r requirements.txt`
3. cd into `sql`
4. run `POSTGRES_HOST=localhost python3 ResetDatabase.py`
    - note: the `POSTGRES_HOST=localhost` is required

#### Opensearch
- There is no initalization step because indexes are created when first ingesting data.


### Starting the frontend

- **NOTE**: Make sure you are not in any subfolders of the project for running this. 
    - if you run into an issue where docker cannot find a .env, you are not in the right spot. 
- start the frontend with `docker compose up -d --build website cognito`

- open your browser of choice and navigate to `localhost:5500`

- login with username `test` and password `test`


### Starting the API Gateway
- NOTE: This will require another terminal, as it does not run detached

1. cd into `api`
2. run `sam build`
3. run `sam local start-api --docker-network dev_network --env-vars ../.env.json`
    - this starts the api in the docker network that the DBs are in and with the environment variables in .env.json


### Starting the Orchestrator Lambda
- NOTE: This will rquire another terminal, as it does not run detached

1. cd into `transformation_trigger/dev-env`
2. run `sam build`
3. run `sam local start-lambda --docker-network dev_network --container-env-vars ../../.env.json --env-vars ../../.env.json`



### Ingesting Data
- The `ingest.py` file will invoke the orchestrator lambda with a given file.
- this requires the databases and the orchestrator lambda to be running

- this requires the `boto3` library
    1. create a virtual environment with `python3 -m venv .venv`
    2. activate the virtual environment with `source .venv/bin/activate`
    3. install the requirements file with `pip install -r requirements.txt`

- to ingest run `python3 ingest.py <path-to-file>`

- **NOTE**: When ingesting dockets, documents and comments, dockets need to be ingested before documents and documents need to be ingested before comments, due to the relational database structure.
