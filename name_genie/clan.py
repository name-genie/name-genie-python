from typing import List
from common import data_clan_suffix, data_shared_action, data_shared_adj, data_shared_creature, data_shared_dao, data_shared_element, data_shared_gesture, data_shared_thing
from util import to_str
import random

__all__ = ['get_clans']

stems = data_shared_action + data_shared_adj + data_shared_creature + data_shared_dao + data_shared_element + data_shared_gesture + data_shared_thing


def get_clans(count: int = 10,
              stem: str | None = None,
              suffix: str | None = None) -> List[str]:
    """
    生成门派
    生成算法：(stem) + (suffix)
    :param count: 数量，默认10
    :param stem: 词干
    :param suffix: 词尾
    :return:
    """
    names: List[str] = []
    for i in range(count):
        stem2 = stem
        suffix2 = suffix
        if stem2 is None:
            stem2 = random.choice(stems)
        if suffix2 is None:
            suffix2 = random.choice(data_clan_suffix)
        name = to_str(stem2) + to_str(suffix2)
        names.append(name)
    return names


if __name__ == '__main__':
    print(get_clans())
