class Constants:
    DEV_ENV = "development"

class Response:
    NO_DATA_FOUND = "No Data Found"
    NOTHING_TO_UPDATE = "Nothing to Update"
    NOTHING_TO_DELETE = "Nothing to Delete"

    RECORD_CREATED_SUCCESSFULLY = "Record Created Successfully"
    RECORD_UPDATED_SUCCESSFULLY = "Record Updated Successfully"
    RECORD_DELETED_SUCCESSFULLY = "Record Deleted Successfully"

class Queries:
    FETCH_ALL = 'SELECT * FROM %s LIMIT %s, %s'
    FETCH_BY_ID = "SELECT * FROM %s WHERE id=%s"

class UserQueries:
    INSERT_USER_RECORD = """
                        INSERT INTO users
                        (first_name, last_name, email, password, phone_no) 
                        VALUES('%s', '%s', '%s', '%s', '%s')
                        """
    UPDATE_USER = "UPDATE users SET "
    DELETE_USER = "DELETE FROM users WHERE id='%s'"

class RecipeQueries:
    UPDATE_RECIPE = "UPDATE recipes SET "
    DELETE_RECIPE = "DELETE FROM recipes WHERE id='%s'"