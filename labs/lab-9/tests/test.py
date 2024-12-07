import pytest

from sqlalchemy import insert, select, text
from models import User

# test db connection
def test_db_connection(db_session):
    # Use db_session to interact with the database
    result = db_session.execute(text("SELECT 1"))
    assert result.scalar() == 1

# test to insert a user
# you can count this as one of your 5 test cases :)
def test_insert_user(db_session, sample_signup_input):
    insert_stmt = insert(User).values(sample_signup_input)

    # execute insert query
    db_session.execute(insert_stmt)
    # commit the changes to the db
    db_session.commit()

    # not part of the app.py code, just being used to get the inserted data
    selected_user = db_session.query(User).filter_by(FirstName="Calista").first()

    assert selected_user is not None
    assert selected_user.LastName == "Phippen"

def test_values_stripped():
    user_data: dict = {}
            # loop through the dict to access each value
    for key, value in sample_signup_inputSpaced.items():
                # remove the leading and trailing spaces using the strip() function
        user_data[key] = value.strip()

    assert user_data == sample_signup_input()

def test_value_altered():
    user_data: dict = {}
            # loop through the dict to access each value
    for key, value in sample_signup_inputSpaced.items():
                # remove the leading and trailing spaces using the strip() function
        user_data[key] = value.strip()

    assert user_data =! sample_signup_input()

def test_empty():
    user_data: dict = {}

    for key, value in sample_empty.items():

        user_data[key] = value.strip()
    
    assert user_data =! sample_empty()

def test_insert_user_login(db_session, sample_signup_input):
    insert_stmt = insert(User).values(sample_login_input)

    # execute insert query
    db_session.execute(insert_stmt)
    # commit the changes to the db
    db_session.commit()

    # not part of the app.py code, just being used to get the inserted data
    selected_user = db_session.query(User).filter_by(Email="calista.phippen1@marist.edu").first()

    assert selected_user is not None
    assert selected_user.Password == "mypassword"