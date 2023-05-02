from typing import List
from common import data_material_state, data_material_suffix, data_shared_dao, data_shared_element, data_shared_color, data_shared_creature, data_shared_thing, data_shared_adj, data_shared_number, data_shared_gesture, data_shared_action
from util import to_str
import random

__all__ = ['get_materials']


stems = data_shared_dao + data_shared_element + data_shared_color + data_shared_creature + data_shared_thing + data_shared_adj + data_shared_number + data_shared_gesture + data_shared_action


def get_materials(count: int = 10,
                  stem: str | None = None,
                  suffix: str | None = None,
                  state: str | None = None) -> List[str]:
    """
    生成材料
    生成算法：(stem) + (suffix) + [(state)]
    :param count: 数量
    :param stem: 词干
    :param suffix: 后缀
    :param state: 状态
    :return:
    """
    names: List[str] = []
    for i in range(count):
        stem2 = stem
        suffix2 = suffix
        state2 = state
        if stem2 is None:
            stem2 = random.choice(stems)
        if suffix2 is None:
            suffix2 = random.choice(data_material_suffix)
        if state2 is None and random.random() > 0.8:
            state2 = random.choice(data_material_state)
        name = to_str(stem2) + to_str(suffix2)
        if state2 is not None and len(state2) > 0:
            name += f'（{state2}）'
        names.append(name)
    return names


if __name__ == '__main__':
    print(get_materials())
