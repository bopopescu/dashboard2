from system.core.model import Model

class Wall(Model):
    def __init__(self):
        super(Wall, self).__init__()

    def get_messages_by_wall(self, userid):
        print "retrieving messages from db"
        messages_query = "SELECT messages.id, messages.content, messages.wall_id, messages.created_at, CONCAT_WS(' ',users.first_name, users.last_name) AS message_poster_name FROM messages JOIN users ON messages.posted_by = users.id WHERE wall_id = %s"
        messages_data = [userid]
        return self.db.query_db(messages_query, messages_data)

    def get_comments_by_wall(self, userid):
        print "retrieving comments from db"
        comments_query = "SELECT comments.id, comments.content, comments.posted_by, comments.message_id, messages.wall_id, CONCAT_WS(' ',users.first_name, users.last_name) AS posted_by_name FROM comments JOIN messages ON comments.message_id = messages.id JOIN users ON comments.posted_by = users.id WHERE messages.wall_id = %s"
        comments_data = [userid]
        comments_result = self.db.query_db(comments_query, comments_data)
        print ":::::comments data::::",comments_result
        return comments_result

    def create_message(self, info):
        create_query = "INSERT INTO messages (content, posted_by, wall_id, created_at) VALUES (%s, %s, %s, NOW())"
        create_data = [info['content'], info['posted_by'], info['wall_id']]
        return self.db.query_db(create_query, create_data)

    def add_comment(self, info):
        create_query = "INSERT INTO comments (content, posted_by, message_id, created_at) VALUES (%s, %s, %s, NOW())"
        create_data = [info['content'], info['posted_by'], info['message_id']]
        return self.db.query_db(create_query, create_data)

    def remove_post(self, id):
        destroy_query = "DELETE FROM messages WHERE id = %s"
        destroy_id = [id]
        return self.db.query_db(destroy_query, destroy_id)

    def remove_comment(self, id):
        destroy_query = "DELETE FROM comments WHERE id = %s"
        destroy_id = [id]
        return self.db.query_db(destroy_query, destroy_id)
