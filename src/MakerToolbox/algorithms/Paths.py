from ..utility import Discrete2DPosition
from typing import List
from math import ceil, sqrt


def compute_discrete_2d_path_differentials(start: Discrete2DPosition, end: Discrete2DPosition) -> List[Discrete2DPosition]:
    """
    Computes a discrete path between two positions relative to the start position.

    Args:
        start (Discrete2DPosition): The starting position.
        end (Discrete2DPosition): The ending position.

    Returns:
        List[Position]: A list of positions representing the computed path.

    Raises:
        Exception: If the computed path contains invalid position differentials.

    Note:
        The computed path is relative to the start position. Each position in the path
        represents a change in position (position differential) required to reach the next
        position in the path.
    """
    if start.x == end.x:
        return [Discrete2DPosition(0, 1 if start.y < end.y else -1) for _ in range(abs(end.y - start.y))]
    if start.y == end.y:
        return [Discrete2DPosition(1 if start.x < end.x else -1, 0) for _ in range(abs(end.x - start.x))]
    rebased_position = end - start
    dx = rebased_position.x
    slope = rebased_position.y / rebased_position.x
    path: List[Discrete2DPosition] = []
    prev_position = Discrete2DPosition(0, 0)
    line_length = int(ceil(sqrt(rebased_position.x ** 2 + rebased_position.y ** 2)))
    sample_dx = dx / line_length
    for sample in range(line_length + 1):
        x = int(round(sample * sample_dx))
        y = int(round(sample * sample_dx * slope))
        current_position = Discrete2DPosition(x, y)
        if current_position == prev_position:
            continue
        dp = current_position - prev_position
        if dp.x < -1 or dp.x > 1 or dp.y < -1 or dp.y > 1:
            raise Exception('Path error.')
        path.append(dp)
        prev_position = current_position
    return path
