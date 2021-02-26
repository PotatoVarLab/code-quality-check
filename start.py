# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


vocab = {
  "q": 1,
  "w": 2,
  "e": 3,
  "r": 4
}


def convert_string_to_id(text=''):
    ids = []
    for i in text:
        if i in ['q','w','e','r']:
            id = vocab.get(i, 0)
            ids.append(id)
    return ids
