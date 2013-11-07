import sys
from factory import Factory

def get_content_file_base64(filename):
    return open(filename, "rb").read().encode("base64")

filename = sys.argv[1]

factory = Factory()

res = get_content_file_base64(filename)
es_doc = factory.create_es_doc()
es_doc.set_content(res)
id_doc = es_doc.save()

print "Id du document.....%d" % id_doc



