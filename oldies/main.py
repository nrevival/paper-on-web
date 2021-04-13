#!/usr/bin/env python3

import connexion
from theconf import Config as C
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

_ = C('config.yaml')

api_app = connexion.FlaskApp(__name__, port=C.get()["portnum"], specification_dir='swagger/')

gauth = GoogleAuth()


@api_app.route('/')
def hello():



    drive = GoogleDrive(gauth)
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file1 in file_list:
        print('title: %s, id: %s' % (file1['title'], file1['id']))
    #test_gdrive_connect()
    return "hello World"
    #upload()
    #return test()

def test_gdrive_connect():
    gauth = GoogleAuth()
    #auth_url = gauth.GetAuthUrl()
    #code = ""
    #gauth.Auth(code)
    drive = GoogleDrive(gauth)

    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file1 in file_list:
        print('title: %s, id: %s' % (file1['title'], file1['id']))





if __name__ == '__main__':
    api_app.add_api('api.yaml', arguments={'title': 'Hello World Example'})
    api_app.run()
