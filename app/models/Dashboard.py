from system.core.model import Model
import re

class Dashboard(Model):
    def __init__(self):
        super(Dashboard, self).__init__()

    def first_user_query(self):
        print "check to see if any users exist in db"
        users_exist = self.db.query_db("SELECT * FROM users WHERE id = 1")
        print "try about to attempt"
        try:
            users_exist[0]
            print "a user exists"
            user_level = 1
        except:
            user_level = 9
            print "no users exist"
        return user_level

    def creation_validation(self, info):
        print "creation validation method"
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\.-]+\.[a-za-z]*$')
        errors = []
        password = info['password']
        if not info['first_name']:
            errors.append('First name cannot be blank')
        elif len(info['first_name']) < 2:
            errors.append('First name must be at least 2 characters long')
        if not info['last_name']:
            errors.append('Last name cannot be blank')
        elif len(info['last_name']) < 2:
            errors.append('Last name must be at least 2 characters long')
        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif info['password'] != info['pw_confirm']:
            errors.append('Password and confirmation must match!')
        if errors:
            return {"status": False, "errors": errors}
        else:
            return{"status": True}

    def login_validation(self, loginfo, userinfo):
        print "login validation"
        password = loginfo['password']
        pw_hash = userinfo['pw_hash']
        errors=[]
        try:
            if loginfo['email'] == userinfo['email']:
                if self.bcrypt.check_password_hash(pw_hash, password):
                    print "passed login checks"
                    return {"status": True}
                else:
                    print "failed login checks"
                    errors.append('incorrect password.')
                    return {"status": False}
        except:
            print "bad email"
            errors.append('bad email.')
            return {"status": False, "errors": errors}


    def new_user(self, info):
        print "new user method"
        pw_hash = self.bcrypt.generate_password_hash(info['password'])
        create_query = "INSERT INTO users (email, first_name, last_name, pw_hash, created_at, user_level) VALUES (%s, %s, %s, %s, NOW(), %s)"
        create_data = [info['email'], info['first_name'], info['last_name'], pw_hash, info['user_level']]
        print "new user created"
        return self.db.query_db(create_query, create_data)

    def get_user_info_by_email(self, info):
        print "attempting to retrieve user info by email"
        print info['email']
        try:
            login_query = "SELECT * FROM users WHERE email = %s LIMIT 1"
            login_data = [info['email']]
            user_info = self.db.query_db(login_query, login_data)[0]
            return user_info
        except:
            return "user does not exist"

    def get_user_info_by_id(self, info):
        print "attempting to retrieve user info from id"
        login_query = "SELECT * FROM users WHERE id = %s LIMIT 1"
        login_data = [info]
        user_info = self.db.query_db(login_query, login_data)[0]
        return user_info

    def get_all_users(self):
        print "getting all users"
        all_users = self.db.query_db("SELECT * FROM users")
        return all_users

    def delete_user_by_id(self, id):
        print "deleting user"
        destroy_query = "DELETE FROM users WHERE id = %s"
        destroy_id = [id]
        return self.db.query_db(destroy_query, destroy_id)

    def update_user(self, info):
        print "updating user information"
        update_query = "UPDATE users SET email = %s, first_name = %s, last_name = %s, updated_at = NOW() WHERE id = %s"
        update_data = [info['email'], info['first_name'], info['last_name'], info['id']]
        return self.db.query_db(update_query, update_data)

    def update_password(self, info):
        print "updating user password"
        pw_hash = self.bcrypt.generate_password_hash(info['password'])
        print "broken yet?"
        errors = []
        if not info['password']:
            errors.append('Password cannot be blank')
            print "says its blank"
        elif len(info['password']) < 8:
            errors.append('Password must be at least 8 characters long')
            print "says its too short"
        elif info['password'] != info['pw_confirm']:
            errors.append('Password and confirmation must match!')
            print "pw and confirmation do not match"
        if errors:
            print "there have been passowrd match errors"
            return {"status": False, "errors": errors}
        else:
            print "no errors"
            update_query = "UPDATE users SET pw_hash = %s WHERE id = %s"
            update_data = [pw_hash, info['id']]
            self.db.query_db(update_query, update_data)
            return{"status": True}

    def update_description(self, info):
        print "updating description"
        update_query = "UPDATE users SET description = %s WHERE id = %s"
        update_data = [info['description'], info['id']]
        return self.db.query_db(update_query, update_data)

    def update_validation(self, info):
        print "creation validation method"
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\.-]+\.[a-za-z]*$')
        errors = []
        if not info['first_name']:
            errors.append('First name cannot be blank')
        elif len(info['first_name']) < 2:
            errors.append('First name must be at least 2 characters long')
        if not info['last_name']:
            errors.append('Last name cannot be blank')
        elif len(info['last_name']) < 2:
            errors.append('Last name must be at least 2 characters long')
        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if errors:
            return {"status": False, "errors": errors}
        else:
            return{"status": True}
