# -*- coding: utf-8 -*-

import os
import yaml
from pathlib import Path

now_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # 获取到项目的根目录位置
dir_path = Path(now_path, "./datas")  # 当前文件位置 拼装 Logs 形成工作目录
log_path = dir_path.resolve()   # 返回文件路径



# print(now_path)
# print(dir_path)
# print(log_path)

with open(f"{log_path}\\abc.yml") as f:
    print(yaml.safe_load(f))