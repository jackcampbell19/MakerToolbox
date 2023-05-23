from ..utility import DiscreteVector
from typing import List
from math import ceil


def compute_discrete_path_differentials(start: DiscreteVector, end: DiscreteVector) -> List[DiscreteVector]:
    """
    Computes a discrete path between two positions relative to the start position.

    Args:
        start (DiscreteVector): The starting position.
        end (DiscreteVector): The ending position.

    Returns:
        List[Position]: A list of positions representing the computed path.

    Raises:
        Exception: If the computed path contains invalid position differentials.

    Note:
        The computed path is relative to the start position. Each position in the path
        represents a change in position (position differential) required to reach the next
        position in the path.
    """
    if start.x == end.x and start.z == end.z:
        return [DiscreteVector(0, 1 if start.y < end.y else -1, 0) for _ in range(abs(end.y - start.y))]
    if start.y == end.y and start.z == end.z:
        return [DiscreteVector(1 if start.x < end.x else -1, 0, 0) for _ in range(abs(end.x - start.x))]
    if start.x == end.x and start.y == end.y:
        return [DiscreteVector(0, 0, 1 if start.z < end.z else -1) for _ in range(abs(end.z - start.z))]
    rebased_vector = end - start
    vector_length = int(ceil(rebased_vector.magnitude()))
    path: List[DiscreteVector] = []
    prev_position = DiscreteVector(0, 0, 0)
    for i in range(vector_length + 1):
        scaled_vector = rebased_vector * (i / vector_length)
        if scaled_vector == prev_position:
            continue
        position_delta = scaled_vector - prev_position
        if position_delta.x < -1 or position_delta.x > 1 \
                or position_delta.y < -1 or position_delta.y > 1 \
                or position_delta.z < -1 or position_delta.z > 1:
            raise Exception('Path error.')
        path.append(position_delta)
        prev_position = scaled_vector
    return path
