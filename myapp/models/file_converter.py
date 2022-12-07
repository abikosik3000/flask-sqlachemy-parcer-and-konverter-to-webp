from PIL import Image
import uuid
import os

class FileConverter:

    # расширения файлов, которые разрешено загружать
    ALLOWED_EXTENSIONS = { 'PNG', 'JPG', 'WEBP'}

    @classmethod
    def convert_to(cls, upload_folder ,file_path ,convert_ext ,filename_save = ""):

         # если путь не существует, создать di
        if not os.path.isdir(upload_folder):
            os.makedirs(upload_folder)

        if(filename_save == ""):
            #рандомное название
            filename_save = str(uuid.uuid4())+ "." + convert_ext.lower()
        else:
            #или обрезаем расширение
            filename_save = filename_save.split(".")[0] + "." + convert_ext.lower()

        if(convert_ext in cls.ALLOWED_EXTENSIONS):
            img = Image.open(file_path).convert("RGB")
            file_path = upload_folder + "/" + filename_save
            img.save(file_path, convert_ext)   
            return file_path

    
             