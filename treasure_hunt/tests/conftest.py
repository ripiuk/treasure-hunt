import pytest


def treasure_maps_and_expected_paths():
    """
    Contains all the treasure maps
    with expected paths for them

    :return: treasure maps with expected paths
    """
    return (
        (((11,), ), [11]),
        (((11, 12), (21, 22)), [11]),  # treasure map: ((11, 12), (21, 22)); expected path: [11]
        (((21, 12), (21, 22)), [11, 21]),
        (((21, 12), (22, 22)), [11, 21, 22]),
        (((21, 12), (22, 12)), [11, 21, 22, 12]),
        (((22, 33, 23),
          (13, 12, 23),
          (11, 13, 21)), [11, 22, 12, 33, 21, 13, 23]),
        (((12, 13, 14, 21),
          (22, 23, 24, 31),
          (32, 33, 34, 41),
          (42, 43, 44, 44)), [11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44]),
        (((55, 14, 25, 52, 21),
          (44, 31, 11, 53, 43),
          (24, 13, 45, 12, 34),
          (42, 22, 43, 32, 41),
          (51, 23, 33, 54, 15)), [11, 55, 15, 21, 44, 32, 13, 25, 43]),
        (((66, 14, 25, 52, 21, 11),
          (44, 31, 23, 53, 43, 11),
          (24, 13, 45, 12, 34, 11),
          (42, 22, 43, 32, 41, 11),
          (51, 23, 33, 54, 15, 11),
          (12, 21, 32, 43, 53, 12)), [11, 66, 12, 14, 52, 23]),
    )


@pytest.fixture(params=treasure_maps_and_expected_paths())
def treasure_map_and_expected_path(request):
    """
    Create fixture with treasure maps and expected paths for them

    :param request: fixture with information of the requesting test function
        (https://docs.pytest.org/en/latest/reference.html#request)
    :return: current parameter
    """
    return request.param


def treasure_maps_with_loops():
    """
    Contains all the treasure maps with loops

    :return: treasure maps with loops
    """
    return (
        ((22, 12), (21, 11)),  # 22 -> 11 -> 22
        ((22, 22), (21, 12)),  # 22 -> 12 -> 22 -> 12
        ((55, 14, 25, 52, 21),
         (44, 31, 11, 53, 43),
         (24, 13, 45, 12, 34),
         (42, 22, 43, 32, 41),
         (51, 23, 33, 54, 11)),  # 11 -> 55 -> 11
        ((55, 11, 25, 52, 21),
         (44, 31, 11, 53, 43),
         (24, 13, 45, 12, 34),
         (42, 22, 43, 32, 41),
         (51, 23, 33, 54, 12)),  # 11 -> 55 -> 12 -> 11 -> 55
        ((55, 14, 25, 52, 21),
         (44, 31, 11, 53, 43),
         (24, 13, 45, 12, 34),
         (42, 22, 43, 21, 41),
         (51, 23, 33, 54, 15)),  # 11 -> 55 -> 15 -> 21 -> 44 -> 21 -> 21 -> 44
    )


@pytest.fixture(params=treasure_maps_with_loops())
def treasure_map_with_loop(request):
    """
    Create fixture for treasure maps with loops

    :param request: fixture with information of the requesting test function
        (https://docs.pytest.org/en/latest/reference.html#request)
    :return: current parameter
    """
    return request.param
