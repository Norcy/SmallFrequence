# https://segmentfault.com/a/1190000010901374
import urllib.request
import urllib.parse
import requests
from pprint import pprint
import json
import shutil
import os
import time
import string

all_file = "FM_List/all.json"
ajmide_file = "FM_Ajmide_List/all.json"
intersect_file = "temp/intersect.json"
complement_ajmide_file = "temp/complement_ajmide.json"
complement_all_file = "temp/complement_all.json"

def simplifyTitle(title):
    title = title.replace(" ", "")
    title = title.replace("频率", "")
    title = title.replace("广播", "")
    title = title.replace("电台", "")
    title = title.replace("人民", "")
    return title

def isSameTitle(title1, title2):
    title1 = simplifyTitle(title1)
    title2 = simplifyTitle(title2)
    if title1 in title2:
        return True
    if title2 in title1:
        return True
    return False

if __name__ == "__main__":
    
    ajmide_list = {}
    with open(ajmide_file, 'r') as f:
        ajmide_list = json.load(f)

    all_list = {}
    with open(all_file, 'r') as f:
        all_list = json.load(f)

    # 交集
    intersect = []
    # 补集
    complement_ajmide = []

    ajmide_list = ajmide_list["data"]
    all_list = all_list["data"]

    # for item in all_list:
    #     found = False
    #     for key in ajmide_list.keys():
    #         if isSameTitle(item["title"], key):
    #             item["url"] = ajmide_list[key]
    #             found = True
    #             break
    #     if found:
    #         intersect.append(item)
    #     else:
    #         complement.append(item)

    for key in ajmide_list.keys():
        found = False
        item = ajmide_list[key]
        for item2 in all_list:
            if isSameTitle(item2["title"], key):
                item2["url"] = item
                intersect.append(item2)    
                found = True
                break
        if not found:
            complement_ajmide.append(key)


    with open(intersect_file, 'w') as f:
        json.dump(intersect, f, ensure_ascii=False, indent=1)

    with open(complement_ajmide_file, 'w') as f:
        json.dump(complement_ajmide, f, ensure_ascii=False, indent=1)

    # with open(complement_all_file, 'w') as f:
    #     json.dump(complement_all, f, ensure_ascii=False, indent=1)

