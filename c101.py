import dropbox

class Upload:
    def __init__(self,access_token):
        self.access_token = access_token

    def fileUpload(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'Ozwm6d4EEcIAAAAAAAAAAZVmLFenhdpMnmXUJ96dNacoZ6A_2H1dRkqLEksZfrQ3'
    upload = Upload(access_token)
    file_from= input('Enter the file path to transfer') 
    file_to=input('enter the full path to upload to Dropbox')    

    upload.fileUpload(file_from,file_to)
    print('file has been moved')

main()           