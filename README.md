# 禁漫下载工具
#### 用于将本子下载到本地并保存为pdf
#### 基于hect0x7/JMComic-Crawler-Python二次开发的py小工具
#### [JMComic-Crawler-Python](https://github.com/hect0x7/JMComic-Crawler-Python "JMComic-Crawler-Python")

## 我认为的牛逼之处
- **支持图片转化为pdf**: ~~那很方便了~~
- **支持同时保存本子标题作者等信息**: ~~纯属我吃饱了撑的~~
- **支持pdf与txt保存在同一文件夹**: ~~其实你也没有别的选择，因为我就这么做的~~
- **支持web与mobile双重爬取模式**: ~~因为有时候某个会抽风~~
- **支持批量下载**: ~~一个一个下载真的很麻烦~~
- **自动优化标题**: ~~被windows命名规范搞死了~~
- **几乎无更新**: ~~除非我很无聊~~

## 准备阶段
  1. 安装python，jmcomic库需python≥3.7，其实直接无脑最新版就可以了。
  2. 安装jmcomic img2pdf aiohttp三个插件，直接在终端中运行。
      ```shell
	  pip install jmcomic img2pdf aiohttp
	  ```
  3. 解压jmdownloadtoolv1.x.zip，并将其中两个yml配置文件中的ur pd改为自己的jm用户名，密码（必须）。

### 如何下载本子
 3. 运行start.py。
 4. 输入1/2选择爬取方式 1=mobile 2=web mobile端不限ip兼容性好，web端限制ip地区但效率高。
 5. 输入1/2选择批量还是单个下载。
 6. 若选择1单个，则输入jm数字号码，不要输入"jm"这两个英文字母，只输入数字就行。
 7. 若选择2批量，则在根目录jm.txt内输入你要下载的所有本子的jm号，可以用空格，换行，逗号等乱七八糟的方式分隔。
 8. 在 根目录/comic 内欣赏你的本子。

### 对于批量下载
使用GitHubActions保存收藏夹教程
[导出收藏夹数据](https://github.com/hect0x7/JMComic-Crawler-Python/blob/master/assets/docs/sources/tutorial/10_export_favorites.md "导出收藏夹数据")

已更新保存收藏夹功能,用法：
1. 在mobile/web中填写ur pd。
2. 运行favorite.py。
3. 保存所有收藏夹则选择1模式，保存特定分组文件夹则选择2模式。
4. 若选择2模式则提示你输入floder代码，打开你的特定文件夹，地址栏显示
`https://jm域名/user/你的名字/favorite/albums?folder=你的folder代码`
则输入folder=后面的部分。
5. 我设置的是保存为jm.txt和jm-title.txt，均保存在根目录内favorite文件夹
前者只包含jm号，后者包含jm号和漫画标题，方便后期对比。
6. 运行前记得清除favorite内两个txt文件，否则无法正常运行程序。
7. 若有时保存的收藏夹明显少于实际内容，请自行将favorite.py中
```python
option = jmcomic.create_option_by_file('mobile.yml')
```
mobile.yml修改为web.yml


 ### 文件结构

| 名称          | 说明                                 |
|---------------|--------------------------------------|
| `comic/`      | 存储漫画文件夹                       |
| `tmp/`       | 存储本子源文件文件夹和转换过后的pdf         |
| `favorite/`  | 存储收藏夹保存内容                   |
| `favorite/jm.txt`  | 只保存jm号的收藏夹保存文件                   |
| `favorite/`  | 保存jm号结合标题的收藏夹保存文件                   |
| `mobile.yml`  | 用于 mobile 模式的配置文件           |
| `web.yml`     | 用于 web 模式的配置文件              |
| `start.py`    | 启动程序                         |
| `favorite.py`    | 保存收藏夹程序                             |
| `库前置.cmd`  | 一键安装三个前置库                   |
| `jm.txt`  | 你要批量下载的本子jm号                   |


 

##yml配置
其中web.yml和mobile.yml是分别用在两种爬取方式的yml，我不会在只存在一个yml的情况下直接在python程序中更换爬取方式，所以搞了这么很简单的方式。
这里是我自己针对我的yml进行的注释和实例，**还是要根据自己实际情况进行调整**

JMcomic插件官方配置文件指南（其实还是推荐你们看这个）
[配置文件指南](https://github.com/hect0x7/JMComic-Crawler-Python/blob/master/assets/docs/sources/option_file_syntax.md "配置文件指南")

```yml
client:
  cache: null
  domain:
    html:
      #下面都是jm的域名，也可以根据你自己的网络环境进行调整 优先用最上面的
      - jmcomic-zzz.one
      - jmcomic-zzz.org
      - 18comic.vip
      - 18comic.org
      - jm18c-zxc.org
      - jm18c-zxc.cc
      - jm18c-zxc.net
    api:
      - www.jmapiproxyxxx.vip
        #这是移动端的接口
  impl: html
  # html网页 api移动端
  postman:
    meta_data:
      headers: null
      impersonate: chrome
      proxies:
        #顾名思义代理
        http: 127.0.0.1:7890
        https: 127.0.0.1:7890
    type: curl_cffi
  retry_times: 5

dir_rule:
#本子jpg保存路径/名称
  base_dir: tmp
  rule: Bd_Aid

download:
  cache: true
  impl: aiohttp
  # 可选: requests（默认）、aiohttp（更快，需安装） 这是gpt告诉我的
  chunk_size: 8192
  #数据块大小 单位字节
  image:
    decode: true
    suffix: .jpg
    # 若设置为null则保存为webp 转换为pdf文件体积极大 jpg无此问题
  threading:
    # 线程数 章节/图片
    image: 4
    photo: 4

log: true

plugins:
  valid: log

version: '2.67'

plugins:
   after_init:
    - plugin: login # 登录插件
      kwargs:
        username: ur # 用户名
        password: pd # 密码
  after_photo:
    # 把章节的所有图片合并为一个pdf的插件
    - plugin: img2pdf
      kwargs:
	  #pdf保存路径/名称
        pdf_dir: tmp
        filename_rule: Aid

```
     

# 自定义txt内保存内容
## GPT告诉我的大部分变量 每个属性名前都要加 album.
因为我我用了
```python
album = client.get_album_detail（）
```
另外，不确定每个变量都是可用的，因为我不会总结，但是90%还是可以用的。

| 属性名             | 类型                   | 说明               |
| --------------- | -------------------- | ---------------- |
| `album_id`      | int                  | 漫画 ID            |
| `title`         | str                  | 漫画标题             |
| `author`        | str                  | 作者               |
| `tags`          | list\[str]           | 漫画标签             |
| `cover_url`     | str                  | 封面图片 URL         |
| `page_count`    | int                  | 总页数              |
| `chapter_count` | int                  | 章节数量             |
| `description`   | str                  | 漫画简介（可为空）        |
| `upload_date`   | str / datetime       | 上传日期             |
| `series_name`   | str                  | 系列名称（可为空）        |
| `type_name`     | str                  | 漫画类型（如“恋爱”）      |
| `language`      | str                  | 漫画语言             |
| `status`        | str                  | 漫画状态（连载 / 完结）    |
| `source`        | str                  | 漫画来源             |
| `photos`        | list\[JmPhotoDetail] | 漫画图片列表，每张图片是一个对象 |

在我的py程序内（f"""xxx""")都是txt内保存内容
```python
f.write(f"""漫画名称：{album.title}
漫画作者：{album.author}
漫画标签：{album.tags}
总页数：{album.page_count}
JM号：{sr}""")
# 变量值可以在这里通过 {变量名} 直接输出到txt内
# 比如我还想在里面加入漫画简介 可以直接在里面换行加入
# 简介：{album.description}
```

### 另外一些注意事项
1. 这个小工具单个下载本子流程是 
输入jm号并检测是不是纯数字
定义album变量
检测comic内有无已存在的此本子文件夹，若有请删除
运行download_album（这一步默认是下载本子图片，保存在py和yml根目录内以本子标题为名称的文件夹内）
自动转换为pdf,保存在tmp
删除上面提到的这个文件夹（懒得手动删总之我要的是pdf）
在comic内新建本子文件夹
新建txt并写入信息
将tmp内pdf移动到comic/标题 文件夹中
继续下一次循环
仅供参考，可以做解决问题思路

2. 此条仅适合v1.1 更新后1.2应该解决了这个些问题
~~如果你批量出现报错，我提供的解决方案是
comic内找到你成功下载的最后一个本子a
在txt内删掉这个a本子的后面本子的jm号
有些本子可能是标题内有特殊符号问题。无论是批量还是单个都无法下载成功，懒得研究解决方案，有大佬知道的话可以提个建议，谢谢。~~

3. 关于标题优化 v1.2
大部分批量下载中报错，大概都是因为文件名/路径名问题。windows文件名称中一些符号无法使用，因此借助正则表达式优化了标题，例子如下

 (無修完整版) [VYCMa]蒙德温泉节 第二幕
 蒙德温泉节 第二幕
 
 并因为这个原因 在yml中修改了图片文件夹名称，路径，pdf文件名称，路径
 名称均改为jm的数字id，路径均改为/tmp，最大限度避免命名问题


## 其他进阶用法还请到原库作者github仓库查找，还有好多功能我不会用，还请谅解
### 说点题外话 v1.0
##### 这个小工具我只做了不到12小时，全程借助GPT（但是没有套用任何GPT给出的代码，纯手搓，只是报错会去问gpt）
#####我python0基础，唯一的一点知识是在高一一年的微机课学的
######~~其实跟没学没啥区别，也就只学了print input 变量赋值 while if mport~~
#####虽然不知道这个小工具会不会派上用处，但是这12小时内我学到的python知识，以及折腾的乐趣，也我收获很多，看几百遍教程也不如自己亲手搓一个来的实在。

####最后希望你们在看用我的小工具下的本子的时候，也会记起JMComic-Crawler-Python的开发者hect0x7和我这个默默无闻的python小萌新，谢谢你们的支持！

