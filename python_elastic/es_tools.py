import datetime
import time


class ES_doc(object):

    def __init__(self, es_connection):
        self.es_connection = es_connection
        self.index_name = "doc2"
        self.idx_type = "test2"
        self.base64_content = None

    def set_content(self, base64_content):
        self.base64_content = base64_content

    def save(self):
        id = self.get_id()
        self.es_connection.index(self.index_name, self.idx_type,{"file" : self.base64_content}, id)
        return id

    def get_id(self):
        return int(time.mktime(datetime.datetime.now().timetuple()))

