import os
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
from myapp.models.file_loader import FileLoader

class Parser():

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
        return urls


    @classmethod
    def load_all_images(cls ,url, path):

        # получить все изображения
        imgs = cls.get_all_images(url)
        for img in imgs:
            # скачать для каждого img
            FileLoader.save_from_url(path ,img)