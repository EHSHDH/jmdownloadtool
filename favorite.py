import jmcomic
from jmcomic import *
option = jmcomic.create_option_by_file('mobile.yml')
client = option.build_jm_client()
all_aid = []
all_title = []
print("默认按照mobile.yml内账号密码获取收藏夹")
file1 = os.path.join("favorite", "jm.txt")
file2 = os.path.join("favorite", "jm-title.txt")
if os.path.isfile(file1) or os.path.isfile(file2):
    print("请删除favorite内已有的两个txt")
    input("按任意键退出程序")
else:
    mode=int(input("1保存收藏夹内所有本子 2保存特定收藏夹"))
    if mode == 1:
        for page in client.favorite_folder_gen():
            for aid, atitle in page:
                print(aid)
                all_aid.append(str(aid))
                all_title.append(atitle)
                os.makedirs(os.path.join("favorite"), exist_ok=True)
                file_path1 = os.path.join(os.path.join("favorite"), "jm-title.txt")
                file_path2 = os.path.join(os.path.join("favorite"), "jm.txt")
                with open(file_path1, "w", encoding="utf-8") as f:
                    for aid, atitle in zip(all_aid, all_title):
                        f.write(f"{aid} - {atitle}\n")  # txt内写入信息
                with open(file_path2, "w", encoding="utf-8") as f:
                    for aid, atitle in zip(all_aid, all_title):
                        f.write(f"{aid}\n")  # txt内写入信息
        input("按任意键退出程序")
    if mode == 2:
        while True:
            folder=input("请输入纯数字floder代码")
            if folder.isdigit():
                for page in client.favorite_folder_gen(folder_id={folder}):
                    for aid, atitle in page.iter_id_title():
                        print(aid)
                        all_aid.append(str(aid))
                        all_title.append(atitle)
                        os.makedirs(os.path.join("favorite"), exist_ok=True)
                        file_path1 = os.path.join(os.path.join("favorite"), "jm-title.txt")
                        file_path2 = os.path.join(os.path.join("favorite"), "jm.txt")
                        with open(file_path1, "w", encoding="utf-8") as f:
                            for aid, atitle in zip(all_aid, all_title):
                                f.write(f"{aid} - {atitle}\n")  # txt内写入信息
                        with open(file_path2, "w", encoding="utf-8") as f:
                            for aid, atitle in zip(all_aid, all_title):
                                f.write(f"{aid}\n")  # txt内写入信息
                input("按任意键退出程序")
                break




