from system.core.model import Model

class Wall(Model):
    def __init__(self):
        super(Wall, self).__init__()

    def get_messages_by_wall(self, userid):
        print "retrieving messages from db"
        messages_query = "SELECT * FROM messages WHERE wall_id = %s"
        messages_data = [userid]
        return self.db.query_db(messages_query, messages_data)

    def get_comments_by_wall(self, userid):
        print "retrieving comments from db"
        comments_query = "SELECT comments.id, comments.content, comments.posted_by, comments.message_id, messages.wall_id FROM comments JOIN messages ON comments.message_id = messages.id WHERE messages.wall_id = %s"
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
