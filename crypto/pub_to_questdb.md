<!-- pub from btc -->
curl -X POST -H "Content-Type: application/json" -d '{
  "name": "questdb-sink-btc",
  "config": {
    "connector.class":"io.questdb.kafka.QuestDBSinkConnector",
    "tasks.max":"1",
    "topics": "topic_BTC",
    "key.converter": "org.apache.kafka.connect.storage.StringConverter",
    "value.converter": "org.apache.kafka.connect.json.JsonConverter",
    "key.converter.schemas.enable": "false",
    "value.converter.schemas.enable": "false",
    "host": "questdb",
    "timestamp.field.name": "timestamp"
  }
}' localhost:8083/connectors
<!-- pub from eth -->
curl -X POST -H "Content-Type: application/json" -d '{
  "name": "questdb-sink-eth",
  "config": {
    "connector.class":"io.questdb.kafka.QuestDBSinkConnector",
    "tasks.max":"1",
    "topics": "topic_ETH",
    "key.converter": "org.apache.kafka.connect.storage.StringConverter",
    "value.converter": "org.apache.kafka.connect.json.JsonConverter",
    "key.converter.schemas.enable": "false",
    "value.converter.schemas.enable": "false",
    "host": "questdb",
    "timestamp.field.name": "timestamp"
  }
}' localhost:8083/connectors
<!-- pub from link -->
curl -X POST -H "Content-Type: application/json" -d '{
  "name": "questdb-sink-link",
  "config": {
    "connector.class":"io.questdb.kafka.QuestDBSinkConnector",
    "tasks.max":"1",
    "topics": "topic_LINK",
    "key.converter": "org.apache.kafka.connect.storage.StringConverter",
    "value.converter": "org.apache.kafka.connect.json.JsonConverter",
    "key.converter.schemas.enable": "false",
    "value.converter.schemas.enable": "false",
    "host": "questdb",
    "timestamp.field.name": "timestamp"
  }
}' localhost:8083/connectors