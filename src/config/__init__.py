import logging
import os
import sys
sys.path.append(os.getcwd())

# 获取环境变量
env = os.getenv("ZNYY_ENV", "")
if env == "PROD":
    # 如果有虚拟环境 则是 生产环境
    from .production import settings
elif env == "DEV":
    # 没有则是开发环境
    from .development import settings
else:
    logging.critical("缺少配置")
    exit(1)
