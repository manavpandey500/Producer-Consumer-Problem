import os
import sys
import pika
import time
import redis
redis_host = 'localhost'
redis_port = 6379


def main():
    try:
        r = redis.StrictRedis(
            host=redis_host, port=redis_port, decode_responses=True)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='hello')

        def callback(ch, method, properties, body):
            msg = body
            print(" [x] Received From Producer %r" % body)
            r.set("message", msg)
            # r.delete("message")
            msg = r.get("message")
            print(f"Message Set In Redis :: {msg} ")
        channel.basic_consume(
            queue='message', on_message_callback=callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
    except Exception as e:
        connection.close()
        print(e)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
