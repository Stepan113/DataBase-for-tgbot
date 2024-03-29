from sqlalchemy import create_engine, DateTime
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func

engine = create_engine("sqlite:///mainInformation.db", echo=True)
session = Session(engine, expire_on_commit=True)


class Base(DeclarativeBase):
    pass


class Information(Base):
    __tablename__ = "information"
    id: Mapped[int] = mapped_column(primary_key=True)
    title_article: Mapped[str]
    text_link_on_file: Mapped[str]
    link_on_photo: Mapped[str]
    create_at = mapped_column(DateTime, default=func.now())
    update_at = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    def __str__(self):
        return f"title_article: {self.title_article}, text_link_on_file: {self.text_link_on_file}, link_on_photo: {self.link_on_photo}"
