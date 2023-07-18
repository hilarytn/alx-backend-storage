#!/usr/bin/env python3
"""A function that lists all documents in a collection

   Prototype: def list_all(mongo_collection):
   Return an empty list if no document in the collection
   mongo_collection will be the pymongo collection object 
"""

def list_all(mongo_collection):
    """Return a list of documents"""
    if mongo_collection is not None:
        docs = mongo_collection.find()
        return [doc for doc in docs]
    else:
        return []
