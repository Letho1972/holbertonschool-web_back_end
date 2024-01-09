#!/usr/bin/env python3

"""inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):

    """Function based on dict kwargs"""

    doc = mongo_collection.insert_one(kwargs)

    """Returns the new _id"""

    return doc.inserted_id
