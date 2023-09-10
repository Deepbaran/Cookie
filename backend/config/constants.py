class Constants:
    DEV_ENV = "development"

class Response:
    NO_DATA_FOUND = "No Data Found"

class UserQueries:
    FETCH_ALL = 'SELECT * FROM cookie.users;'
    FETCH_BY_ID = "SELECT * FROM users WHERE id=%s;"
    INSERT_USER_RECORD = """
                        INSERT INTO users
                        (first_name, last_name, email, password, phone_no) 
                        VALUES('%s', '%s', '%s', '%s', '%s');
                        """

class RecipeQueries:
    FETCH_ALL = 'SELECT * FROM recipes;'