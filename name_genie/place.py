from typing import List
from name_genie.common import data_place_suffix, data_shared_place
from name_genie.util import to_str
import random

__all__ = ['get_places']


def get_places(count: int = 10,
               length: int | None = None,
               stem: str | None = None,
               suffix: str | None = None) -> List[str]:
    """
    生成地点
    生成算法：(stem) + (suffix)
    :param count: 数量
    :param length: 词干长度
    :param stem: 词干
    :param suffix: 后缀
    :return:
    """
    names: List[str] = []
    for i in range(count):
        stem2 = stem
        suffix2 = suffix
        if stem2 is None:
            stem2 = ''
            length2 = length
            if length2 is None:
                length2 = 2 if random.random() > 0.3 else 1
            for j in range(length2):
                stem2 += random.choice(data_shared_place)
        if suffix2 is None:
            suffix2 = random.choice(data_place_suffix)
        name = to_str(stem2) + to_str(suffix2)
        names.append(name)
    return names


if __name__ == '__main__':
    print(get_places())
