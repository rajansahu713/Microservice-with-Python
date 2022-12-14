import pika, json
from main import app, Blog, db

params = pika.URLParameters('amqps_url')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)

    if properties.content_type == 'blog_created':
        with app.app_context():
            product = Blog(id=int(data['id']), title=data['title'], image=data['image'], description=data['description'])
            db.session.add(product)
            db.session.commit()
            print('Blog Created')

    elif properties.content_type == 'blog_updated':
        with app.app_context():
            product = Blog.query.get(data['id'])
            product.title = data['title']
            product.image = data['image']
            product.description = data["description"]
            db.session.commit()
            print('Blog Updated')

    elif properties.content_type == 'blog_deleted':
        with app.app_context():
            product = Blog.query.get(data)
            db.session.delete(product)
            db.session.commit()
            print('Blog Deleted')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()