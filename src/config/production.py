# 开发环境配置
import os
from typing import List
from pydantic import BaseSettings, validator, IPvAnyAddress, EmailStr, AnyHttpUrl


class Settings(BaseSettings):
    # 监听 URL
    HOST: str = '127.0.0.1'
    # 监听 端口
    PORT: int = 8000
    # 日志目录
    LOG_PATH = os.getcwd()
    # 数据库配置
    DB_NAME = 'znyy'
    DB_HOST = '127.0.0.1'
    DB_PORT = 3306
    DB_USER = 'root'
    DB_PASSWORD = '123456'

    PRODUCT = 'ZNYY'


# 实例化配置对象
settings = Settings()
