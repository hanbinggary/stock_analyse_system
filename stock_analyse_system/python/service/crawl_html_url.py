
# 雪球网站地址
"""获取投资者列表"""
snow_ball_position_url = "https://xueqiu.com/cubes/discover/rank/cube/list.json?category=14&page={}&count={}"
"""雪球首页 当做登陆 会话使用"""
snow_ball_main_url = "https://xueqiu.com/"
"""获取指定投资者仓位"""
snow_ball_investor_url = "https://xueqiu.com/cubes/rebalancing/show_origin.json?rb_id={}"

"""雪球股票信息数据"""
snow_ball_stock_info_url="https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size={}&order=desc&orderby=percent&order_by=percent&market=CN&type=sh_sz&_=1568860118055"
"""雪球单只股票信息信息数据"""
# snow_ball_single_stock_info_url="https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol={}&begin={}&period=day&type=before&count={}&indicator=kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance"
snow_ball_single_stock_info_url="https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol={}&begin={}&period=day&type=before&count={}&indicator=kline"

snow_ball_stock_all_info = "https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size={}&order=desc&orderby=percent&order_by=percent&market=CN&type=sh_sz&_=1571144454126"

# 新浪地址
sina_comment_url= "http://finance.sina.com.cn/roll/index.d.html?cid=56589&page={}"

# 东方财富主力资金净流入地址
east_money_main_funds = "http://push2.eastmoney.com/api/qt/clist/get?pn=1&pz={}&po=1&np=1&ut=b2884a393a59ad64002292a3e90d46a5&fltt=2&invt=2&fid0=f4001&fid=f62&fs=m:0+t:6+f:!2,m:0+t:13+f:!2,m:0+t:80+f:!2,m:1+t:2+f:!2,m:1+t:23+f:!2,m:0+t:7+f:!2,m:1+t:3+f:!2&stat=1&fields=f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124&rt=52497485"