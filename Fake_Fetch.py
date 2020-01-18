# https://segmentfault.com/a/1190000010901374
import urllib.request
import urllib.parse
import requests
from pprint import pprint
import json
import shutil
import os
import time
import datetime

region_url = 'https://api.psy-1.com/miniapp/v1/music/tag'

categories_url = 'https://api.psy-1.com/miniapp/v1/tag/music?tag_id={}'

root_director = "Fake_List"

fake_group_prefix = -100000

def doRequests(url):
    print(url)
    payload = {"version" : "6", "platformid":"3",
    "token":"5d4d03be06a264e71043593676753228", 
    "packageid" : "12"}
    r = requests.get(url, headers=payload)
    jsonResult = r.json()
    # pprint(jsonResult)
    return jsonResult
    
def request_channels(regionId):
    result = doRequests(categories_url.format(-regionId+fake_group_prefix))
    return result["data"]

def simplifyChannel(regionId, channel):
    simplifiedChannel = {}
    simplifiedChannel["content_id"] = fake_group_prefix-channel["id"];
    simplifiedChannel["title"] = channel["musicdesc"];
    simplifiedChannel["url"] = channel["musicurl"];
    # simplifiedChannel["poster"] = channel["cover_miniapp_big"];
    simplifiedChannel["group_id"] = regionId
    return simplifiedChannel

def simplifyChannels(regionId, channels):
    simplifiedChannels = []
    for channel in channels:
        simplifiedChannels.append(simplifyChannel(regionId, channel))
    return simplifiedChannels

def simplifyRegion(region):
    # pprint(region)
    simplifiedRegion = {}
    simplifiedRegion["title"] = region["tag_name"]
    simplifiedRegion["id"] = fake_group_prefix-region["tag_id"];
    return simplifiedRegion;

def request_regions():
    simplifiedRegions = []
    regions = doRequests(region_url)["data"]
    for region in regions:
        if region["tag_id"] == 1:
            continue
        simplifiedRegions.append(simplifyRegion(region))
    return simplifiedRegions

if __name__ == "__main__":
   
    d = datetime.datetime.fromtimestamp(time.time())
    print(d.strftime("%Y-%m-%d %H:%M:%S.%f"))
 
    regions = request_regions()

    absolute_root_director = os.path.split(os.path.realpath(__file__))[0]+"/"+root_director;
    # print(absolute_root_director);

    if os.path.exists(absolute_root_director):
        shutil.rmtree(absolute_root_director)    
    os.mkdir(absolute_root_director)

    version = int(time.time()/2);
    finalRegions = {};
    finalRegions["version"] = version;
    finalRegions["data"] = regions;
    with open(absolute_root_director+'/regions.json', 'w') as f:
        json.dump(finalRegions, f, ensure_ascii=False)

    allChannels = [];
    for region in regions:
        regionId = region["id"]
        regionTitle = region["title"]
        channels = request_channels(regionId)
        simplifiedChannels = simplifyChannels(regionId, channels)
        allChannels += simplifiedChannels;
    
    finalChannels = {};
    finalChannels["version"] = version;
    finalChannels["data"] = allChannels;
    with open(absolute_root_director+'/all.json', 'w') as f:
        json.dump(finalChannels, f, ensure_ascii=False, indent=4, separators=(',', ':'))
