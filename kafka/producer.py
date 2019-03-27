from kafka import KafkaProducer

producer = KafkaProducer(acks=1, compression_type='gzip', 
bootstrap_servers='class14.encore.com:6667,class15.encore.com:6667,class16.encore.com:6667')

# 단일 메시지 보내기
'''
future = producer.send('peter-topic', b'Apache Kafka is a distributed streaming platform')
result = future.get(timeout=60)
print(result)
'''

# for문을 이용해서 메시지 10개 보내기
'''
for i in range(1, 11):
    future = producer.send('peter-topic', b'Apache Kafka is a distributed streaming platform - %d' % i)
    result = future.get(timeout=60)
'''

# 키를 이용한 메시지 전송
for i in range(1, 11):
    if i % 2 == 1:
        future = producer.send('peter-topic2', key=b'1', value=b'%d - Apache Kafka is a distributed \
            streaming platform - key=1' % i)
        future.get()
    else:
        future = producer.send('peter-topic2', key=b'2', value=b'%d - Apache Kafka is a distributed \
            streaming platform - key=2' % i)
        future.get()
        