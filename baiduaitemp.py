import base64

from aip import AipFace

APP_ID='119428005'
API_KEY='Ufc63J3mACpNHO4GxlvfHwYp'
S_KEY='8TTnuOqOFqQnwnUzQTN7Q6rQOF2Qvk3E'



def get_file_content(file_path):
    file= open(file_path, 'rb')
    data=file.read()
    content=base64.b64encode(data)
    file.close()
    return content.decode('utf-8')

def detect_face(client,base):
    options={'face_field':'beauty',}
    return client.detect(base,'BASE64',options)

if __name__ == '__main__':
    client = AipFace(APP_ID, API_KEY, S_KEY)
    base=get_file_content('qwe5.png')
    json=detect_face(client,base)
    print(json)