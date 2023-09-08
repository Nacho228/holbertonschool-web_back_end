#!/usr/bin/env python3
""" Task 9 """


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document
    in a collection based on kwargs:

    Args:
        mongo_collection: pymongo collection object
        **kwargs: key-value pairs of fields and,
        values to be inserted into the database.
    Return:
        The new _id
    """
    cursor = mongo_collection.insert_one(kwargs)
    return cursor.inserted_id
