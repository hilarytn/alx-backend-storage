#!/usr/bin/env python3
"""A function that lists all documents in a collection"""
def list_all(mongo_collection):
    my_list = []
    if mongo_collection.find() is not None:
        docs = mongo_collection.find()
        return [doc for doc in docs]
    else:
        return my_list
