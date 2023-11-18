# scrapy类爬虫说明

## 1、创建爬虫的项目（cmd终端运行）

命令1：cd 要创建爬虫项目的文件夹
命令2：scrapy startproject 项目的名字

注意1 :项目的名字不允许使用数字开头也不能包含中文
注意2：以下所有命令均由命令行(windows)系统自带终端运行
## 2、创建爬虫文件（cmd终端运行）

要在spiders文件夹中去创建爬虫文件

命令1：
cd 项目的名字\项目的名字\spiderscd
eg(实例):
cd   scrapy_baidu_091\scrapy_baidu_091\spiders
命令2：
scrapy genspider 爬虫文件的名字（网页名称＋网页域名）
eg(实例)：
scrapy genspider baidu www.baidu.com

注意：一般情况下不需要添加 http协议，因为start_urls的值是根据allowed_domains修改的 所以添加了http的话，那么start_urls就需要我们手动去修改了。
## 3.运行爬虫代码（cmd终端运行）
命令：scrapy crawl 爬虫的名字
eg：scrapy crawl baidu
