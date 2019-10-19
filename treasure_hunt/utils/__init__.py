"""
Contains useful utils
"""

import typing as typ


def list_to_str(data: typ.Union[tuple, list]) -> str:
    """
    Convert list with some data to space separated string

    :param data: list with data
    :return: space separated string
    :raise ValueError: if the input data is not correct
    """
    if not data:
        raise ValueError(f'Got empty input value: {data!r}')
    if not isinstance(data, (list, tuple)):
        raise ValueError(f'Expected list or tuple, got {type(data)} instead')
    return ' '.join(map(str, data))
