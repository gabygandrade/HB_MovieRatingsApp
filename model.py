from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref

engine = create_engine("sqlite:///ratings.db", echo=True)
session = scoped_session(sessionmaker(bind=engine,
                                      autocommit = False,
                                      autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

### Class declarations go here
class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable = True)
    password = Column(String(64), nullable = True)
    age = Column(Integer, nullable = True)
    zipcode = Column(String(15), nullable = True)

    def __repr__(self):
        """Cleanly show info about self """
        return "<User id=%d email=%s password=%s age=%d zipcode=%s>" % (self.id, self.email, self.password, self.age, self.zipcode)
### End class declarations

class Movie(Base): 
    __tablename__ = "Movies"
    id = Column(Integer, primary_key = True)
    title = Column(String(64), nullable = False)
    rel_date = Column(DateTime, nullable = True)
    url = Column(String(150), nullable = False)
    
    def __repr__(self):
        """Cleanly show info about self """
        return "<id=%d title=%s rel_date=%s url=%s>" % (self.id, self.title, self.rel_date, self.url)

class Rating(Base):
    __tablename__ = "Ratings"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    movie_id = Column(Integer, ForeignKey('Movies.id'))
    rating = Column(Integer)

    user = relationship("User",
            backref=backref("ratings", order_by = id))  # "ratings" is a name we gave to reference the relationship between the user and the ratings

    movie = relationship("Movie",
            backref=backref("ratings", order_by = id))

    def __repr__(self):
        """Cleanly show info about self """
        return "<id=%d user_id=%d movie_id=%d rating=%d>" % (self.id, self.user_id, self.movie_id, self.rating)

def connect():
    # global ENGINE
    # global Session
    # return Session()
    pass

def main():
    # session = connect()
    pass

if __name__ == "__main__":
    main()
