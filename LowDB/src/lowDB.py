import os.path as p
import fileOp.file as fileOps


class LowDB:
    data = {}

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
        if p.isfile(path):
            self.data = fileOps.loadFile(path)
        else:
            self.data = fileOps.makeFile(path)