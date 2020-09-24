from redis import Redis #导入redis模块
# 创建redis对象,操作str类型
redis_client = Redis(host='localhost',port=6379,db=0)
redis_client.set('mingzi','itheima')
name = redis_client.get('mingzi')
print(name)