# Logging with Opensearch on Docker

In this guide you will learn how to quickstart with detailed logging using opensearch.

## Setup Opensearch on Docker locally
### Pull OpenSearch images
#### OpenSearch
```bash
docker pull opensearchproject/opensearch:latest
```

#### OpenSearch dashboard
```bash
docker pull opensearchproject/opensearch-dashboards:latest
```

### Start Opensearch containers
#### OpenSearch
```bash
docker run -d -p 9200:9200 -p 9600:9600 -e "discovery.type=single-node" -e "plugins.security.disabled=true" opensearchproject/opensearch:latest
```

#### OpenSearch dashboard
```bash
docker run -it -d --network="host" -e "DISABLE_SECURITY_DASHBOARDS_PLUGIN=true" opensearchproject/opensearch-dashboards:latest
```

### Verify if the containers are up & running
Send a request to port 9200
```bash
curl https://127.0.0.1:9200
```
List indices through curl
```bash
curl -X GET "https://127.0.0.1:9200/_cat/indices?v"
```
Create indices through curl
```bash
curl -X PUT "https://127.0.0.1:9200/your_index_name"
```
Delete index
```bash
curl --location --request DELETE 'https://127.0.0.1:9200/index_name'
```
Fetch logs for an index_name
```bash
curl --location --request GET 'https://127.0.0.1:9200/ethereal/_search' \
  --header 'Content-Type: application/json' \
  --data '{
  "query": {
    "match_all": {}
  },
  "size": 10000
  }'
```

### Enable logging
Configure these variables in the `.env.local` file to ensure proper communication with OpenSearch and to enable client and server log aggregation
#### Enable client logging
Set `VITE_FORCE_CLIENT_LOG_AGGREGATE` to true to enable client log aggregation
```bash
VITE_FORCE_CLIENT_LOG_AGGREGATE=true
```

#### Enable Server Logging
Set `DISABLE_SERVER_LOG` to false to enable server log aggregation
```bash
DISABLE_SERVER_LOG=false
```
