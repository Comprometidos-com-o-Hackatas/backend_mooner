import redis

r = redis.StrictRedis(
    host='redis-16798.c11.us-east-1-3.ec2.redns.redis-cloud.com',
    port=16798,
    username='default',
    password='vo0nNYwJoubyuPd8Oy2sQjXrJh0dlHja'
)
print(r.ping())  # Deve retornar True
