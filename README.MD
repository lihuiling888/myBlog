## 一、环境配置

1. VScode下载，安装python，chinese，path intellisece, npm, npm intellisence,       Vetur, Vue3 Snippets, vscode-icons, live sever  这些插件

   ![image-20210104105723956](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104105723956.png)

2. 配置终端   切换到cmd![image-20210104105545929](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104105545929.png)

3. 安装前端开发工具HbuilderX  https://www.dcloud.io/hbuilderx.html

4. 安装小程序开发工具 https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html

## 二、安装git

1. 安装git https://git-scm.com

2. 创建远程仓库 myBlog

   ![image-20210104110041591](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104110041591.png) 

   ![image-20210104110242776](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104110242776.png)![image-20210104110830670](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104110830670.png)

3. 初始化本地仓库，也就是在本地myBlog文件夹下执行 `git init` ，执行完后会创建一个 .git 的隐藏文件

   ![image-20210104110620826](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104110620826.png)

4. 远程仓库和本地仓库进行关联 git remote add origin “你的远程仓库地址”

   ![image-20210104110853645](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104110853645.png)

5. 如果出现错误，ssh没有创建

6. 先去创建秘钥 ssh-keygen,一路enter，生成秘钥

7. 查看生成的秘钥 `cat ~/.ssh/id_rsa.pub`![image-20210104111137119](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104111137119.png)   

8. 将秘钥写入到github上的settings下的SSH and GPG keys 下![image-20210104111507321](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104111507321.png)

   ![image-20210104111548346](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104111548346.png)

9. 推送四步骤：

   `git status`    查看发生变化的文件

   `git add .`    追踪所有发生变化的文件

   `git commit -m "备注"`  提交到本地仓库

   `git push -u origin master` （第一次提交）推送到远程仓库

   `git push` （之后提交）

## 三、创建myBlog项目

1. 空文件下，执行 `django-admin startproject myBlog`创建myBlog项目

2. 给myBlog创建虚拟环境，使用 `python -m venv env`(env为虚拟环境名称)

3. 进入虚拟环境，Windows下：`.\\env\\Scripts\\activate`

4. 退出虚拟环境，Windows下：`deactivate`

5. 使用VSCode打开myBlog，执行 

   python manage.py startapp articles 创建articlesAPP 

   python manage.py startapp users 创建usersAPP

   python manage.py startapp cousers  创建cousersAPP

6. 迁移 python manage.py makemigrations

   python manage.py migrate

## 四、创建articles的model

1. 创建model

2. 数据库同步

3. 在admin.py中注册model

4. 创建超级用户 `python manage.py createsuperuser`

   账号：admin   邮箱：2593908796@qq.com  密码：admin123

5. 运行项目： `python manage.py runserver` 

6. 127.0.0.1:8000/admin 进入

7. 在settings文件里修改(页面显示中文)

   `LANGUAGE_CODE = ‘zh-Hans’`

   `TIME_ZONE = 'Asia/Shanghai'`

   `USE_TZ = False`

8. ![image-20210104164947769](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104164947769.png)

9. 将app注册到settings.py里

   ![image-20210104165313642](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104165313642.png)

10. 再次迁移运行，页面增加了

   ![image-20210104165524714](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104165524714.png)

11. 将图片写为不是必填的，访问量默认为0

   ![image-20210104165903609](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104165903609.png)

12. 添加文章并保存![image-20210104170242007](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104170242007.png)

13. 在models.py里重写str方法，迁移刷新

   ![](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104170428442.png)![image-20210104170613088](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104170613088.png)

14. 页面显示字段添加搜索框

   ![image-20210104170853517](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104170853517.png)![image-20210104171002370](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104171002370.png)

15. 在models里添加，迁移

   ![image-20210104171127606](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104171127606.png)![image-20210104171156149](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104171156149.png)

 ## 五、业务逻辑

1. 文章列表页，分页
2. 文章详情页，评论
3. 全局搜索功能 Q
4. 最新文章，最新评论的排行
5. 按照分类，标签的一个聚类操作
6. 联系我页面，发送邮件

   ​          

1. 新建templates文件夹和static文件夹

2. 将相应的文件分别放入文件夹

3. 在articles里的views渲染模板

   ![image-20210104184934736](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104184934736.png)

4. 在articles里新建urls.py文件

5. 在总urls.py中将articles里的分路由写进去

   ![image-20210104185405364](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104185405364.png)

6. 在articles的分路由写入路径

   ![image-20210104203520636](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104203520636.png)

7. 运行 ，进入http://127.0.0.1:8000/article/list/

8. 在index里修改

   ![image-20210104191112837](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104191112837.png)![image-20210104191325384](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104191325384.png)

9. 其他三个HTML也改同一地方

10. articles里的apps.py![image-20210104193456461](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104193456461.png)

11. settings.py 里

   ![image-20210104193826855](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104193826855.png)

12. 在users,cousersAPP里起别名![image-20210104194249240](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104194249240.png)

   ![image-20210104194215023](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104194215023.png)

13. 多添加几篇文章

14. 在templates文件夹下创建common文件夹，在common文件夹下创建base.html，aside.html

15. 把首页（index)里的内容复制到base.html里,

   将index里的内容清空

   将<div class="col-md-8">复制到index里

   将<div class="col-md-4">复制到aside里

   base里的<div class="col-md-4/8">删除

16. ![image-20210104200649228](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104200649228.png)![image-20210104201245851](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104201245851.png)![image-20210104202451249](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104202451249.png)![image-20210104202034463](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104202034463.png)![image-20210104201812145](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104201812145.png)

17. ![image-20210104203939367](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210104203939367.png)

    ​             
## 六、将所有app归拢到apps文件夹下
import sys
sys.path.insert(0,os,path.join(BASE_DIR,'apps'))

1. 将所有app移到apps文件夹下，在settings.py里将apps写入

   ![image-20210105144522743](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210105144522743.png)

2. 在articles里的models里创建两个模型类Category和Tag，并迁移

   ![image-20210105145707229](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210105145707229.png)![image-20210105145744565](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210105145744565.png)

3. 在admin里将模型类注册

   ![image-20210105150221279](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210105150221279.png)

4. 增加分类标签，给每篇文章增加分类和标签

   ![image-20210105155136445](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210105155136445.png)

5. 给页面添加访问量以及图标，将详情也也添加（single_article.html）

   ![image-20210105161353664](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210105161353664.png)

6. 给文章添加一个方法，如果有一次查看就增加一次访问量

7. 反向解析，得到每篇文章的绝对路径

## 七、评论和集成markdownfx插件
django-contrib-comments
django-markdownfy

1. 获取最新文章，获取所有分类，获取所有标签

2. 写分页`python manage.py shell` 进入shell里

   `from django.core.paginator import Paginator`

   `from articles.models import Articles`![image-20210105190250436](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210105190250436.png)

3. 写通过标题，文章内容或者摘要搜索内容



​             

