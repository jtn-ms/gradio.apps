import zipfile

archive = zipfile.ZipFile('file.docx')
for file in archive.filelist:
    if file.filename.startswith('word/media/') and file.file_size > 300000:
        archive.extract(file)