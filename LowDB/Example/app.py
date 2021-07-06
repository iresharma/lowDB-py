from lowDB import LowDB
import os.path as p

db = LowDB(p.abspath('db.json'))
print(db.search('hi', 'bye'))