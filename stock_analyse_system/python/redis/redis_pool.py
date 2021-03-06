import redis
from python.mysql import mysql_config

"""redis 连接池"""
class RedisPool():

    """初始化redis连接"""
    def __init__(self):
        pool = redis.ConnectionPool(host=mysql_config.REDIS_HOST, port= 6379, password = mysql_config.REDIS_PASSWORD, db=mysql_config.REDIS_DB, decode_responses=True)
        self.service = redis.Redis(connection_pool=pool)

    """保存字符串"""
    def setString(self,key,value):
        return self.service.set(key,value)

    """设置字符串过期时间"""
    def setStringExpire(self,key,value,second):
        return self.service.setex(key,second,value)
    """获取字符串"""
    def getString(self,key):
        return self.service.get(key)
    """删除字符串"""
    def delString(self,key):
        return self.service.delete(key)

    """map存储"""
    def hset(self,name,key,value):
        return self.service.hset(name,key,value);

    """map单个删除"""
    def hdel(selef,name,key):
        return selef.service.hdel(name,key)
    """map获取单个"""
    def hget(self,name,key):
        return self.service.hget(name,key)

    """保存map"""
    def setMap(self,key,map):
        return self.service.hmset(key,map)

    """获取map"""
    def getMap(self,key):
        return self.service.hgetall(key)


