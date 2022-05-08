HOST:=$(host)
PORT:=$(port)
ifeq ($(HOST),)
	HOST:=0.0.0.0
endif
ifeq ($(PORT),)
	PORT:=8000
endif

.PHONY: init
# 从requirements.txt中初始化依赖
init:
	pip install -r requirements.txt;

.PHONY: generate
# 保存当前依赖至requirements.txt
generate:
	pip freeze > requirements.txt;

.PHONY: run-dev
# 运行
run-dev:
	export ZNYY_ENV=DEV; python src/main.py;

.PHONY: run
# 运行
run:
	export ZNYY_ENV=PROD; python src/main.py;

# 清理日志等文件
.PHONY: clean
clean:
	make clean-log;

.PHONY: clean-log;
clean-log:
	rm -rf ./znyy*.log