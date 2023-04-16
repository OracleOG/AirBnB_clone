#!/usr/bin/python3
""" Module of BAse_model unittest"""
import unittest
from models.base_model import BaseModel



class TestBaseModel(unittest.Testcase):
""" test for basemodel """
    my_model = BaseModel()

    def testbasemodel(self):
        self.my_model.name = "Model Alpha"
        self.my_model.my_number = 23
        self.my_model_json = my_model.to_dict()
        self.my_model.save()

        self.assertEqual(self.my_model.name, 'my_model_json[name]')
        self.assertEqual(self.my_model.my_number, 'my_model_json[my_number]')
        self.assertEqual(self.my_model.id, 'my_model_json[id]')
        self.assertEqual(BaseModel, 'my_model_json[__class__]')

        def testsave(self):
            self.assertIsInstance(my_model.id, str)
            self.assertISInstance(my_model.created_at, datetime.datetime)
            self.assertISInstance(my_model.updated_at, datetime.datetime)
            my_model.name = 'beta'

            my_model.save()
            first_dic = my_model.to_dict()

            my_model.name = 'gamma'
            my_model.save()
            sec_dic = my_model.to_dict()

            self.assertEqual(first_dic['created_at'], sec_dic[created_at])
            self.assertNotEqual(first_dic['updated_at'], sec_dic[updated_at])

if __name__ == '__main__':
    unittest.main()
