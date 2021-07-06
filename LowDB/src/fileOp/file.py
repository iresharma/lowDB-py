from json import loads, dumps, JSONDecodeError
from datetime import datetime as dt
from Logger.logger import Logger
import Errors.lowDBExceptions as exceptions

logger = Logger()

PATH = ''

def makeFile(path: str) -> dict:
    '''
        Function to create the lowDB json file

        params:
        
            path: <str> path to where the file needs to createdOn

        returns:
        
            <dict>: {metaData:<dict>, data: {}}
    '''
    try:
        with open(path, 'w') as db:
            data = {
                'metaData': {
                    'version': '1.0.0',
                    'createdOn': dt.now().timestamp(),
                },
                'data': {}
            }
            db.write(dumps(data, indent=4))
        logger.success('Created')
    except FileNotFoundError:
        logger.error('File not found')
        raise exceptions.FileNotFound
    except JSONDecodeError:
        logger.error('JSON decoding was able to complete')
        raise exceptions.JSONDecode
    return data

def loadFile(path: str) -> dict:
    '''
        Function to load the lowDB json file

        params:
        
            path: <str> path to where the file needs to createdOn

        returns:
        
            <dict>: {metaData:<dict>, data: {}}
    '''
    try:
        with open(path, 'r') as db:
            data = loads(db.read())
    except FileNotFoundError:
        logger.error('File not found')
        raise exceptions.FileNotFound
    except JSONDecodeError:
        logger.error('JSON decoding was able to complete')
    logger.success('Loaded')
    logger.info("Database metaData:", data=data['metaData'])
    return data

def updateFile(path: str, data: dict):
    with open(path, 'w') as db:
        db.write(dumps(data, indent=4))