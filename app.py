from flask import Flask, request, redirect
import twilio.twiml
import threading, logging, time
from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError

app = Flask(__name__)

callers = {}


@app.route("/", methods=['GET', 'POST'])
def dis_handler():
    """Respond to incoming SMS."""

    from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Monkey, thanks for the message!"

    kafka_producer = get_kafka_producer()
    future = kafka_producer.send('dis-test', b'raw_bytes')
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        # Decide what to do if produce request failed...
        log.exception()
        pass
    print (record_metadata.topic)
    print (record_metadata.partition)
    print (record_metadata.offset)
    print str(record_metadata)
    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)

def get_kafka_producer():
    return KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])


if __name__ == "__main__":
    app.run(debug=True)
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    #main()
