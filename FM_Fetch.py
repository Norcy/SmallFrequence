# https://segmentfault.com/a/1190000010901374
import urllib.request
import urllib.parse
import requests
from pprint import pprint
import json
import shutil
import os

region_url = 'https://rapi.qingting.fm/regions'

categories_url = 'https://rapi.qingting.fm/categories/{}/channels?with_total=true&pagesize=50&page={}'

root_director = "FM_List"

def doRequests(url):
    print(url)
    r = requests.get(url)
    jsonResult = r.json()
    # pprint(jsonResult)
    return jsonResult
    
def request_channels_single_page(regionId, pageIndex):
    result = doRequests(categories_url.format(regionId, pageIndex))
    return result["Data"]

def request_channels(regionId):
    pageIndex = 1
    requstChannelCount = 0
    channelCount = 1
    channels = []
    while channelCount > requstChannelCount:
        result = request_channels_single_page(regionId, pageIndex)
        channelCount = result["total"]
        channels += result["items"]
        requstChannelCount += len(channels)
        pageIndex += 1

    return channels

def simplifyChannel(channel):
    simplifiedChannel = {}
    channelId = channel["content_id"]
    simplifiedChannel["content_id"] = channelId;
    simplifiedChannel["title"] = channel["title"];
    simplifiedChannel["url"] = 'http://ls.qingting.fm/live/{}/64k.m3u8'.format(channelId);
    return simplifiedChannel

def simplifyChannels(channels):
    simplifiedChannels = []
    for channel in channels:
        simplifiedChannels.append(simplifyChannel(channel))
    return simplifiedChannels

def request_regions():
    result = doRequests(region_url)
    return result["Data"]

if __name__ == "__main__":
    regions = request_regions()
    
    if os.path.exists(root_director):
        shutil.rmtree(root_director)    
    os.mkdir(root_director)

    with open(root_director+'/regions.json', 'w') as f:
        json.dump(regions, f, ensure_ascii=False)

    # pprint(regions)
    for region in regions:
        regionId = region["id"]
        regionTitle = region["title"]
        channels = request_channels(regionId)
        simplifiedChannels = simplifyChannels(channels)
        # pprint(len(channels))
        with open(root_director+'/{}.json'.format(regionId), 'w') as f:
            json.dump(simplifiedChannels, f, ensure_ascii=False)