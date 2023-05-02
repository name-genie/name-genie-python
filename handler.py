# 将data数据写入到name_genie.common内

import os
import json


# 遍历目录下所有的 JSON 文件
def traverse_json_files(dir_path):
    buf = ''
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file == 'package.json':
                continue
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                print(file_path)
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    var = file_path.replace('/', '_', -1).replace('.json', '')
                    buf += f'{var} = {data}\n\n'

    with open('name_genie/common.py', 'w', encoding='utf-8') as f:
        f.write(buf)


if __name__ == '__main__':
    traverse_json_files('data')
