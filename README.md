# Auto-Test-Framework

## English version

### description
An automatic &amp; light test framework based on Python &amp; HTML; python do the logic, and web(HTML) display it.

### 
### 
### 

## ����˵��

### һ�仰����
����һ����Python&HTML�������������Զ������Կ��; Python���߼���, HTML����ʾ.

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

### 
### 