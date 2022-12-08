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


        abs_path_upload = os.path.join(app.config['UPLOAD_FOLDER'] , upload_folder)
        abs_file_path = os.path.join(app.config['UPLOAD_FOLDER'] , file_path)
         # если путь не существует, создать dir
        if not os.path.isdir(abs_path_upload):
            os.makedirs(abs_path_upload)

        if(filename_save == ""):
            #рандомное название
            filename_save = str(uuid.uuid4())+ "." + convert_ext.lower()
        else:
            #или меняем расширение
            filename_save = filename_save.split(".")[0] + "." + convert_ext.lower()

        if(convert_ext in cls.ALLOWED_EXTENSIONS):
            img = Image.open(abs_file_path).convert("RGB")
            save_file_abs_path = abs_path_upload + "/" + filename_save
            img.save(  save_file_abs_path , convert_ext)
            file = File(path=os.path.join("uploads",upload_folder)  , name=filename_save.split(".")[0] 
                , extenstion=convert_ext.lower() , parse_seanse_id = parse_seanse_id)
            db.session.add(file)
            db.session.commit()
            return file

    
             