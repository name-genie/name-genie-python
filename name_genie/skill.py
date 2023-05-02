from typing import List
from common import data_skill_numfix, data_skill_prefix, data_skill_suffix, data_shared_number, data_shared_clan, data_shared_action, data_shared_adj, data_shared_creature, data_shared_dao, data_shared_element, data_shared_gesture, data_shared_thing
from util import to_str
import random

__all__ = ['get_skills']

stems = data_shared_number + data_shared_clan + data_shared_action + data_shared_adj + data_shared_creature + data_shared_dao + data_shared_element + data_shared_gesture + data_shared_thing


def get_skills(count: int = 10,
               stem: str | None = None,
               prefix: str | None = None,
               suffix: str | None = None,
               numfix: str | None = None,
               position: str | None = None) -> List[str]:
    """
    生成功法
    生成算法1：[numfix] + 路 + [prefix] + (stem) + (suffix)
    生成算法2：[prefix] + (stem) + (suffix) + [numfix] + 式
    :param count: 数量
    :param stem: 词干
    :param prefix: 前缀
    :param suffix: 后缀
    :param numfix: 数字
    :param position: 数字位置: 'left' | 'right'
    :return:
    """
    names: List[str] = []
    for i in range(count):
        stem2 = stem
        prefix2 = prefix
        suffix2 = suffix
        numfix2 = numfix
        position2 = position
        if numfix2 is None and random.random() > 0.8:
            numfix2 = random.choice(data_skill_numfix)
        if prefix2 is None and random.random() > 0.8:
            prefix2 = random.choice(data_skill_prefix)
        if stem2 is None:
            stem2 = random.choice(stems)
        if suffix2 is None:
            suffix2 = random.choice(data_skill_suffix)
        if position2 is None:
            position2 = 'left' if random.random() > 0.5 else 'right'
        name = to_str(prefix2) + to_str(stem2) + to_str(suffix2)
        if numfix2 is not None and len(numfix2) > 0:
            if position2 == 'left':
                name = to_str(numfix2) + '路' + name
            else:
                name = name + to_str(numfix2) + '式'
        names.append(name)
    return names


if __name__ == '__main__':
    print(get_skills())
