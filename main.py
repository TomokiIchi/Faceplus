import requests
import base64
import os,sys
import json
API_KEY = 'iOxruN-OC80zoII0F6sH_C3H2al2Dxd8'
API_SECRET = 'BU7yi3k-F40q9YRPnivPa2N7EezI6DIn'

def get_face_feature(img_file):
    config = {'api_key':API_KEY,
          'api_secret':API_SECRET,
          'image_base64':img_file,
          'return_landmark':1,
		  'return_attributes':'gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus'
    }
    url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
    res = requests.post(url, data=config)
    data = json.loads(res.text)
    with open('response'+'.json', 'w') as f:
        json.dump(data, f, indent=4)

    data_json = json.dumps(data, indent=4)
    print(data_json)

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        with open('./picture1.jpg', 'rb') as f:
            img_file = base64.encodebytes(f.read())
        get_face_feature(img_file)
    elif len(args) == 2:
        with open(args[1], 'rb') as f:
            img_file = base64.encodebytes(f.read())
        get_face_feature(img_file)
    else:
        print('too many argument! argument length should be <=1')
