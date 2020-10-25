import abc
from typing import List
from datetime import date

from chillax.domain.model import User, Movies, Tag, Comment


repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user: User):
        """" Adds a User to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:
        """ Returns the User named username from the repository.

        If there is no User with the given username, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_article(self, article: Movies):
        """ Adds an Movies to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_article(self, id: int) -> Movies:
        """ Returns Movies with id from the repository.

        If there is no Movies with the given id, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_articles_by_date(self, target_date: date) -> List[Movies]:
        """ Returns a list of Movies that were published on target_date.

        If there are no Movies on the given date, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_articles(self):
        """ Returns the number of Movies in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_article(self) -> Movies:
        """ Returns the first Movies, ordered by date, from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_article(self) -> Movies:
        """ Returns the last Movies, ordered by date, from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_articles_by_id(self, id_list):
        """ Returns a list of Movies, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_article_ids_for_tag(self, tag_name: str):
        """ Returns a list of ids representing Movies that are tagged by tag_name.

        If there are Movies that are tagged by tag_name, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_date_of_previous_article(self, article: Movies):
        """ Returns the date of an Movies that immediately precedes article.

        If article is the first Movies in the repository, this method returns None because there are no Movies
        on a previous date.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_date_of_next_article(self, article: Movies):
        """ Returns the date of an Movies that immediately follows article.

        If article is the last Movies in the repository, this method returns None because there are no Movies
        on a later date.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_tag(self, tag: Tag):
        """ Adds a Tag to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_tags(self) -> List[Tag]:
        """ Returns the Tags stored in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_comment(self, comment: Comment):
        """ Adds a Comment to the repository.

        If the Comment doesn't have bidirectional links with an Movies and a User, this method raises a
        RepositoryException and doesn't update the repository.
        """
        if comment.user is None or comment not in comment.user.comments:
            raise RepositoryException('Comment not correctly attached to a User')
        if comment.article is None or comment not in comment.article.comments:
            raise RepositoryException('Comment not correctly attached to an Movie')

    @abc.abstractmethod
    def get_comments(self):
        """ Returns the Comments stored in the repository. """
        raise NotImplementedError







