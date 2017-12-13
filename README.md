SATURN
======

# 通用组件开发框架

## 文件夹结构

```
saturn
│
├── saturn               -->组件名称
│   ├── controllers      -->组件主要业务逻辑
│   ├── models           -->数据模型及数据库交互
│   ├── settings         -->组件设置项常量等信息
│   ├── utils            -->工具集模块
│   ├── libs             -->第三方模块或工具集
│   │   ├── db
│   │   └── logger
│   ├── api              -->组件接口层
│   │   ├── v1           -->http接口
│   │   └── rpc          -->rpc接口
│   └── app.py
├── manage.py
├── setup.py
│
├── database             -->项目初始化的表结构
├── docs                 -->文档
├── crons                -->项目定时任务
├── scripts              -->项目的脚本（shell或python脚本）
├── tools                -->脚本工具集
├── tests                -->项目单元测试用例
├── requirements         -->项目依赖
│
├── setup.cfg            -->lint配置
├── Makefile
└── README.md
```

## 开发及调试环境搭建

### 安装全局依赖

- [Python 2.7](https://www.python.org/downloads/release/python-279/): `brew install python`
- [Upgrate](https://pip.pypa.io/): `pip install -U setuptools pip`
- [Virtualenv](https://virtualenv.pypa.io): `pip install -U virtualenv`
- [MySQL](https://mariadb.com): `brew install mariadb`


### 安装本地依赖

    $ cd /path/to/saturn
    $ virtualenv -p python2.7 venv
    $ . venv/bin/activate
    $ make pip

### 准备环境变量

    $ cp .env.example .env
    $ vim .env

### 启动进程

    $ . venv/bin/activate
    $ honcho start

### Shell 调试

    $ . venv/bin/activate
    $ honcho run ipython

### 测试

    $ . venv/bin/activate
    $ make lint
    $ make unittest
    $ make apittest

## 配置管理

项目依赖、数据库表结构等应用配置信息一样被版本控制,变更也应该被提交到版本库。

### Python 依赖管理

Python 依赖存放在requirements文件夹中:

- `base.in`: 运行时依赖
- `dev.in`:  开发工具
- `testing.in`: 测试工具和测试环境依赖

管理依赖时，应该编辑 `*.in` 文件并运行 `make compile-deps` 以更新
`*.txt`，然后**将变更提交入版本库**。

生产环境应该被假设只安装 `base.txt` 中的依赖。
