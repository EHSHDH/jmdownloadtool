import jmcomic
import shutil
import os
from jmcomic import *
option = jmcomic.create_option_by_file('mobile.yml')
client = option.build_jm_client()
n=[1.2]
while True:
    m=input("请输入爬取模式 1web 2mobile")
    if m == "1":
        option = jmcomic.create_option_by_file('mobile.yml')
        break
    elif m =="2": 
        option = jmcomic.create_option_by_file('web.yml')
        break
    else:
        print("请输入1或2")
        continue
while True:
    sr = input("请输入数字jm号")
    if sr.isdigit():
        album = client.get_album_detail(int(sr))
        if os.path.isdir(os.path.join("comic", album.title)):
            print("已存在此漫画文件夹，请删除后重新运行")
            continue
        else:
            download_album(int(sr), option)
            shutil.rmtree(album.title) #删除根目录下jpg缓存文件夹
            folder_name = f"{album.title}"
            os.makedirs(os.path.join("comic", album.title), exist_ok=True) #新建标题为名称的文件夹
            file_path = os.path.join(os.path.join("comic", album.title), f"{album.title}.txt") #文件夹内新建标题.txt
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"""漫画名称：{album.title}
漫画作者：{album.author}
漫画标签：{album.tags}
总页数：{album.page_count}
JM号：{sr}""") #txt内写入信息
            src_file = f"temp/{album.title}.pdf"
            dst_folder = os.path.join("comic", album.title)
            os.makedirs(dst_folder, exist_ok=True) 
            shutil.move(src_file, os.path.join(dst_folder, os.path.basename(src_file))) #移动pdf到标题文件夹
    else:
        print("请输入纯数字部分jm号")
