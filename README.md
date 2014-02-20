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

### ���˵��
��ֻ��һ���ϲ���������˵Ŀ��ƿ��, �²���ôʵ��ȡ������, ����ֻҪ��ץȡ�����Ե�log����һ������������. ��ֻ��һ�����ڴ��ģ���Եı�ש�����idea, ������ôʵʩ, �ǽ�����������!