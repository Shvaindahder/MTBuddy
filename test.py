import unittest
from app import db, create_app
from app.models.user import User
from app.models.meeting import Meeting
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

#     def test_password_hashing(self):
#         u = User(username = 'Polina')
#         u.set_password('avonamut1001')
#         self.assertFalse(u.check_password('avonamut2000'))
#         self.assertTrue(u.check_password('avonamut1001'))

#     def test_avatar(self):
#         u = User(username = 'Arthur', email = 'asimonan97@gmail.com')
#         self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/'
#                                         '4532a970196c3cb13306fc6584bc5a3e'
#                                         '?d=indenticon&s=128'))

#     def test_follow(self):
#         u1 = User(username = 'Arthur', email = 'asimonan97@gmail.com')
#         u2 = User(username = 'Maria', email = 'shema00@gmail.com')
#         db.session.add(u1)
#         db.session.add(u2)
#         db.session.commit()
#         self.assertEqual(u1.followers.all(), [])
#         self.assertEqual(u1.followed.all(), [])

#         u1.follow(u2)
#         db.session.commit()
#         self.assertTrue(u1.is_following(u2))
#         self.assertEqual(u1.followed.count(), 1)
#         self.assertEqual(u1.followers.count(), 0)
#         self.assertEqual(u1.followed.first().username, 'Maria')
#         self.assertEqual(u2.followers.count(), 1)
#         self.assertEqual(u2.followed.count(), 0)
#         self.assertEqual(u2.followers.first().username, 'Arthur')

#         u1.unfollow(u2)
#         db.session.commit()
#         self.assertFalse(u1.is_following(u2))
#         self.assertEqual(u1.followed.count(), 0)
#         self.assertEqual(u2.followers.count(), 0)

#     def test_follow_posts(self):
#         # create 4 users
#         u1 = User(username = 'Arthur', email = 'asimonan97@gmail.com')
#         u2 = User(username = 'Maria', email = 'shema00@gmail.com')
#         u3 = User(username = 'Polina', email = 'BrusnikovaP01@gmail.com')
#         u4 = User(username = 'Anastasiya', email = 'lipovaya99@gmail.com')
#         anon = User(username = 'Anonymous', email = 'anon97@gmail.com')
#         pop = User(username = 'Emma', email = 'eroberts91@gmail.com')
#         db.session.add_all([u1, u2, u3, u4, anon, pop])

#         # create posts
#         now = datetime.utcnow()
#         p1 = Post(body = 'post from Arthur', author = u1, timestamp = now + timedelta(seconds = 6))
#         p2 = Post(body = 'post from Maria', author = u2, timestamp = now + timedelta(seconds = 5))
#         p3 = Post(body = 'post from Polina', author = u3, timestamp = now + timedelta(seconds = 4))
#         p4 = Post(body = 'post from Nastya', author = u4, timestamp = now + timedelta(seconds = 3))
#         anon_post = Post(body = 'post from anonymous', author = anon, timestamp = now + timedelta(seconds = 2))
#         pop_post = Post(body = 'Ama Emma', author = pop, timestamp = now + timedelta(seconds = 1))
#         db.session.add_all([p1, p2, p3, p4, anon_post, pop_post])
#         db.session.commit()

#         # setup the followers
#         u1.follow(u2) # A follow M
#         u1.follow(u3) # A follow P
#         u1.follow(pop) # A follow pop
#         u2.follow(u4) # M follow N
#         u2.follow(u1) # M follow A
#         u2.follow(pop) # M follow pop
#         u3.follow(u1) # P follow A
#         u3.follow(pop) # P follow pop
#         u4.follow(u1) # N follow A
#         u4.follow(pop) # N follow pop
#         anon.follow(u1) # Anon follow A
#         anon.follow(pop) # Anon follow pop
#         db.session.commit()

#         # check the followed post of each user
#         f1 = u1.followed_posts().all()
#         f2 = u2.followed_posts().all()
#         f3 = u3.followed_posts().all()
#         f4 = u4.followed_posts().all()
#         anonf = anon.followed_posts().all()
#         popf = pop.followed_posts().all()
#         self.assertEqual(f1, [p1, p2, p3, pop_post])
#         self.assertEqual(f2, [p1, p2, p4, pop_post])
#         self.assertEqual(f3, [p1, p3, pop_post])
#         self.assertEqual(f4, [p1, p4, pop_post])
#         self.assertEqual(anonf, [p1, anon_post, pop_post])
#         self.assertEqual(popf, [pop_post])

# if __name__ == '__main__':
#     unittest.main(verbosity=2)
