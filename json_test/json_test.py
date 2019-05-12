
import json
import ujson
import copy



def test():
    print(dir(json))
    str = "{'a': 'c', 'a1':'b1'}"
    print(type(str))

    usjon_obj = ujson.loads('{"a":"b","c":{"c1":"d1"}}')

    print(type(ujson))
    print(usjon_obj['c'])
    josn_object = json.loads('{"a":"b","c":{"c1":"d1"}}')

    print(type(josn_object))
    print(josn_object["a"])


def json_iter():
    content = '''
        {
        
            "contents": [{
                "a": "a"
            },
                {
                    "a": "b"
                },
                {
                    "d": "c"
                },
                {
                    "a": "d"
                }
            ]
    
        }'''

    content_obj = json.loads(content)
    print(type(content_obj['contents']))
    print(type(content_obj['contents'][0]))
    convert_contents = []
    for content in content_obj['contents']:
        if content.keys()[0] == 'd':
            generate_objs = [{'d1': 'd1'}, {'d2': 'd2'}]
            convert_contents.extend(generate_objs)
        else:
            convert_contents.append(content)

    content_obj["contents"] = convert_contents
    print(json.dumps(content_obj))



if __name__ == '__main__':
    json_iter()


