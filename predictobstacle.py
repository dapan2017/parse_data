# -*- coding: utf-8 -*-
# Copyright © 2021 Li Auto. All rights reserved.

"""Obstacle data structure"""

import json
from enum import Enum
import math
import logging
from typing import Dict, List, Tuple

import numpy as np

class ObstacleType(Enum):
    VISION = 1
    LIDAR = 2
    RADAR = 3
    DEFAULT = 4


class PredictObstacle(object):
    """Obstacle class
    """

    def __init__(self, obstacle_info):
        """Init

        Args:
            obstacle_info: obstacle basic info from raw data
            mode: insert obstacle mode, eg: predicted, ground_truth
        """
        logging.info(obstacle_info)

        self.id: int = obstacle_info['id']
        self.timestamp: int = int(float(obstacle_info["stamp"])*1000)
        self.label: float = obstacle_info["label"]
        self.position_x: float = obstacle_info["pose"]["position"]["x"]
        self.position_y: float = obstacle_info["pose"]["position"]["y"]
        self.obstacle_type: int = obstacle_info['type']
