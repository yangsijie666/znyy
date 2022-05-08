# ZNYY 创新工具

## 使用方法

### 按需修改配置
更新 `src/config/production.py`（生产环境配置文件）或 `src/config/development.py`（开发环境配置文件）
```text
# 监听 URL
HOST: str = '0.0.0.0'
# 监听 端口
PORT: int = 8001
# 日志目录
LOG_PATH = os.getcwd()
# 数据库配置
DRIVER = 'mysql'
SOURCE = 'root:root@tcp(127.0.0.1:3306)/test'
```

### 运行
```shell
# 初始化运行环境
make init
# 开发环境运行
make run-dev
# 生产环境运行
# make run
```

## 目录结构

```text
znyy tree -L 1 
.
├── Makefile            # 运维脚本
├── README.md           # 说明文档
├── bin                 # 可执行文件目录
├── docs                # 文档
├── requirements.txt    # 依赖包版本
├── src                 # 源码
```



```text
znyy tree src -L 1 
src
├── biz             # 领域层
├── config          # 配置
├── data            # DB层
├── main.py         # 入口代码（编写 API url 的入口）
├── service         # Api层
├── tests           # 测试
└── utils           # 工具
```

访问链路
```text
main.py (入口函数) -> 
service (注册的API方法 / API 层，会对请求体做校验和默认值填充) -> 
biz (执行具体逻辑的方法 / 领域层) ->
data (使用 repo 执行访问外部（DB）获取 DO 对象 / DB层) ->
data （DB 层将 DO 对象转换为 领域对象 entity）->
biz （获取到 entity，可能需要再做一些操作，将 entity 返回给 API 层）->
service （将 entity 转换为 DTO 对象）->
main.py 
```

```text
DTO: API 层的对象，所在目录（service/dto/）
entity：领域层对象，所在目录（biz/model/）
DO：DB 层的对象，所在目录（data/do/）
VO：第三方的对象（比如 ssh 返回的话单）
```
