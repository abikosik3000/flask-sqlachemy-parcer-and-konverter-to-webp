import uuid
import os
import requests
from myapp import app

class FileLoader:

    @classmethod
    def create_or_exist_folder(cls,upload_folder):
        # если путь не существует, создать dir
        if not os.path.isdir(upload_folder):
            os.makedirs(upload_folder)

    @classmethod
    def save_from_temp(cls,upload_folder,file ,filename_save = ""):
        

        abs_path_upload = os.path.join(app.config['UPLOAD_FOLDER'] , upload_folder)

        cls.create_or_exist_folder(abs_path_upload)

        if file and cls.allowed_file(file.filename):

            if(filename_save == ""):
                filename_save = str(uuid.uuid4()) + '.'+ cls.file_extension(file.filename)

            file_abs_path = os.path.join(abs_path_upload , filename_save ) 
            # сохраняем файл 
            file.save(file_abs_path)

            return os.path.join(upload_folder, filename_save)
        else:
            return None
            
    @classmethod
    def save_from_url(cls,upload_folder,url,filename_save = ""):
        #Загружает файл по URL‑адресу
        abs_path_upload = os.path.join(app.config['UPLOAD_FOLDER'] , upload_folder)
        # если путь не существует, создать dir
        cls.create_or_exist_folder(abs_path_upload)

        response = requests.get(url, stream=True)
        # получить общий размер файла
        file_size = int(response.headers.get("Content-Length", 0))
        # получаем имя файла

        if(filename_save == ""):
            filename_save =  url.split("/")[-1]

        file_abs_path = os.path.join(abs_path_upload, filename_save)

        if(cls.allowed_file(filename_save)):
            with requests.get(url, stream=True) as r:
                with open(file_abs_path, "wb") as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)

            return os.path.join(upload_folder, filename_save)

        else:
            return None

    # расширения файлов, которые разрешено загружать
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

    @classmethod
    def file_extension(cls,filename):
        return filename.rsplit('.', 1)[1].lower()

    @classmethod
    def allowed_file(cls,filename):
        return '.' in filename and cls.file_extension(filename) in cls.ALLOWED_EXTENSIONS
