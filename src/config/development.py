# 开发环境配置
import os
from typing import List
from pydantic import BaseSettings, validator, IPvAnyAddress, EmailStr, AnyHttpUrl


class Settings(BaseSettings):
    # 监听 URL
    HOST: str = '0.0.0.0'
    # 监听 端口
    PORT: int = 8001
    # 日志目录
    LOG_PATH = os.getcwd()
    # 数据库配置
    DRIVER = 'mysql'
    SOURCE = 'root:root@tcp(127.0.0.1:3306)/test'

    PRODUCT = 'ZNYY'


# 实例化配置对象
settings = Settings()
