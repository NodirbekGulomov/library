from decimal import Decimal
import json

from sqlalchemy import ForeignKey, Numeric, create_engine, delete, select, func
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship, selectinload

engine = create_engine("sqlite:///library.db")


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str]
    birth_year: Mapped[int]
    books: Mapped[list['Book']] = relationship(back_populates='author', cascade="all, delete-orphan")


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    price: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2))
    published_year: Mapped[int]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped['Author'] = relationship(back_populates='books')


Base.metadata.create_all(bind=engine)


def load_initial_data():
    with open('authors.json', 'r') as file:
        authors = json.load(file)

    with open('books.json', 'r') as file:
        books = json.load(file)

    with Session(engine) as session:
        authors_objects = [
            Author(
                full_name=a['full_name'],
                birth_year=a['birth_year'],
            ) for a in authors
        ]

        books_objects = [
            Book(
                title=b['title'],
                price=b['price'],
                published_year=b['published_year'],
                author_id=b['author_id'],
            ) for b in books
        ]

        session.execute(delete(Author))
        session.execute(delete(Book))

        session.add_all(authors_objects)
        session.add_all(books_objects)
        session.commit()


load_initial_data()


def q1():
    with Session(engine) as session:
        stmt = select(Author)

    res = session.execute(stmt).scalars().all()

    for item in res:
        print(item.id, item.full_name, item.birth_year, sep=' | ')


# q1()

def q2():
    with Session(engine) as session:
        stmt = select(Book)

    res = session.execute(stmt).scalars().all()

    for item in res:
        print(item.id, item.title, item.price, item.price, item.published_year, item.author_id, sep=' | ')


# q2()

def q3():
    with Session(engine) as session:
        stmt = select(Author).options(selectinload(Author.books))
    for author in session.scalars(stmt):
        print(f"\nMuallif: {author.full_name}")
        for book in author.books:
            print(f"  * {book.title} ({book.published_year})")


# q3()

def q4(author_full_name):
    with Session(engine) as session:
        stmt = select(Author).options(selectinload(Author.books)).where(Author.full_name == author_full_name)
    for author in session.scalars(stmt):
        print(f"\nMuallif: {author.full_name}")
        for book in author.books:
            print(f"  * {book.title} ({book.published_year})")


# q4('Ernest Hemingway')

def q5():
    with Session(engine) as session:
        stmt = select(Book.title, Book.price).where(Book.price > Decimal('100000'))
        res = session.execute(stmt).all()
    for book in res:
        print(f"\nBook: {book.title} Price: {book.price}")


# q5()

def q6():
    with Session(engine) as session:
        stmt = select(Book.title, Book.published_year).where(Book.published_year > 2015)
        res = session.execute(stmt).all()
    for book in res:
        print(f"\nBook: {book.title} Price: {book.published_year}")


# q6()

def q7():
    with Session(engine) as session:
        stmt = select(Book.title, Book.price).order_by(Book.price.desc()).limit(1)
        res = session.execute(stmt).first()

        print(f"\nBook: {res.title} Price: {res.price}")


# q7()

def q8():
    pass


def q9():
    with Session(engine) as session:
        stmt = select(Author)
        res = session.execute(stmt).scalars().all()
        for r in res:
            print(r.full_name, len(r.books))


# q9()


def q10():
    with Session(engine) as session:
        stmt = select(Book.title).where(Book.title.ilike('%Python%'))
        res = session.execute(stmt).scalars().all()

        for b in res:
            print(b)


# q10()

def q11():
    with Session(engine) as session:
        stmt = select(Book.title, Author.full_name).join(Author, Author.id == Book.author_id)
        res = session.execute(stmt).all()
        for r in res:
            print(r.title, ' | ', r.full_name)

# q11()
