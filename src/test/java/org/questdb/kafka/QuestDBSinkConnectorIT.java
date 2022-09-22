//package org.questdb.kafka;
//
//import io.debezium.testing.testcontainers.Connector;
//import io.debezium.testing.testcontainers.ConnectorConfiguration;
//import io.debezium.testing.testcontainers.DebeziumContainer;
//import okhttp3.OkHttpClient;
//import okhttp3.Request;
//import okhttp3.RequestBody;
//import okhttp3.Response;
//import org.apache.kafka.clients.producer.KafkaProducer;
//import org.apache.kafka.clients.producer.Producer;
//import org.apache.kafka.clients.producer.ProducerConfig;
//import org.apache.kafka.clients.producer.ProducerRecord;
//import org.apache.kafka.clients.producer.RecordMetadata;
//import org.apache.kafka.common.serialization.StringSerializer;
//import org.junit.jupiter.api.BeforeAll;
//import org.junit.jupiter.api.Test;
//import org.slf4j.Logger;
//import org.slf4j.LoggerFactory;
//import org.testcontainers.containers.GenericContainer;
//import org.testcontainers.containers.KafkaContainer;
//import org.testcontainers.containers.Network;
//import org.testcontainers.containers.output.Slf4jLogConsumer;
//import org.testcontainers.containers.wait.strategy.HttpWaitStrategy;
//import org.testcontainers.lifecycle.Startables;
//import org.testcontainers.utility.DockerImageName;
//
//import java.io.BufferedInputStream;
//import java.io.File;
//import java.io.FileInputStream;
//import java.io.FileOutputStream;
//import java.io.IOException;
//import java.time.Duration;
//import java.util.Properties;
//import java.util.jar.Attributes;
//import java.util.jar.JarEntry;
//import java.util.jar.JarOutputStream;
//import java.util.jar.Manifest;
//import java.util.stream.Stream;
//
//import static java.time.Duration.ofMinutes;
//
//public class QuestDBSinkConnectorIT {
//    private static final OkHttpClient CLIENT = new OkHttpClient();
//
//    private static Network network = Network.newNetwork();
//
//    private static KafkaContainer kafkaContainer = new KafkaContainer(DockerImageName.parse("confluentinc/cp-kafka:7.2.0"))
//            .withNetwork(network);
////            .withLogConsumer(new Slf4jLogConsumer(LoggerFactory.getLogger("kafka")));
//
//    public static DebeziumContainer connectContainer = new DebeziumContainer("debezium/connect-base:1.9.5.Final")
//            .withFileSystemBind("target/questdb-connector", "/kafka/connect/questdb-connector")
//            .withNetwork(network)
//            .withKafka(kafkaContainer)
//            .dependsOn(kafkaContainer)
//            .waitingFor(new HttpWaitStrategy()
//                    .forPath("/connectors")
//                    .forPort(8083)
//                    .withStartupTimeout(ofMinutes(4))
//            )
//            .withLogConsumer(new Slf4jLogConsumer(LoggerFactory.getLogger("connect")));
//
//    private static GenericContainer questDBContainer = new GenericContainer("questdb/questdb:6.5.2")
//            .withNetwork(network)
//            .withExposedPorts(9000)
//            .withLogConsumer(new Slf4jLogConsumer(LoggerFactory.getLogger("questdb")));
//
//    @BeforeAll
//    public static void startContainers() throws Exception {
//        createConnectorJar();
//        Startables.deepStart(Stream.of(
//                        kafkaContainer, connectContainer, questDBContainer))
//                .join();
//    }
//
//    @Test
//    public void test() throws Exception {
//        Properties props = new Properties();
//
//        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, kafkaContainer.getBootstrapServers());
//        props.put(ProducerConfig.ACKS_CONFIG, "all");
//        props.put(ProducerConfig.RETRIES_CONFIG, Integer.MAX_VALUE);
//        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
//        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
//        try (Producer<String, String> producer = new KafkaProducer<>(props)) {
//            RecordMetadata recordMetadata = producer.send(new ProducerRecord<>("test-topic", "key", "value")).get();
//            System.out.println(recordMetadata);
//        }
//
//        ConnectorConfiguration connector = ConnectorConfiguration.create()
//                .with("connector.class", "org.questdb.kafka.QuestDBSinkConnector")
//                .with("tasks.max", "1")
////                .with("key.converter", "org.apache.kafka.connect.storage.StringConverter")
////                .with("value.converter", "org.apache.kafka.connect.storage.StringConverter")
//                .with("topics", "test")
//                .with("auto.offset.reset", "earliest")
//                .with("my.setting", questDBContainer.getNetworkAliases().get(0) + ":9009");
//
//        connectContainer.registerConnector("my-connector", connector);
////        connectContainer.ensureConnectorTaskState("my-connector", 0, Connector.State.RUNNING);
//
//        final Request request = new Request.Builder()
//                .url("http://" + questDBContainer.getHost() + ":" + questDBContainer.getFirstMappedPort() + "/exec?query=select * from whatever")
//                .build();
//
//        for (;;) {
//            try (Response response = CLIENT.newCall(request).execute()) {
//                int code = response.code();
//                if (code == 200) {
//                    System.out.println(response.body().string());
//                    break;
//                } else {
//                    System.out.println("Waiting for QuestDB to start");
//                    Thread.sleep(1000);
//                }
//            }
//        }
//    }
//
//    private static void createConnectorJar() throws IOException {
//        Manifest manifest = new Manifest();
//        manifest.getMainAttributes().put(Attributes.Name.MANIFEST_VERSION, "1.0");
//        JarOutputStream target = new JarOutputStream(new FileOutputStream("target/questdb-connector/questdb-connector.jar"), manifest);
//        add(new File("target/classes"), target);
//        target.close();
//    }
//
//    private static void add(File source, JarOutputStream target) throws IOException {
//        String name = source.getPath().replace("\\", "/").replace("target/classes/", "");
//        if (source.isDirectory()) {
//            if (!name.endsWith("/")) {
//                name += "/";
//            }
//            JarEntry entry = new JarEntry(name);
//            entry.setTime(source.lastModified());
//            target.putNextEntry(entry);
//            target.closeEntry();
//            for (File nestedFile : source.listFiles()) {
//                add(nestedFile, target);
//            }
//        }
//        else {
//            JarEntry entry = new JarEntry(name);
//            entry.setTime(source.lastModified());
//            target.putNextEntry(entry);
//            try (BufferedInputStream in = new BufferedInputStream(new FileInputStream(source))) {
//                byte[] buffer = new byte[1024];
//                while (true) {
//                    int count = in.read(buffer);
//                    if (count == -1)
//                        break;
//                    target.write(buffer, 0, count);
//                }
//                target.closeEntry();
//            }
//        }
//    }
//}
