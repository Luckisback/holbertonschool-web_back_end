#!/usr/bin/env python3

""" A function that lists all document in a collection"""

import pymongo


def list_all(mongo_collection):
    """ Defintion of the function"""
    if not db.mongo_collection.count()
        return []
    return list(db.mongo_collection.find())
