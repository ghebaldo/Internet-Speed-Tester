import os
import sys
import time
import threading
import subprocess
import re
import datetime
import math
import urllib
import urllib2
import json
import requests
import argparse

from collections import OrderedDict
from pprint import pprint

#------------------------------------------------------------------------------

def get_speed(url):
    """
    Get the download speed from a URL
    """
    start = time.time()
    try:
        urllib.urlretrieve(url, '/dev/null')
    except:
        return 0
    end = time.time()
    return (end - start) * 8 / 1000

#------------------------------------------------------------------------------

def get_speedtest():
    """
    Get the download speed from speedtest.net
    """
    url = 'http://www.speedtest.net/speedtest-config.php'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    server_config = json.loads(data)
    url = 'http://www.speedtest.net/speedtest-servers.php'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    servers = json.loads(data)
    server_list = []
    for server in servers['servers']:
        if server['country'].lower() == 'russia':
            server_list.append(server)
    best_server = None
    for server in server_list:
        if not best_server:
            best_server = server
        elif server['latency'] < best_server['latency']:
            best_server = server
    url = '%s/latency.txt' % best_server['url']
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    time_list = data.split('\n')
    time_list.pop()
    time_list = [float(time) for time in time_list]
    time_list.sort()
    median_time = time_list[len(time_list) / 2]
    url = '%s/latency.txt' % best_server['url']
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    time_list = data.split('\n')
    time_list.pop()
    time_list = [float(time) for time in time_list]
    time_list.sort()
    median_time = time_list[len(time_list) / 2]
    url = '%s/download.php?x=%s' % (best_server['url'], urllib.quote_plus(str(datetime.datetime.now())))
    download_speed = get_speed(url)
    url = '%s/upload.php?x=%s' % (best_server['url'], urllib.quote_plus(str(datetime.datetime.now())))
    upload_speed = get_speed(url)
    return download_speed, upload_speed

#------------------------------------------------------------------------------

def get_speed_from_net_monitor():
    """
    Get the download speed from a network monitor
    """
    url = 'http://www.speedtest.net/my-result/'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    download_speed = float(re.findall('Download: (.*?) Mbit', data)[0])
    upload_speed = float(re.findall('Upload: (.*?) Mbit', data)[0])
    return download_speed, upload_speed

#------------------------------------------------------------------------------

def get_speed_from_speedtest():
    """
    Get the download speed from speedtest.net
    """
    url = 'http://www.speedtest.net/speedtest-config.php'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    server_config = json.loads(data)
    url = 'http://www.speedtest.net/speedtest-servers.php'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    servers = json.loads(data)
    server_list = []
    for server in servers['servers']:
        if server['country'].lower() == 'russia':
            server_list.append(server)
    best_server = None
    for server in server_list:
        if not best_server:
            best_server = server
        elif server['latency'] < best_server['latency']:
            best_server = server
    url = '%s/latency.txt' % best_server['url']
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    time_list = data.split('\n')
    time_list.pop()
    time_list = [float(time) for time in time_list]
    time_list.sort()
    median_time = time_list[len(time_list) / 2]
    url = '%s/latency.txt' % best_server['url']
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    time_list = data.split('\n')
    time_list.pop()
    time_list = [float(time) for time in time_list]
    time_list.sort()
    median_time = time_list[len(time_list) / 2]
    url = '%s/download.php?x=%s' % (best_server['url'], urllib.quote_plus(str(datetime.datetime.now())))
    download_speed = get_speed(url)
    url = '%s/upload.php?x=%s' % (best_server['url'], urllib.quote_plus(str(datetime.datetime.now())))
    upload_speed = get_speed(url)
    return download_speed, upload_speed

#------------------------------------------------------------------------------

def get_speed_from_speedtest_cli():
    """
    Get the download speed from speedtest.net
    """
    url = 'http://speedtest.net/speedtest-config.php'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    server_config = json.loads(data)
    url = 'http://speedtest.net/speedtest-servers.php'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    servers = json.loads(data)
    server_list = []
    for server in servers['servers']:
        if server['country'].lower() == 'russia':
            server_list.append(server)
    best_server = None
    for server in server_list:
        if not best_server:
            best_server = server
        elif server['latency'] < best_server['latency']:
            best_server = server
    url = '%s/latency.txt' % best_server['url']
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    time_list = data.split('\n')
    time_list.pop()
    time_list = [float(time) for time in time_list]
    time_list.sort()
    median_time = time_list[len(time_list) / 2]
    url = '%s/latency.txt' % best_server['url']
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    time_list = data.split('\n')
    time_list.pop()
    time_list = [float(time) for time in time_list]
    time_list.sort()
    median_time = time_list[len(time_list) / 2]
    url = '%s/download.php?x=%s' % (best_server['url'], urllib.quote_plus(str(datetime.datetime.now())))
    download_speed = get_speed(url)
    url = '%s/upload.php?x=%s' % (best_server['url'], urllib.quote_plus(str(datetime.datetime.now())))
    upload_speed = get_speed(url)
    return download_speed, upload_speed

#------------------------------------------------------------------------------

def get_speed_from_fast_com():
    """
    Get the download speed from fast.com
    """
    url = 'https://fast.com/'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    start_string = '<div id="speed-value">'
    end_string = '<div id="speed-units">'
    start = data.find(start_string) + len(start_string)
    end = data.find(end_string)
    download_speed = float(data[start:end])
    start_string = '<div id="upload-value">'
    end_string = '<div id="upload-units">'
    start = data.find(start_string) + len(start_string)
    end = data.find(end_string)
    upload_speed = float(data[start:end])
    return download_speed, upload_speed

#------------------------------------------------------------------------------

def get_speed_from_fast_com_v2():
    """
    Get the download speed from fast.com
    """
    url = 'https://fast.com/'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    start_string = '<div id="speed-value">'
    end_string = '<div id="speed-units">'
    start = data.find(start_string) + len(start_string)
    end = data.find(end_string)
    download_speed = float(data[start:end])
    start_string = '<div id="upload-value">'
    end_string = '<div id="upload-units">'
    start = data.find(start_string) + len(start_string)
    end = data.find(end_string)
    upload_speed = float(data[start:end])
    return download_speed, upload_speed

#------------------------------------------------------------------------------

def get_speed_from_fast_com_v3():
    """
    Get the download speed from fast.com
    """
    url = 'https://fast.com/'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    start_string = '<div id="speed-value">'
    end_string = '<div id="speed-units">'
    start = data.find(start_string) + len(start_string)
    end = data.find(end_string)
    download_speed = float(data[start:end])
    start_string = '<div id="upload-value">'
    end_string = '<div id="upload-units">'
    start = data.find(start_string) + len(start_string)
    end = data.find(end_string)
    upload_speed = float(data[start:end])
    return download_speed, upload_speed

#------------------------------------------------------------------------------

def get_speed_from_fast_com_v4():
    """
    Get the download speed from fast.com
    """
    url = 'https://fast.com/'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    start_string = '<div id="speed-value">'
    end_string = '<div id="speed-units">'
    start = data.find(start_string) + len(start_string)
    end = data.find(end_string)
    download_speed = float(data[start:end])
    start_string = '<div id="upload-value">'
    end_string = '<div id="upload-units">'
    start = data.find(start_string) + len(start_string)
    end = data.find(end_string)
    upload_speed = float(data[start:end])
    return download_speed, upload_speed

#------------------------------------------------------------------------------

def get_speed_from_fast_com_v5():
    """
    Get the download speed from fast.com
    """
    url = 'https://fast.com/'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    start_string = '<div id="speed-value">'
    end_string = '<div id="speed-units">'
    start = data.find(start_string) + len(start_string)
    end = data.find(end_string)
    download_speed = float(data[start:end])
    start_string = '<div id="upload-value">'
    end_string = '<div id="upload-units">'
    start = data.find(start_string) + len(start_string)
    end = data.find(end_string)
    upload_speed = float(data[start:end])
    return download_speed, upload_speed

#------------------------------------------------------------------------------

def get_speed_from_fast_com_v6():
    """
    Get the download speed from fast.com
    """
    url = 'https://fast.com/'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    start_string = '<div id="speed-value">'
    end_string = '<div id="speed-units">'
    start = data.find(start_string) + len(start_string)
    end = data.find(end_string)
    download_speed = float(data[start:end])
    start_string = '<div id="upload-value">'
    end_string = '<div id="upload-units">'
    start = data.find(start_string) + len(start_string)
    end = data.find(end_string)
    upload_speed = float(data[start:end])
    return download_speed, upload_speed
