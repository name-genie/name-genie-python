from typing import List
from common import data_name_prefix, data_name_interfix, data_name_male_suffix, data_name_female_suffix
from util import to_str
import random

__all__ = ['get_names']


interfixes = data_name_male_suffix + data_name_female_suffix + data_name_interfix

suffixes = data_name_male_suffix + data_name_female_suffix


def get_names(count: int = 10,
              gender: int | None = None,
              length: int | None = None,
              prefix: str | None = None,
              suffix: str | None = None) -> List[str]:
    """
    生成名字
    生成算法：(prefix) + (suffix)
    :param count: 数量
    :param gender: 性别: 1 - 男; 2 - 女
    :param length: 名字长度
    :param prefix: 前缀
    :param suffix: 后缀
    :return:
    """
    names: List[str] = []
    for i in range(count):
        gender2 = gender
        length2 = length
        prefix2 = prefix
        suffix2 = suffix
        if prefix2 is None:
            prefix2 = random.choice(data_name_prefix)
        if suffix2 is None:
            suffix2 = ''
            if length2 is None:
                length2 = 2 if random.random() > 0.5 else 1
            if length2 == 2:
                if gender2 == 1:
                    suffix2 += random.choice(data_name_male_suffix)
                elif gender2 == 2:
                    suffix2 += random.choice(data_name_female_suffix)
                else:
                    suffix2 += random.choice(interfixes)
                length2 -= 1
            for j in range(length2):
                if gender2 == 1:
                    suffix2 += random.choice(data_name_male_suffix)
                elif gender2 == 2:
                    suffix2 += random.choice(data_name_female_suffix)
                else:
                    suffix2 += random.choice(interfixes)
        name = to_str(prefix2) + to_str(suffix2)
        names.append(name)
    return names


if __name__ == '__main__':
    print(get_names())
