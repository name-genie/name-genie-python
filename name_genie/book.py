from typing import List
from name_genie.common import data_book_state, data_book_suffix, data_book_interfix, data_shared_dao, data_shared_element, data_shared_creature, data_shared_thing, data_shared_adj, data_shared_number, data_shared_gesture, data_shared_action
from name_genie.util import to_str
import random

__all__ = ['get_books']


stems = data_shared_dao + data_shared_element + data_shared_creature + data_shared_thing + data_shared_adj + data_shared_number + data_shared_gesture + data_shared_action


def get_books(count: int = 10,
              stem: str | None = None,
              interfix: str | None = None,
              suffix: str | None = None,
              state: str | None = None) -> List[str]:
    """
    生成秘籍
    生成算法：(stem) + [(interfix)] + (suffix) + [(state)]
    :param count: 数量
    :param stem: 词干
    :param interfix: 连接
    :param suffix: 后缀
    :param state: 状态
    :return:
    """
    names: List[str] = []
    for i in range(count):
        stem2 = stem
        interfix2 = interfix
        suffix2 = suffix
        state2 = state
        if stem2 is None:
            stem2 = random.choice(stems)
        if interfix2 is None and random.random() > 0.8:
            interfix2 = random.choice(data_book_interfix)
        if suffix2 is None:
            suffix2 = random.choice(data_book_suffix)
        if state2 is None and random.random() > 0.8:
            state2 = random.choice(data_book_state)
        name = to_str(stem2) + to_str(interfix2) + to_str(suffix2)
        if state2 is not None and len(state2) > 0:
            name += f'（{state2}）'
        names.append(name)
    return names


if __name__ == '__main__':
    print(get_books())
