from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from httplib2 import Http
from oauth2client import file as oa_file, client, tools



# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'

def upload():
    store = oa_file.Storage('token.json') # user마다 다르게?
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

    file_metadata = {'name': 'Paper/gg_photo.jpg'}
    media = MediaFileUpload('photo.jpg',
                            mimetype='image/jpeg')
    c_file = DRIVE.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()
    print ('File ID: %s' % c_file.get('id'))

def check_drive_folder():
    store = oa_file.Storage('token.json')  # user마다 다르게?
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)

    DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

    print("h")


    # file_metadata = {
    #     'name': 'Invoices',
    #     'mimeType': 'application/vnd.google-apps.folder'
    # }
    # folder = DRIVE.files().create(body=file_metadata,fields='id').execute()
    # return folder.get('id')



def test():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = oa_file.Storage('token.json') # user마다 다르게?
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        return 'No files found.'
    else:
        res_str = 'Files:\n'
        for item in items:
            res_str += u'{0} ({1})\n'.format(item['name'], item['id'])
        return res_str