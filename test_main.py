import unittest
from app import app
import json

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        

    def test_prediction(self):
        datas = "0,0,0,0,0,44,105,44,10,0,0,0,0,0,0,0,0,0,0,0,34,68,34,0,0,0,0,0,0,0,0,0,34,136,102,105,98,74,64,34,27,20,13,20,27,47,71,85,85,91,136,27,0,0,0,0,0,0,0,0,102,119,74,91,81,95,95,88,95,88,78,78,81,78,71,68,68,61,68,115,0,0,0,0,0,0,0,0,153,102,88,91,71,78,71,64,68,68,68,71,61,61,68,64,71,78,64,122,13,0,0,0,0,0,0,6,163,95,98,91,85,78,68,71,71,71,71,71,61,61,64,68,68,68,64,112,44,0,0,0,0,0,0,30,153,88,102,95,88,74,64,68,64,68,68,68,57,57,61,61,64,68,68,115,47,0,0,0,0,0,0,47,146,105,108,102,95,81,68,71,71,74,78,74,64,64,68,68,71,71,74,102,68,0,0,0,0,0,0,71,139,98,112,102,95,88,78,81,78,81,91,88,78,74,74,74,81,81,81,85,102,0,0,0,0,0,0,102,129,95,105,115,122,102,88,91,88,85,91,98,88,95,85,88,78,74,81,71,102,0,0,0,0,0,0,108,119,119,108,132,125,95,88,88,88,81,81,88,81,81,78,98,98,68,74,71,102,0,0,0,0,0,0,112,102,115,105,139,112,85,91,88,88,81,81,88,81,81,78,91,136,81,68,74,105,30,0,0,0,0,10,122,108,115,108,149,115,85,91,88,85,85,88,95,88,91,78,74,156,95,78,78,91,47,0,0,0,0,23,129,102,88,129,170,95,91,95,91,91,85,85,85,85,88,81,57,163,129,74,74,78,71,0,0,0,0,68,112,115,85,173,187,85,102,95,95,91,91,88,88,88,95,85,51,159,187,78,102,68,85,0,0,0,0,112,176,98,98,221,180,74,102,98,95,95,88,88,88,88,91,81,54,139,200,119,95,88,115,0,0,0,0,3,190,105,115,207,163,74,102,102,98,95,91,91,91,95,85,81,61,108,217,142,105,122,3,0,0,0,0,0,34,163,132,204,153,74,95,98,98,105,102,95,95,98,95,88,64,81,214,183,200,23,0,0,0,0,0,0,0,88,173,210,105,78,108,98,102,108,102,91,95,95,98,98,81,51,183,241,54,0,0,0,0,0,0,0,0,0,200,231,68,91,105,102,105,108,102,95,98,98,98,95,98,34,204,207,0,0,0,0,0,0,0,0,0,0,98,187,81,88,108,102,105,108,105,98,102,102,105,85,98,54,255,51,0,6,3,0,0,0,0,0,0,0,0,98,122,91,105,112,115,115,112,112,108,112,105,91,98,88,119,0,0,0,0,0,0,0,0,0,0,0,0,139,119,95,112,115,122,119,119,122,119,119,112,95,102,91,129,0,0,0,0,0,0,0,0,0,3,0,0,149,115,105,112,119,125,122,125,129,122,125,119,105,105,95,136,0,0,0,0,0,0,0,0,0,3,0,0,156,119,112,115,122,129,125,125,125,122,119,119,115,108,95,139,0,0,0,0,0,0,0,0,0,3,0,0,136,119,108,125,129,129,132,129,129,129,129,129,122,115,105,139,6,0,3,0,0,0,0,0,0,3,0,0,173,125,108,136,125,132,136,132,132,132,132,125,122,122,105,166,23,0,3,0,0,0,0,0,0,0,0,0,122,149,119,115,119,125,132,129,125,125,129,122,125,139,132,132,10,0,0,0,0,0,0,0,0,0,0,0,0,23,57,105,108,115,125,125,122,122,125,119,105,64,30,0,0,0,0,0,0,0"
        response = self.app.post("/api/classify", data={'query': datas})
        res = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res, {"prediction": "Shirt"})

if __name__ == '__main__':
    unittest.main()
