import time
import pika
import redis
redis_host = 'localhost'
redis_port = 6379


def createMQConnection():
    while(True):
        try:
            r = redis.StrictRedis(
                host=redis_host, port=redis_port, decode_responses=True)
            msg = r.get("message")
            print(f"get Message From RADIS: {msg}")
            if(msg == None):
                msg = "HELLO from producer"
            else:
                r.delete("message")
            connection = pika.BlockingConnection(
                pika.ConnectionParameters('localhost'))
            channel = connection.channel()
            channel.queue_declare(queue='hello')
            channel.basic_publish(exchange='', routing_key='message', body=msg)
            print(" [x] Sent Message to Consumer")
            connection.close()
            time.sleep(10)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    # redis_string()
    # redis_integer()
    createMQConnection()
