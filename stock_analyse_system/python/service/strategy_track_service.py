from python.util import date_time_util
from python.dao import stock_strategy_record_dao,log_dao,stock_strategy_dao
from python.redis import redis_pool,redis_key_constants
import logging
"""策略选股跟踪处理类"""
class strategy_track():

    def __init__(self):
        self.redis = redis_pool.RedisPool()
        self.log_dao = log_dao.log_record()
        self.stock_strategy_record = stock_strategy_record_dao.stock_strategy_record()
        self.stock_strategy = stock_strategy_dao.stock_strategy()


    """跟踪记录策略选择股票信息"""
    def get_track_stock(self):

        logging.info("------------------调用跟踪方法开始-----------------")
        """获取5个工作日前日期"""
        begin_date = date_time_util.get_work_date(5)
        """获取上一个工作日日期"""
        end_date = date_time_util.get_work_date(1)
        param = []
        param.append(begin_date)
        param.append(end_date)
        # 查询需要追溯时间内的所有股票
        track_stock_list = self.stock_strategy.get_stock_track(param)
        # 遍历追溯股票
        for stock in track_stock_list:
            stock_code = stock['stock_code']
            current_data = self.redis.hget(redis_key_constants.current_day_stock_map,stock_code)
            if current_data == None:
                param = []
                param.append(1)
                param.append(stock_code)
                param.append("追溯股票异常，股票信息不存在")
                self.log_dao.add_log(param)
                continue
            # 记录当天追溯信息
            self.stock_strategy_record.save_stock_strategy_record(stock_code,current_data)

        logging.info("------------------调用跟踪方法结束-----------------")
        # 删除redis里面缓存
        self.redis.delString(redis_key_constants.current_day_stock_map)


