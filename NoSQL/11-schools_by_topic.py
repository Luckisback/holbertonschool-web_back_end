#!/usr/bin/env python3

"""A function that returns the list
of school having a specific topic"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """A function that returns a list"""
    filter_query = {"topics": {"$in": [topic]}}
    result = mongo_collection.find(filter_query)
    return list(result)
