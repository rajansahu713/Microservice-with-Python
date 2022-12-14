import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Blogs.settings")
django.setup()

from app.models import Blog

params = pika.URLParameters('amqps://pfjwwqsf:yZGEauqx7YSRBhDlSEOEwSg_S2UByLDd@beaver.rmq.cloudamqp.com/pfjwwqsf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):

    if properties.content_type == 'blog_liked':
        print('Received in admin')
        id = json.loads(body)
        blog = Blog.objects.get(id=id)
        blog.likes = blog.likes + 1
        blog.save()
        print('Blog likes increased!')
    if properties.content_type == 'blog_view':
        id = json.loads(body)
        blog = Blog.objects.get(id=id)
        blog.views = blog.views + 1
        blog.save()
        print("Blog view increase")


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()