#!/usr/bin/env python3

"""A Python function that changes
all topics based on the name"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """ Receiving name whitch will concerned by the change"""
    filter_query = {"name": name}
    update_data = {"$set": {"topics": topics}}
    mongo_collection.update_one(filter_query, update_data)
