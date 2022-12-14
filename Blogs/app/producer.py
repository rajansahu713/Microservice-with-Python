import pika, json

params = pika.URLParameters('amqps://pfjwwqsf:yZGEauqx7YSRBhDlSEOEwSg_S2UByLDd@beaver.rmq.cloudamqp.com/pfjwwqsf')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)