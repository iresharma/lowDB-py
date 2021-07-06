import os.path as p
import fileOp.file as fileOps
from Logger.logger import Logger

logger = Logger()

class LowDB(dict):
    db = {}
    PATH = ''

    def __init__(self, path: str):
        '''
        Initialize lowDb instance, looks for an existing lowdb file
        if Found:
            found loads data into the running instance
        else:
            Creates a new file a write basic metadata to it


        params:

            path: <str> absolute path to the file
        '''
        self.PATH = path
        if p.isfile(path):
            self.db = fileOps.loadFile(path)
        else:
            self.db = fileOps.makeFile(path)
    
    def __str__(self):
        '''
            Override for default string typecaster to send the db['data']

            returns:
            
                <str>: stringify of db['data']
        '''
        return str(self.db['data'])
    
    def __getitem__(self, key):
        '''
            Override for default getItem to return the data key instead of the full db dict

            params:

                key: <str> key to gotten

            returns:
            
                <dict> | <str>: db['data'][key]
        '''
        return self.db['data'][key]

    def __setitem__(self, key, value):
        '''
            Override for default getItem to return the data key instead of the full db dict

            params:

                key: <str> key to be set
                value: <str> | <dict> | <list> value to be set
        '''
        self.db['data'][key] = value
        fileOps.updateFile(self.PATH, self.db)

    @property
    def metadata(self):
        '''
            Property decorator for metadata

            returns:
            
                <dict>: db['metaData']
        '''
        return self.db['metaData']

    def addMetadata(self, key, value):
        '''
            Function to set add metadata

            params:

                key: <str> key to be set
                value: <str> | <dict> | <list> value to be set
        '''
        self.db['metaData'][key] = value
        fileOps.updateFile(self.PATH, self.db)