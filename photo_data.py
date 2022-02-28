from csv import list_dialects
from os import dup
import database

def get_image(file : str):
    for x in database.data:
        if x['name'] == file:
            return x
    return 'Doesnt exist here!'

def get_duplicates_all():
    return ([objects for objects in database.data if database.data.count(objects) > 1])

def get_metrics():
    print("Metrics")
