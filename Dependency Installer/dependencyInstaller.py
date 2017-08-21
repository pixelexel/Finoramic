import json
import subprocess
import collections

#loading JSON as python dictionary
with open("dependencies.json") as json_file:
    data = json.load(json_file)

#removing unicode from dictionary
def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data
data = convert(data)

#installing dependencies
def install(name):
    subprocess.call(['pip', 'install', name])

error_list = []
for key, value in data.items():
    name = key + "==" + value
    try:
        install(name)
    except Exception as e:
        error_list.append(name)

if not error_list:
    print "Success!"
else:
    print error_list
