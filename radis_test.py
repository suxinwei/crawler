from redis import StrictRedis, ConnectionPool

redis = StrictRedis(host='localhost', port=6379, db=0, password='')
# redis = StrictRedis(connection_pool=ConnectionPool.from_url('redis://:@localhost:6379/0'))
redis.set('name', 'Bob')
print(redis.get('name'))
