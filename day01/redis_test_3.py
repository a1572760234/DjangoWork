import redis
redis_conn = redis.Redis(host='localhost',port=6379,db=0)
redis_conn.set('test','hello')