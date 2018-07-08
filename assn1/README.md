## 爬虫
一段自动抓取互联网信息的程序
> 简单爬虫架构（运行流程）  
调度端 --> URL管理器 --> 下载器 --> 解析器 --> 应用  

### PicsCrawler.py
爬取[PEXELS](https://www.pexels.com/)高清图片  

* 搜索框中输入关键字：smile，图片通过Ajax请求慢慢加载出来  
![img1](PEXELSPics/img1.png)  

* 通过对url中参数的分析，构造出以下结构  
`https://www.pexels.com/search/smile/?page=2`  
其中page代表的是页数，可以对值进行改变  
![img2](PEXELSPics/img2.png)  

* 找出当前页面的图片信息    
![img3](PEXELSPics/img3.png)
> 可以通过请求这个页面，将相关图片的链接解析出来，拿到想要的图片  
> ![img4](PEXELSPics/img4.png)  
> ![img5](PEXELSPics/img5.png) 
> ![img6](PEXELSPics/img6.png)   

* 选取图片进行下载，观察图片地址  
![img7](PEXELSPics/img7.png) 
![img8](PEXELSPics/img8.png) 

  





