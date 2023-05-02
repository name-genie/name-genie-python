from typing import List
from name_genie.common import data_creature_interfix, data_creature_suffix, data_shared_action, data_shared_adj, data_shared_creature, data_shared_dao, data_shared_element, data_shared_gesture, data_shared_thing
from name_genie.util import to_str
import random

__all__ = ['get_creatures']

stems = data_shared_action + data_shared_adj + data_shared_creature + data_shared_dao + data_shared_element + data_shared_gesture + data_shared_thing


def get_creatures(count: int = 10,
                  stem: str | None = None,
                  interfix: str | None = None,
                  suffix: str | None = None) -> List[str]:
    """
    生成生灵
    生成算法：(stem) + [(interfix)] + (suffix)
    :param count: 数量
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
        if stem2 is None:
            stem2 = random.choice(stems)
        if interfix2 is None and random.random() > 0.8:
            interfix2 = random.choice(data_creature_interfix)
        if suffix2 is None:
            suffix2 = random.choice(data_creature_suffix)
        name = to_str(stem2) + to_str(interfix2) + to_str(suffix2)
        names.append(name)
    return names


if __name__ == '__main__':
    print(get_creatures())
