# 禁漫下载工具
#### 用于将本子下载到本地并保存为pdf
#### 基于hect0x7/JMComic-Crawler-Python二次开发的py小工具
#### https://github.com/hect0x7/JMComic-Crawler-Python

##我认为的牛逼之处
- **支持图片转化为pdf**: ~~那很方便了~~
- **支持同时保存本子标题作者等信息**: ~~纯属我吃饱了撑的~~
- **支持pdf与txt保存在同一文件夹**: ~~其实你也没有别的选择，因为我就这么做的~~
- **支持web与mobile双重爬取模式**: ~~因为有时候某个会抽风~~
- **几乎无更新**: ~~除非我很无聊~~

##如何使用
 1. 安装python，jmcomic库需python≥3.7，其实直接无脑最新版就可以了。
 2. 安装jmcomic img2pdf aiohttp三个插件，直接在终端中运行。
      ```shell
	  pip install jmcomic img2pdf aiohttp
	  ```
 3. 运行start.py。
 4. 输入1/2选择爬取方式 1=mobile 2=web mobile端不限ip兼容性好，web端限制ip地区但效率高。
 5. 输入jm数字号码，不要输入"jm"这两个英文字母，只输入数字就行。
 6. 在根目录/comic内欣赏你的本子。
 

##yml配置
其中web.yml和mobile.yml是分别用在两种爬取方式的yml，我不会在只存在一个yml的情况下直接在python程序中更换爬取方式，所以搞了这么很简单的方式。
这里是我自己针对我的yml进行的注释和实例，**还是要根据自己实际情况进行调整**

JMcomic插件官方配置文件指南（其实还是推荐你们看这个）
https://github.com/hect0x7/JMComic-Crawler-Python/blob/master/assets/docs/sources/option_file_syntax.md

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
  base_dir: .
  rule: Bd_Pname

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
  after_photo:
    # 把章节的所有图片合并为一个pdf的插件
    - plugin: img2pdf
      kwargs:
        pdf_dir: temp
        filename_rule: Aname

```
     

# 自定义txt内保存内容
## GPT告诉我的大部分变量 没猜错的话每个属性名前都要加 album.

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

在我的py程序内33行往下 （f"""xxx""")都是txt内保存内容
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

## 其他进阶用法还请到原库作者github仓库查找，还有好多功能我不会用，还请谅解
### 说点题外话
##### 这个小工具我只做了不到12小时，全程借助GPT（但是没有套用任何GPT给出的代码，纯手搓，只是报错会去问gpt）
#####我python0基础，唯一的一点知识是在高一一年的微机课学的
######~~其实跟没学没啥区别，也就只学了print input 变量赋值 while if mport~~
#####虽然不知道这个小工具会不会派上用处，但是这12小时内我学到的python知识，以及折腾的乐趣，也我收获很多，看几百遍教程也不如自己亲手搓一个来的实在。

####最后希望你们在看用我的小工具下的本子的时候，也会记起JMComic-Crawler-Python的开发者hect0x7和我这个默默无闻的python小萌新，谢谢你们的支持！

