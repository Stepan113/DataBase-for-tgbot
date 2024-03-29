import os.path

from sqlalchemy.orm import Session

from DataBase.database.DataBase import Information
from sqlalchemy import create_engine, select


class Article(object):
    """Класс для обработки статей"""

    def __init__(self, title: str = None, link_on_file: str = None, link_on_photo: str = None):
        """Конструктор"""
        self.__title = title
        self.__link_on_file = link_on_file
        self.__link_on_photo = link_on_photo
        self.__engine = create_engine("sqlite:///mainInformation.db")
        self.__session = Session(self.__engine, expire_on_commit=True)

    @property
    def title(self) -> str:
        if self.__title is None:
            return ""
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def link_on_file(self) -> str:
        if self.__link_on_file is None:
            return ""
        return self.__link_on_file

    @link_on_file.setter
    def link_on_file(self, link_on_file: str):
        self.__link_on_file = link_on_file

    @property
    def link_on_photo(self) -> str:
        if self.__link_on_photo is None:
            return ""
        return self.__link_on_photo

    @link_on_photo.setter
    def link_on_photo(self, link_on_photo):
        self.__link_on_photo = link_on_photo

    def add_article(self):
        article = Information(title_article=self.title, text_link_on_file=self.link_on_file,
                              link_on_photo=self.link_on_photo)
        self.__session.add(article)
        self.__session.commit()

    def select_article(self, title: str) -> str:
        """Возвращает строку основного текста"""
        article = self.__session.scalar(select(Information).where(Information.title_article == title))
        print(article.text_link_on_file)
        if not os.path.isfile(article.text_link_on_file):
            raise FileNotFoundError("Нет файла с таким именем")
        return self.__get_text(article.text_link_on_file)

    def __get_text(self, name_file: str) -> str:
        with open(name_file, "r+", encoding="utf-8") as file:
            text = file.readlines()
            return "\n".join(text)
