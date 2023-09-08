#!/usr/bin/env python3
""" Task 8 """


def list_all(mongo_collection):
    """
    Python function that lists,
    all documents in a collection
    Params:
    mongo_collection: pymongo collection object
    Returns:
    list of dictionaries with the data from each document.
    """
    cursor = mongo_collection.find({})

    data_list = []
    for data in cursor:
        data_list.append(data)

    return data_list
