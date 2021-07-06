from lowDB import LowDB
import os.path as p

db = LowDB(p.abspath('db.json'))
print(db)
db['hello'] = {
    'hi':'bye',
    'hi2':'bye2'
}
print(db['hello'])