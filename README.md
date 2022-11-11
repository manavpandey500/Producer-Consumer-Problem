# Producer-Consumer-Problem
It is done with the help of Rabbit MQ and Redis local server

## Prerequisite

### <B> Steps to Install Rabbit MQ </B> 
 <li> Download the installer from https://www.rabbitmq.com/download </li>
 <li> Run it on http://localhost:15672/#/
 <li> Enter Default ID Password as "guest"

### <B> Steps to Install Redis on local server </B> 
 <li> <B> Install or enable WSL2 </B></li>

```
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
```
```
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
```
```
sudo apt-get update
```
```
sudo apt-get install redis
```
```
sudo service redis-server start

```

### <B> Steps to Install Pika </B> 
```
pip install pika
```



