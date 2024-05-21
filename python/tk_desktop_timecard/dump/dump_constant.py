# -*- coding: utf-8 -*-

from collections import OrderedDict

MODEL_KEYS = OrderedDict()

MODEL_KEYS["check"] = 0
MODEL_KEYS["project"] = "project"
# MODEL_KEYS["shot"] = "entity.Task.entity"
MODEL_KEYS["shot"] = "entity"
MODEL_KEYS["task"] = "entity"
MODEL_KEYS["date"] = "date"
MODEL_KEYS["hour"] = "duration"
# MODEL_KEYS["duration"] = 5
MODEL_KEYS["description"] = "description"
