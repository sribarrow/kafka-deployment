## connect to questdb
http://localhost:19000/

## with slight adaptation on
https://github.com/Yitaek/kafka-crypto-questdb

## other reference
https://questdb.io/blog/2023/01/03/change-data-capture-with-questdb-and-debezium

## Reference Samples Projects

There are 2 sample projects:
## [Faker](faker)
Simplistic project which uses a simple node.js application to create JSON entries in Apache Kafka and QuestDB Kafka Connect Sink to feed generated data from Kafka to QuestDB.

## [Stocks](stocks)
This project uses Debezium to stream data from Postgres to Kafka and QuestDB Kafka Connect Sink to feed data from Kafka to QuestDB. It also uses Grafana to visualize the data.

