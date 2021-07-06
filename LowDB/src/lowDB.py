import os.path as p
import fileOp.file as fileOps
from Logger.logger import Logger
import Errors.lowDBExceptions as exceptions 

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
    
    def __str__(self) -> str:
        '''
            Override for default string typecaster to send the db['data']

            returns:
            
                <str>: stringify of db['data']
        '''
        return str(self.db['data'])
    
    def __getitem__(self, key) -> (dict or int or bool or list):
        '''
            Override for default getItem to return the data key instead of the full db dict

            params:

                key: <str> key to gotten

            returns:
            
                <dict> | <str>: db['data'][key]
        '''
        return self.db['data'][key]

    def __setitem__(self, key, value) :
        '''
            Override for default getItem to return the data key instead of the full db dict

            params:

                key: <str> key to be set
                value: <str> | <dict> | <list> value to be set
        '''
        self.db['data'][key] = [value]
        fileOps.updateFile(self.PATH, self.db)

    def __iter__(self) -> iter:
        return iter(self.db['data'].keys())

    def __repr__(self) -> str:
        metadata = self.metadata
        logger.success('=============== <class "lowDB.LowDB"> ===============')
        logger.info("", data=metadata)
        return f'Collections: {len(self.db["data"].keys())}'

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

    def search(self,  key: str, val, collection: str=None, subDict: dict=None) -> (dict or list or str or int):
        if collection:
            try:
                all = self.db['data'][collection]
                if type(all) == dict:
                    return all[key] if all[key] == val else None
                elif type(all) == list:
                    for i in all:
                        if i[key] == val:
                            return i[key]
                    return None
            except KeyError:
                logger.error(f"search failed: {collection} not found")
                raise KeyError
        elif subDict:
            if type(subDict) == dict:
                return subDict[key] if subDict[key] == val else None
            elif type(subDict) == list:
                for i in subDict:
                    if i[key] == val:
                        return i[key]
                return None
        else:
            logger.error("Provide either a subDict or a collection")
            raise exceptions.InvalidSearchArgsError