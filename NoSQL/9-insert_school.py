#!/usr/bin/env python3

"""A function that insert a new document in a collection"""

def insert_school(mongo_collection, **kwargs):
    """Receiving an argument as document and insert it"""
    new_school_data = kwargs
    result = mongo_collection.insert_one(new_school_data)
    return result.inserted_id
