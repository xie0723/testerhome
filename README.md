#### 简介
>解析:  [TesterHome](https://testerhome.com/) 网站内容

#### 目的
>锻炼代码能力，熟悉Python Requests,爬虫,web开发等方面的库。

---
#### 目标：
##### 实现以下功能：

- 模拟登录 
- 数据获取
- 数据清洗分析
- 内容转换成PDF文档
- 数据可视化
- 接口监控
- 单元测试
- python django 开发仿testerhome

---

#### 使用
- clone 代码到本地

    git clone https://github.com/xie0723/testerhome.git
    或直接下载ZIP 文件后解压.


    
- 登录

    程序入口从 client.TesterHomeClient 开始

```python
from testerhome.tsclient.client import TesterHomeClient

th_client = TesterHomeClient()

th_client.login('xie0723', 'xie0723') # 登录

```

- 获取信息
```python
from testerhome.tsclient.client import TesterHomeClient

th_client = TesterHomeClient()
th_client.login('xie0723', 'xie0723') 


# 登录态时默认是username的关注者，也可以自提供username
print(th_client.followers('seveniruby').followers_num) 


# 关注者detail
for name, zname in th_client.followers('seveniruby').followers_detail:  

    print(u'昵称:{:<16} 名字：{:<15}'.format(name, zname))

```
输出:

```text
登录成功

关注者数量:910

昵称:sgq1117          名字：孙国权            
昵称:andyguo          名字：郭振华            
昵称:Lihuazhang       名字：恒温             
昵称:Anikikun         名字：大东             
昵称:oscarxie         名字：国文             
昵称:muchild          名字：七禾叶            
昵称:keen_lau         名字：keen           
昵称:guo              名字：GUO            
昵称:tomi             名字：TM             
昵称:qddegtya         名字：Archer_小A      
昵称:panshujuan       名字：潘淑娟            
昵称:cinderella       名字：汤大碗            
昵称:xulz             名字：许立             
昵称:luis             名字：               
昵称:oscar            名字：dabao          
昵称:luyi0824         名字：luyi0824       
昵称:skytiger0419     名字：宁如虎            
昵称:lion             名字：rywu           
.
.
.
.
```



```python
# 获取任意文章创建时间
print(th_client.article(7880).topic_age)

# 获取任意文章阅读量
print(th_client.article(7880).topic_volume)

# 获取任意文章作者
print(th_client.article(7880).topic_auth)

```
输出:
```text
topic_age:2017年3月10日
478 次阅读
topic_auth:Lihuazhang

```


---
#### TODO
- [x] 获取关注者数量，关注详情
- [x] 获取收藏数量，收藏详情
- [x] 完成正在关注 功能
- [ ] 获取翻页数据,例如关注者翻页
- [x] 爬取指定ID文章功能
- [ ] 完成爬取数据，分析测试关键字趋势变化
- [ ] 增加多线程爬取,提高访问性能
- [ ] 抓取收藏数最多的前N个文章，并转化成PDF
- [ ] 抓取点赞数最多的前N个文章，并转化成PDF
- [ ] 抓取关注数最多的前N个文章，并转化成PDF
- [ ] 获取文章评论


---
#### About Me
爱生活，爱技术！ To  Be  A  Better  Man

邮箱：xiewm.0723@gmail.com

**Tester，Pythonista，^_^**






