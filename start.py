import jmcomic
import shutil
import os
import re
from jmcomic import *
while True:
    m=input("请输入爬取模式 1web 2mobile")
    if m == "1":
        option = jmcomic.create_option_by_file('web.yml')
        client = option.build_jm_client()
        break
    elif m =="2": 
        option = jmcomic.create_option_by_file('mobile.yml')
        client = option.build_jm_client()
        break
    else:
        print("请输入1或2")
        continue
def clean_title(original_title):#定义名称规则函数
    cleaned = re.sub(r'\[.*?\]|\(.*?\)|【.*?】|（.*?）', '', original_title)
    cleaned = re.sub(r'[\\/:*?"<>|]', '', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned[:255]

while True:
        mm=input("选择下载模式 1单个 2批量")
        if mm == "1":
            while True:

                sr = input("请输入数字jm号")
                if sr.isdigit():
                    album = client.get_album_detail(int(sr))
                    title = clean_title(album.title)#原始标题进行优化
                    if os.path.isdir(os.path.join("comic", title)):
                        print(f"已存在此漫画文件夹，请删除后重新运行 标题为{title}")
                        continue
                    else:
                        download_album(int(sr), option)
                        os.makedirs(os.path.join("comic", title), exist_ok=True) #新建标题为名称的文件夹
                        file_path = os.path.join(os.path.join("comic", title), f"{title}.txt") #文件夹内新建标题.txt
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(f"""漫画名称：{album.title}
漫画作者：{album.author}
漫画标签：{album.tags}
总页数：{album.page_count}
JM号：{sr}""") #txt内写入信息
                        src_file = f"tmp/{sr}.pdf"
                        dst_folder = os.path.join("comic", title)
                        os.makedirs(dst_folder, exist_ok=True) 
                        shutil.move(src_file, os.path.join(dst_folder, f"{title}.pdf")) #移动pdf到标题文件夹
                        shutil.rmtree("tmp")
                else:
                    print("请输入纯数字部分jm号")
        if mm == "2":
            import re
            def load_numbers_from_txt(filepath: str):
                with open(filepath, "r", encoding="utf-8") as f:
                    text = f.read()
                numbers = re.findall(r'\d+', text)
                return [int(num) for num in numbers]
            sr = load_numbers_from_txt("jm.txt")
            for i in sr:
                album = client.get_album_detail(int(i))
                title = clean_title(album.title)#原始标题进行优化
                if os.path.isdir(os.path.join("comic", title)):
                    print(f"已存在此漫画文件夹，请删除后重新运行  标题为{title}")
                    continue
                else:
                    download_album(int(i), option)
                    shutil.rmtree("tmp")
                    os.makedirs(os.path.join("comic", title), exist_ok=True)
                    file_path = os.path.join(os.path.join("comic", title), f"{title}.txt")
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(f"""漫画名称：{album.title}
漫画作者：{album.author}
漫画标签：{album.tags}
总页数：{album.page_count}
JM号：{i}""")
                        src_file = f"tmp/{i}.pdf"
                        dst_folder = os.path.join("comic", title)
                        os.makedirs(dst_folder, exist_ok=True) 
                        shutil.move(src_file, os.path.join(dst_folder, f"{title}.pdf")) #移动pdf到标题文件夹

        
        else:
        
            print("请输入1或2")
os.system("pause")

                    
                   
            
        

