class LowDBError(Exception):
    """Base class for other errors to extend"""
    pass

class FileNotFound(LowDBError):
    """Error when db.json file is not found"""

    def __str__(self):
        print("db.json file was not found")

class DecodeError(LowDBError):
    """Error when the data from file was not decoded"""

    def __str__(self):
        print("Error occurred while decoding json from db.json")

class InvalidSearchArgsError(LowDBError):
    """Error when invalid parameters were send to the search function"""

    def __str__(self):
        print("Error occured in searching; invalid props were sent")