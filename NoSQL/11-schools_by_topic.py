#!/usr/bin/env python3
""" Task 11 """


def schools_by_topic(mongo_collection, topic):
    """function that returns the list
    of school having a specific topic:"""
    cursor = mongo_collection.find({"topics": topic})
    matches = []
    for school in cursor:
        matches.append(school)
    return school
