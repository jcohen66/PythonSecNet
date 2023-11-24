import zipfile

def list_files_in_zip(filename):
    with zipfile.ZipFile(filename, 'r') as zip_file:
        for zipinfo in zip_file.infolist():
            yield zipinfo.filename

if __name__ == '__main__':
    for filename in list_files_in_zip('files.zip'):
        print(filename)

