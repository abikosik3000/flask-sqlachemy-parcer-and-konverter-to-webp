from PIL import Image
import uuid
import os
from myapp.models.file import File
from myapp import app , db


class FileConverter:

    # расширения файлов, в которые разрешено конвертировать
    ALLOWED_EXTENSIONS = { 'PNG', 'JPG', 'WEBP'}

    @classmethod
    def convert_to(cls, upload_folder ,file_path ,convert_ext ,filename_save = "" , parse_seanse_id = None):

         # если путь не существует, создать di
        if not os.path.isdir(app.config['UPLOAD_FOLDER'] +"/"+upload_folder):
            os.makedirs(app.config['UPLOAD_FOLDER'] +"/"+upload_folder)

        if(filename_save == ""):
            #рандомное название
            filename_save = str(uuid.uuid4())+ "." + convert_ext.lower()
        else:
            #или меняем расширение
            filename_save = filename_save.split(".")[0] + "." + convert_ext.lower()

        if(convert_ext in cls.ALLOWED_EXTENSIONS):
            img = Image.open(file_path).convert("RGB")
            file_path = upload_folder + "/" + filename_save
            img.save(app.config['UPLOAD_FOLDER'] +"/"+file_path, convert_ext)
            file = File(path=file_path , name=filename_save.split(".")[0] 
                , extenstion=convert_ext.lower() , parse_seanse_id = parse_seanse_id)
            db.session.add(file)
            db.session.commit()
            return file

    
             