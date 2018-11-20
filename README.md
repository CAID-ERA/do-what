# do-what
Deploy the flask app by:
```
cd Scripts
sudo sh ./init.sh
export FLASK_APP = app.py
cd ../Flask/
```
Run the web app without logging by:
```nohup python3 -m flask run -h 0.0.0.0 --port 80 >/dev/null 2>&1 &```

Or run the app in the debug mode by:
```python3 -m flask run -h 0.0.0.0 --port 80```

This app uses a remote MySQL database and it will be closed at around the end of Dec. 2018.
If there's any advice please email us at: iiivanzhu@gmail.com  

## Introduction to our project
![do-what group](https://github.com/CAID-ERA/do-what/raw/master/Flask/static/architect.png) 
 
### 一级目录下：
```
Flask
Script
.gitignore
LICENSE
README.md
```
#### 1.Flask
```
recommend
static
templates
utils
app.py
```
1.1 recommend:内含推荐算法源码  
1.2 static:静态文件  
1.3 templates:用于渲染的模板  
1.4 utils:开发小工具，后期维护将加入音乐以及其他推荐  
1.5 app.py:包含后端的路由规则以及对应的逻辑  

#### 2.Script:项目部署脚本代码  
#### 3..gitignore:过滤一些无用的编译的一些残余文档的规则  
#### 4.LICENSE:许可证  
#### 5.README.md:本文档  


