#!/usr/bin/python3
"""
Base class
"""
import json
import os
import csv


class Base:
    """Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Initializes the class"""
        if not(id == None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of the list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            json_repr = "[]"
        else:
            json_repr = json.dumps(list_dictionaries)
        return json_repr

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        dict_list = []
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None or len(list_objs) == 0:
                j_str = ""
            else:
                for obj in list_objs:
                    dic = cls.to_dictionary(obj)
                    dict_list.append(dic)
            j_str = cls.to_json_string(dict_list)
            f.write(j_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            json_list = []
        else:
            json_list = json.loads(json_string)
        return json_list

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)
        if cls.__name__ == "Square":
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        data = ""
        json_list = []
        my_list = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                data = f.read()
                my_list = cls.from_json_string(data)
                for elem in my_list:
                    json_list.append(cls.create(**elem))
            return json_list
        else:
            return json_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV"""
        filename = cls.__name__ + '.csv'

        with open(filename, 'w') as f:
            if list_objs is None:
                data = csv.writer(f, delimiter=',')
                data.writerow([])
            else:
                data = csv.writer(f, delimiter=',')
                if cls.__name__ == "Rectangle":
                    for element in list_objs:
                        attr = ['id', 'width', 'height', 'x', 'y']
                        value = []
                        for x in attr:
                            value.append(getattr(element, x))
                        data.writerow(value)
                elif cls.__name__ == "Square":
                    for element in list_objs:
                        attr = ['id', 'size', 'x', 'y']
                        value = []
                        for x in attr:
                            value.append(getattr(element, x))
                        data.writerow(value)

    @classmethod
    def load_from_file_csv(cls):
        """loads from csv file and creates objects"""
        filename = cls.__name__ + ".csv"
        inst = []
        dic = {}
        if os.path.exists(filename):
            with open(filename) as f:
                content = csv.reader(f, delimiter=',')
                for row in content:
                    a = []
                    for elem in row:
                        a.append(int(elem))

                    if cls.__name__ == "Rectangle":
                        new = ['id', 'width', 'height', 'x', 'y']
                        for i in range(len(a)):
                            dic[new[i]] = a[i]
                        inst.append(cls.create(**dic))
                    if cls.__name__ == "Square":
                        new = ['id', 'size', 'x', 'y']
                        for i in range(len(a)):
                            dic[new[i]] = a[i]
                        inst.append(cls.create(**dic))
            return inst
        else:
            return inst
