from typing import List
from common import data_dao_stem, data_dao_male_suffix, data_dao_female_suffix, data_shared_dao, data_shared_thing, data_shared_adj, data_shared_number
from util import to_str
import random

__all__ = ['get_daos']


stems = data_dao_stem + data_shared_dao + data_shared_thing + data_shared_adj + data_shared_number
suffixes = data_dao_male_suffix + data_dao_female_suffix


def get_daos(count: int = 10,
             gender: int | None = None,
             stem: str | None = None,
             suffix: str | None = None) -> List[str]:
    """
    生成道号
    生成算法：(stem) + (suffix)
    :param count: 数量
    :param gender: 性别: 1 - 男; 2 - 女
    :param stem: 词干
    :param suffix: 后缀
    :return:
    """
    names: List[str] = []
    for i in range(count):
        gender2 = gender
        stem2 = stem
        suffix2 = suffix
        if stem2 is None:
            stem2 = random.choice(stems)
        if suffix2 is None:
            if gender2 == 1:
                suffix2 = random.choice(data_dao_male_suffix)
            elif gender2 == 2:
                suffix2 = random.choice(data_dao_female_suffix)
            else:
                suffix2 = random.choice(suffixes)
        name = to_str(stem2) + to_str(suffix2)
        names.append(name)
    return names


if __name__ == '__main__':
    print(get_daos())
