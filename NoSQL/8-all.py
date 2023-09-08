#!/usr/bin/env python3
""" Task 8 """


def list_all(mongo_collection):
    cursor = mongo_collection.find({})

    data_list = []
    for data in cursor:
        data_list.append(data)

    return data_list
