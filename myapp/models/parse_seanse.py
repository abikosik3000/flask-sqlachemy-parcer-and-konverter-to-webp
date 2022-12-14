from myapp import db
from sqlalchemy.sql import func
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
from myapp.models.file_loader import FileLoader
from myapp.models.file_converter import FileConverter
from myapp.models.file import File
import uuid
import os


class Parse_seanse(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id') ,nullable=True)
    status = db.Column(db.String(64))
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    page_to_parse = db.Column(db.String(360))

    PARSE_FOLDER_NAME = "parser_load"

    @property
    def images(self):
        return db.session.query(File).filter(File.parse_seanse_id == self.id).all()

    @staticmethod
    def get_all_for_user_id(user_id):
        return db.session.query(Parse_seanse).filter(Parse_seanse.user_id == user_id).all()

    def set_status(self , new_status):
        self.status = new_status
        db.session.add(self)
        db.session.commit()

    def convert_all_img_from_url(self , page_to_parse):
        '''
        конвертирует все изображения со страницы
        возвращает path папки
        '''

        self.set_status("parsing")

        urls = self.get_all_images(page_to_parse)
        save_urls = []

        
        for url in urls:

            buff = FileLoader.save_from_url( 
                os.path.join( "parser_load" , str(self.id))
                , url)

            if(buff is None):
                continue

            save_urls.append( buff)

        upload_folder = os.path.join(self.PARSE_FOLDER_NAME, str(self.id),"optimized")
        for path in save_urls:

            _filename_save = path.split("/")[-1]
            FileConverter.convert_to(upload_folder,path,"WEBP"
            , filename_save=_filename_save , parse_seanse_id=self.id)
    

        self.set_status("ready")

        return upload_folder

    def get_all_converted_img_urls(self):
        '''
        возвращает лист url конвертированных изображенией
        #user = db.session.query(User).filter(User.email == form.email.data).first()
        '''
        files = db.session.query(File).filter(File.parse_seanse_id == self.id).all()

        urls = []
        for file in files:
            urls.append(file.url)
        
        return urls

    @classmethod
    def is_valid(cls ,url):
        # Проверяем, является ли url действительным URL
        
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    @classmethod
    def get_all_images(cls ,url):
        # Возвращает все URL‑адреса изображений по одному `url`

        soup = bs(requests.get(url).content, "html.parser")
        urls = []
        for img in tqdm(soup.find_all("img"), "Получено изображение"):
            img_url = img.attrs.get("src")
            if not img_url:
                # если img не содержит атрибута src, просто пропускаем
                continue
            # сделаем URL абсолютным, присоединив имя домена к только что извлеченному URL
            img_url = urljoin(url, img_url)
            # удалим URL‑адреса типа '/hsts-pixel.gif?c=3.2.5'
            try:
                pos = img_url.index("?")
                img_url = img_url[:pos]
            except ValueError:
                pass
            # наконец, если URL действителен
            if cls.is_valid(img_url):
                urls.append(img_url)

        return list(set(urls))


    @classmethod
    def load_all_images(cls ,url, path):

        # получить все изображения
        imgs = cls.get_all_images(url)
        for img in imgs:
            # скачать для каждого img
            FileLoader.save_from_url(path ,img)


    

    



