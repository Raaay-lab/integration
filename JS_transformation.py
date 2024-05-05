import json
import xml.etree.ElementTree as E


def get_tag(temp_tag):
    res = temp_tag.split('}')
    return res[-1]


def transform(r):
    json_data = {"elements": []}
    for child in r:
        dic = {}
        for child2 in child:
            if child2.tag not in dic:
                dic[get_tag(child2.tag)] = child2.text
        dic = {**dic, **child.attrib}
        json_data["elements"].append({get_tag(child.tag): dic})

    return json_data


def save_to_json(json_data):
    with open('JS_transform/js_OUT.json', 'w') as json_file:
        json_data = json.dumps(json_data)
        json_file.write(json_data)


if __name__ == "__main__":
    tree = E.parse('JS_transform/js_in.xml')
    root = tree.getroot()
    rdy_data = transform(root)
    save_to_json(rdy_data)
