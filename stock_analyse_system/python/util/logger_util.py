import logging
import date_time_util
from logging.handlers import TimedRotatingFileHandler

"""日志初始化配置"""
def logger_init():
    # 第一步，创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG) # Log等级总开关
    # 第二步，创建一个handler，用于写入日志文件
    logfile = date_time_util.get_date_time_line(0) + '-log.txt'
    # fh = logging.FileHandler(logfile, mode='a') # open的打开模式这里可以进行参考
    fh = TimedRotatingFileHandler(filename=logfile, when="D", interval=1)
    fh.setLevel(logging.DEBUG) # 输出到file的log等级的开关

    # 第三步，再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)  # 输出到console的log等级的开关
    # 第四步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # 第五步，将logger添加到handler里面
    logger.addHandler(fh)
    logger.addHandler(ch)