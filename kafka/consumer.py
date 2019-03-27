from kafka import KafkaConsumer

# 그룹아이디, 브로커 주소, 자동 커밋, 오프셋 리셋 옵션을 지정합니다.
consumer = KafkaConsumer('peter-topic', group_id='peter-consumer',
    bootstrap_servers=['class14.encore.com:6667','class15.encore.com:6667','class16.encore.com:6667'],
    enable_auto_commit=True, auto_offset_reset='smallest')

# 루프를 돌고, poll을 호출하면서 메시지를 가져옵니다.
for message in consumer:
    #print(message)
    print("Topic: %s, Partition: %d, Offset: %d, Key : %s, Value: %s" % \
        (message.topic, message.partition, message.offset, message.key, message.value.decode('utf-8')))