from pymongo import MongoClient
from bson.objectid import ObjectId


'''
Helper function to save & load data from mongodb
'''

def save_grid(js):
	client = MongoClient()
	db = client.grid_database
	grids = db.grids
	return str(grids.insert({'js': js}))

def load_grid(mongo_id):
	client = MongoClient()
	db = client.grid_database
	grids = db.grids
	return grids.find_one({'_id': ObjectId(mongo_id)})['js']