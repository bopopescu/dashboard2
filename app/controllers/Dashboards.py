from system.core.controller import *

class Dashboards(Controller):
    def __init__(self, action):
        super(Dashboards, self).__init__(action)

        self.load_model('Dashboard')
        self.load_model('Wall')

    def index(self):
        print "index page"
        return self.load_view('dashboards/index.html')

    def register(self):
        print "register page"
        return self.load_view('dashboards/register.html')

    def new(self):
        print "new user controller"
        query = self.models['Dashboard'].first_user_query()
        user_level =  query
        user_info = {
        "email" : request.form['email'],
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "password" : request.form['password'],
        "user_level" : query,
        "pw_confirm": request.form['pw_confirm']
        }
        errors = []
        creation_status = self.models['Dashboard'].creation_validation(user_info)
        print "creation validation running"
        if creation_status['status'] == True:
            self.models['Dashboard'].new_user(user_info)
            session['id'] = self.models['Dashboard'].get_user_info_by_email(user_info)
            return redirect('/dashboard')
        else:
            print "validation failed"
            flash(creation_status['errors'])
            return redirect('/register')

    def signin(self):
        print "loading signin page"
        return self.load_view('/dashboards/signin.html')

    def validate_login(self):
        print "validations controller"
        login_info = {
        "email" : request.form['email'],
        "password" : request.form['password']
        }
        errors=[]
        user_info = self.models['Dashboard'].get_user_info_by_email(login_info)
        print "user info:",user_info
        if user_info == "user does not exist":
            flash("user does not exist.")
            return redirect('/signin')
        login_status = self.models['Dashboard'].login_validation(login_info, user_info)
        if login_status['status'] == True:
            print "true enough"
            user_id = user_info['id']
            session['id'] = user_id
            print "session id", session['id']
            session['user_level'] = user_info['user_level']
            print session['id'], session['user_level']
            return redirect('/dashboard')
        else:
            flash("incorrect password.")
            return redirect('/signin')

    def dashboard(self):
        print "user dashboard page"
        users = self.models['Dashboard'].get_all_users()
        return self.load_view('/dashboards/dashboard.html', users=users)

    def logout(self):
        session.clear()
        print "sessions cleared"
        return redirect('/')

    def destroy(self, id):
        print "destroy dialog"
        self.models['Dashboard'].delete_user_by_id(id)
        return redirect('/dashboard')

    def edit(self, id):
        print "edit page"
        user_info = self.models['Dashboard'].get_user_info_by_id(id)
        return self.load_view('/dashboards/edit.html', user=user_info, id=id)

    def update(self, id):
        print "updating info"
        user_info = {
        "email" : request.form['email'],
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "id" : id
        }
        update_status = self.models['Dashboard'].update_validation(user_info)
        if update_status['status'] == True:
            self.models['Dashboard'].update_user(user_info)
            return redirect('/dashboard')
        else:
            print "validation failed"
            flash(update_status['errors'])
            return redirect('/dashboard')

    def nocango(self):
        print "this isn't a supported page."
        return redirect('/')

    def update_password(self, id):
        if id == session['id']:
            user_info = self.models['Dashboard'].get_user_info_by_id(session['id'])
            password_info = {
            "email" : user_info['email'],
            "password" : request.form['password'],
            "pw_confirm" : request.form['pw_confirm'],
            "id" : session['id']
            }
            print "in update passwrod, session['id'] =", session['id']
            # self.models['Dashboard'].
            pw_update_status = self.models['Dashboard'].update_password(password_info)
            print pw_update_status

            return redirect('/dashboard')
        else:
            return redirect('/logout')

    def update_description(self, id):
        description_info = {
        "description" : request.form['description'],
        "id" : session['id']
        }
        self.models['Dashboard'].update_description(description_info)
        return redirect('/dashboard')

    def admin_create(self):
        return self.load_view('/dashboards/admin_create.html')

    def admin_new(self):
        user_info = {
        "email" : request.form['email'],
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "password" : request.form['password'],
        "user_level" : request.form['user_level'],
        "pw_confirm": request.form['pw_confirm']
        }
        errors = []
        creation_status = self.models['Dashboard'].creation_validation(user_info)
        print "creation validation running"
        if creation_status['status'] == True:
            self.models['Dashboard'].new_user(user_info)
            return redirect('/dashboard')
        else:
            print "validation failed"
            flash(creation_status['errors'])
            return redirect('/register')

    def wall(self, id):
        print " loading The Wall "
        user = self.models['Dashboard'].get_user_info_by_id(id)
        messages = self.models['Wall'].get_messages_by_wall(id)
        comments_result = self.models['Wall'].get_comments_by_wall(id)
        return self.load_view('walls/wall.html', messages=messages, user=user, id=id, comments=comments_result)

    def new_message(self):
        print "new message function"
        print request.form['content']
        print request.form['wall_id']
        message_data = {
        "content" : request.form['content'],
        "posted_by" : session['id'],
        "wall_id" : request.form['wall_id']
        }
        print message_data
        self.models['Wall'].create_message(message_data)
        print "message posted successfully"
        return redirect('/users/'+str(request.form['wall_id'])+'/wall')

    def add_comment(self, id):
        print "new comment"
        comment_data = {
        "content" : request.form['content'],
        "message_id" : id,
        "posted_by": session['id']
        }
        print comment_data
        print "comment"*250
        self.models['Wall'].add_comment(comment_data)
        return redirect('/users/'+str(request.form['wall_id'])+'/wall')

    def remove_post(self, id):
        print "deleting post"
        self.models['Wall'].remove_post(id)
        return redirect('/dashboard')
