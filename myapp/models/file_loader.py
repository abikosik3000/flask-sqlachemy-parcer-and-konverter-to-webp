import uuid
import os
import requests

class FileLoader:

    @classmethod
    def create_or_exist_folder(cls,upload_folder):
        # если путь не существует, создать di
        if not os.path.isdir(upload_folder):
            os.makedirs(upload_folder)

    @classmethod
    def save_from_temp(cls,upload_folder,file ,filename_save = ""):
        
        cls.create_or_exist_folder(upload_folder)

        if file and cls.allowed_file(file.filename):

            if(filename_save == ""):
                filename_save = str(uuid.uuid4()) + '.'+ cls.file_extension(file.filename)

            file_path = upload_folder + "/" + filename_save 
            # сохраняем файл #app.config['UPLOAD_FOLDER']
            file.save(file_path)

            return file_path
        else:
            return None
            
    @classmethod
    def save_from_url(cls,upload_folder,url,filename_save = ""):
        #Загружает файл по URL‑адресу
        
        # если путь не существует, создать dir
        cls.create_or_exist_folder(upload_folder)

        response = requests.get(url, stream=True)
        # получить общий размер файла
        file_size = int(response.headers.get("Content-Length", 0))
        # получаем имя файла

        if(filename_save == ""):
            filename_save =  url.split("/")[-1]
        file_path = os.path.join(upload_folder, filename_save)

        if(cls.allowed_file(filename_save)):
            with requests.get(url, stream=True) as r:
                with open(file_path, "wb") as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)

            return file_path

        else:
            return None

    # расширения файлов, которые разрешено загружать
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

    @classmethod
    def file_extension(cls,filename):
        return filename.rsplit('.', 1)[1].lower()

    @classmethod
    def allowed_file(cls,filename):
        return '.' in filename and cls.file_extension(filename) in cls.ALLOWED_EXTENSIONS
