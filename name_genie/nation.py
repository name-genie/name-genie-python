from typing import List
from name_genie.common import data_nation_interfix, data_nation_suffix, data_shared_place
from name_genie.util import to_str
import random

__all__ = ['get_nations']


def get_nations(count: int = 10,
                length: int | None = None,
                stem: str | None = None,
                interfix: str | None = None,
                suffix: str | None = None) -> List[str]:
    """
    生成国家
    生成算法：(stem) + [interfix] + (suffix)
    :param count: 数量
    :param length: 词干长度
    :param stem: 词干
    :param interfix: 连接
    :param suffix: 后缀
    :return:
    """
    names: List[str] = []
    for i in range(count):
        stem2 = stem
        interfix2 = interfix
        suffix2 = suffix
        if suffix2 is None:
            suffix2 = random.choice(data_nation_suffix)
        if interfix2 is None and random.random() > 0.8:
            interfix2 = random.choice(data_nation_interfix)
        suffix2 = to_str(interfix2) + to_str(suffix2)

        if stem2 is None:
            stem2 = ''
            length2 = length
            if length2 is None:
                length2 = 2 if random.random() > 0.5 else 1
                if len(suffix2) == 2:
                    length2 = 2
            for j in range(length2):
                stem2 += random.choice(data_shared_place)

        name = to_str(stem2) + to_str(suffix2)
        names.append(name)
    return names


if __name__ == '__main__':
    print(get_nations())
