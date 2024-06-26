#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound



from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memorized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add user to DB
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """ 2. Find user by
        """
        results = self._session.query(User).filter_by(**kwargs)
        return results.one()

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user attributes."""
        try:
            # Première requête qui retourne un résultat
            result = (self.session.query(self.YourModel)
                      .filter(self.YourModel.id == 1)
                      .one())
            print(result.id)  # ou un autre attribut pertinent

            # Deuxième requête similaire
            result = (
                self.session.query(self.YourModel)
                .filter(self.YourModel.id == 2)
                .one())
            print(result.id)  # ou un autre attribut pertinent

        except NoResultFound:
            print("Not found")

        except Exception:
            print("Invalid")
