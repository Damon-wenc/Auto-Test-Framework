# Auto-Test-Framework

## English version

### Keywords
An automatic &amp; light mass-clients test framework based on Python &amp; HTML; python do the logic, and web(HTML) display it.

### description
This is not a complete auto-test system, it's just a upper layer test framework, sort of a 'Control Center', allow you to master a mass of devices; whatever tests you are about to run on your device is not included, but this framework will help you senting 'start/stop' commands via SSH, and collecting test logs to monitor test progress, and eventually the web will show the test results to you in a clear way.

### Structure
The code is less than 600 lines, the structure of the framework is like thils:
![structure](https://github.com/Damon-wenc/Auto-Test-Framework/raw/master/examples/structure.png)

* **web_tornado.py** is the base, it's powered by [tornado](http://www.tornadoweb.org/en/stable/), a powerful library of Python; it process requests like 'GET index/init/run/stop/open_log';
* **GLOBAL.py** saves global variables;
* **init_by_ping.py** detecting whether your devices are online by fetch the return value of 'ping' cmd;
* **run_test.py** send commands/retrieve log/analysis log with multi-threading;
* **ssh.py** connecting to your devices with 'plink' tool, with a mechanism of re-connect;
* **analysis.py** analysis retrieved log by matching 'error keywords'

### Examples
1. root page: this is the page shown up after you run web_tornado.py
![index](https://github.com/Damon-wenc/Auto-Test-Framework/raw/master/examples/index.jpg)
You can see we could monitor 100 or more devices here.
2. step 2, click the 'init' button
![init](https://github.com/Damon-wenc/Auto-Test-Framework/raw/master/examples/init.jpg)
Now there are 80 devices online, with color green, and the other 20 devices are offline, with color grey
3. step 3, click the 'run' button
![run](https://github.com/Damon-wenc/Auto-Test-Framework/raw/master/examples/run.jpg)
Now the program begins to run, error occurred on any devices will turn the color of the devices from green to red, and logs from those particular devices will not longer be updated. So if you click the table url, if the device is OK, as green, the latest folder will shown up automatically; while if you click the wrong ones, as red, the log of the failed round will shown up.
4. step 4, if you want to finish the test, click the 'stop' button.

### Details
Please watch the code by urself :D

### Implementation
The code is tested with Python version 2.7 on Windows. All you need to install is tornado library, please follow the [official guide](http://www.tornadoweb.org/en/stable/#installation). And if your OS is *nix, you may rewrite the ssh.py module with more properly libraries, like paramiko.

### Last words
This is just a light&clear upper level control framework, what you are intending to do on your device is not included,  'send' -> 'run' -> 'retrieve log' -> 'analysis log' is a complete loop.
This is a idea about 'auto-test on mass of devices', how you are about to implement it or what, that is for you to decide. XD

## ����˵��

### һ�仰����
����һ����Python&HTML���������������ģ�Զ������Կ��; Python���߼���, HTML����ʾ.

### ��ƶ�λ
�ⲻ����һ���������Զ�������ϵͳ, ������һ���ϲ�Ĳ��Կ��, ������һ����������, �²��ϵͳ�ڵĸ��ֲ��Բ�����������, ���ǿ���ͨ��ssh������'start'����, ͨ���ռ�'��־'�ӿ�����ȡ״̬log, �ȵ���������ײ���. ͬʱHTML(web)������ֱ�׵���ʾ�����Խ��, �������Ա�۲�.

### ���
���״��벻��600��, ����������ͼ
![structure](https://github.com/Damon-wenc/Auto-Test-Framework/raw/master/examples/structure.png)

* **web_tornado.py**��������, ��[tornado](http://www.tornadoweb.org/en/stable/)����ⷢ��, ��Ҫ����index/init/run/stop/open log����������
* **GLOBAL.py**����ȫ�ֱ���
* **init_by_ping.py**��ץȡping����ֵ�ķ�ʽ�ж��豸�Ƿ���
* **run_test.py**���ö��̵߳ķ�ʽ����������/ץȡlog/����log�Ĳ���
* **ssh.py**����plink���Ӹ��豸, ����������
* **analysis.py**��ץȡ����ؼ��ֵķ�ʽ����log

### ����ʾ��
1. ����������web_tornado.py��ĸ�ҳ��
![index](https://github.com/Damon-wenc/Auto-Test-Framework/raw/master/examples/index.jpg)
����չʾ�˶�100̨�豸���й���.
2. �ڶ���, �û�init��
![init](https://github.com/Damon-wenc/Auto-Test-Framework/raw/master/examples/init.jpg)
��������ǰ80̨�豸����, ����ɫ��ʶ; ��ɫ�豸�ǲ�����.
3. ������, �û�run��
![run](https://github.com/Damon-wenc/Auto-Test-Framework/raw/master/examples/run.jpg)
��ʱ�����ѿ�ʼ����, ���ҳ���������豸���ú�ɫ��ʶ. ��������, ����ת����Ӧ��log�ִ�. ������ɫ�Ļ���ת��96��log, ��ɫ����ת�����������һ��. ��ɫ���豸�����������̺�������. 
4. ���Ĳ�, �����в����������stop��

### ��ϸ���
�������Ͻ������Ķ�Դ����:D

### ����
��������Windowsƽ̨�ϵ�Python 2.7�汾�²���ͨ��. ����Ҫ��ֻ�ǰ�װ��tornado��, ���Բ���[�ٷ��ĵ�](http://www.tornadoweb.org/en/stable/#installation), ����һЩ���������Ҫ��Windows�ı���汾. ������Ҫ��*nixƽ̨�����д˴���, ����Ҫ��дssh.pyģ��, ���ø���׼�Ŀ�, ����paramiko��.

### ���˵��
��ֻ��һ���ϲ���������˵Ŀ��ƿ��, �²���ôʵ��ȡ������, ����ֻҪ��ץȡ�����Ե�log����һ������������. ��ֻ��һ�����ڴ��ģ���Եı�ש�����idea, ������ôʵʩ, �ǽ�����������!