from sqlalchemy import select, inspect

from chillax.adapters.orm import metadata


def test_database_populate_inspect_table_names(database_engine):
    # Get table information
    inspector = inspect(database_engine)
    assert inspector.get_table_names() == ['article_tags', 'articles', 'comments', 'tags', 'users']


def test_database_populate_select_all_tags(database_engine):
    # Get table information
    inspector = inspect(database_engine)
    name_of_tags_table = inspector.get_table_names()[3]

    with database_engine.connect() as connection:
        # query for records in table tags
        select_statement = select([metadata.tables[name_of_tags_table]])
        result = connection.execute(select_statement)

        all_tag_names = []
        for row in result:
            print(row)
            all_tag_names.append(row)

        assert all_tag_names == [(1, 'Action'),
                                 (2, 'Adventure'),
                                 (3, 'Sci-Fi'),
                                 (4, 'Mystery'),
                                 (5, 'Horror'),
                                 (6, 'Thriller'),
                                 (7, 'Animation'),
                                 (8, 'Comedy'),
                                 (9, 'Family'),
                                 (10, 'Fantasy'),
                                 (11, 'Drama'),
                                 (12, 'Music'),
                                 (13, 'Biography'),
                                 (14, 'Romance'),
                                 (15, 'History'),
                                 (16, 'Crime'),
                                 (17, 'Western'),
                                 (18, 'War'),
                                 (19, 'Musical'),
                                 (20, 'Sport')]


def test_database_populate_select_all_users(database_engine):
    # Get table information
    inspector = inspect(database_engine)
    name_of_users_table = inspector.get_table_names()[4]

    with database_engine.connect() as connection:
        # query for records in table users
        select_statement = select([metadata.tables[name_of_users_table]])
        result = connection.execute(select_statement)

        all_users = []
        for row in result:
            all_users.append(row['username'])

        assert all_users == ['thorke', 'fmercury', 'mjackson']


def test_database_populate_select_all_comments(database_engine):
    # Get table information
    inspector = inspect(database_engine)
    name_of_comments_table = inspector.get_table_names()[2]

    with database_engine.connect() as connection:
        # query for records in table comments
        select_statement = select([metadata.tables[name_of_comments_table]])
        result = connection.execute(select_statement)

        all_comments = []
        for row in result:
            all_comments.append((row['id'], row['user_id'], row['article_id'], row['comment']))

        assert all_comments == [(1, 2, 1, 'Oh no, COVID-19 has hit New Zealand'),
                                (2, 1, 1, 'Yeah Freddie, bad news'),
                                (3, 3, 1, "I hope it's not as bad here as Italy!")]


def test_database_populate_select_all_articles(database_engine):
    # Get table information
    inspector = inspect(database_engine)
    name_of_articles_table = inspector.get_table_names()[1]

    with database_engine.connect() as connection:
        # query for records in table articles
        select_statement = select([metadata.tables[name_of_articles_table]])
        result = connection.execute(select_statement)

        all_articles = []
        for row in result:
            all_articles.append((row['id'], row['title']))

        nr_articles = len(all_articles)

        assert all_articles[0] == (1, 'Guardians of the Galaxy')
        assert all_articles[nr_articles // 2] == (501, 'Maze Runner: The Scorch Trials')
        assert all_articles[nr_articles - 1] == (1000, 'Nine Lives')
