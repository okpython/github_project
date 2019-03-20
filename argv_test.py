#!/usr/bin/python
#coding:utf-8

import sys
import json
import re
from collections import OrderedDict

# 发过来的数据有格式要求，而且操作系统也有要求，只能在Linux或类Unix系统下执行
# 例如： '{"name":"xiaoming"}'
# Linux环境下得到 {"name":"xiaoming"}
# win环境下得到的数据 {name:xiaoming}

def get_param():
    types = sys.argv[1]
    touser = sys.argv[2]
    message  = sys.argv[3]
    alert_dict = json.loads(message, encoding="utf-8", object_pairs_hook=OrderedDict)
    alert_dict['type'] = types
    alert_dict['touser'] = touser
    alert_str = json.dumps(alert_dict, encoding="utf-8", ensure_ascii=False).encode("utf-8")
    print(alert_str)

if __name__ == '__main__':
    get_param()
