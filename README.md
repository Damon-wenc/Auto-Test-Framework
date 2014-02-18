# Auto-Test-Framework

## English version

### description
An automatic &amp; light test framework based on Python &amp; HTML; python do the logic, and web(HTML) display it.

### 
### 
### 

## 中文说明

### 一句话综述
这是一个由Python&HTML构建的轻量级自动化测试框架; Python作逻辑层, HTML来显示.

### 设计定位
这不是是一个完整的自动化测试系统, 仅仅是一个上层的测试框架, 类似于一个控制中心, 下层的系统内的各种测试并不包含在内, 但是可以通过ssh来发送'start'命令, 通过收集'日志'接口来获取状态log, 等等来完成整套测试. 同时HTML(web)能清晰直白地显示出测试结果, 方便测试员观察.
### 框架
整套代码不到600行, 大体框架如下图
![structure](https://github.com/Damon-wenc/Auto-Test-Framework/raw/master/examples/structure.png)

* **web_tornado.py**是主函数, 由[tornado](http://www.tornadoweb.org/en/stable/)这个库发力, 主要处理index/init/run/stop/open log各个请求动作
* **GLOBAL.py**保存全局变量
* **init_by_ping.py**用抓取ping返回值的方式判断设备是否存活
* **run_test.py**采用多线程的方式处理发送命令/抓取log/分析log的操作
* **ssh.py**藉由plink连接各设备, 有重连机制
* **analysis.py**用抓取错误关键字的方式分析log

### 
### 