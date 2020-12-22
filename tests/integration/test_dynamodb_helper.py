from unittest import TestCase
import configparser
from dynamodb_helper import UserTable
from models.user import User
import uuid


class TestUserTable(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = configparser.ConfigParser()
        cls.config.read('../../config.ini')

    def test_put_user(self):
        user_table = UserTable(
            region=self.config['dynamodb']['region'],
            table_name=self.config['dynamodb']['table']
        )

        user_to_put = User(
            id=str(uuid.uuid4()),
            name='test-user',
            address='nowhere',
            age=83,
            points=0
        )

        result = user_table.put_user(user=user_to_put)

        self.assertTrue(result)

        user_read = user_table.get_user(user_id=user_to_put.id)
        print(user_read)

        self.assertEqual(user_to_put, user_read)

    def test_get_user(self):
        user_table = UserTable(
            region=self.config['dynamodb']['region'],
            table_name=self.config['dynamodb']['table']
        )

        user_to_put = User(
            id=str(uuid.uuid4()),
            name='test-user',
            address='nowhere',
            age=83,
            points=0
        )

        result = user_table.put_user(user=user_to_put)

        self.assertTrue(result)

        user_read = user_table.get_user(user_id=user_to_put.id)
        print(user_read)

        self.assertEqual(user_to_put, user_read)

    def test_update_user(self):
        user_table = UserTable(
            region=self.config['dynamodb']['region'],
            table_name=self.config['dynamodb']['table']
        )

        user_to_put = User(
            id=str(uuid.uuid4()),
            name='test-user',
            address='nowhere',
            age=83,
            points=0
        )

        result = user_table.put_user(user=user_to_put)
        self.assertTrue(result)

        user_read = user_table.get_user(user_id=user_to_put.id)
        print(user_read)

        self.assertEqual(user_to_put, user_read)

        # -- update user
        user_to_update = User(
            id=user_read.id,
            name='new name',
            address='new address',
            age=38,
            points=22
        )

        result = user_table.update_user(user=user_to_update)
        self.assertTrue(result)

        user_read = user_table.get_user(user_id=user_to_update.id)
        print(user_read)

        self.assertEqual(user_to_update, user_read)

    def test_get_all_users(self):
        user_table = UserTable(
            region=self.config['dynamodb']['region'],
            table_name=self.config['dynamodb']['table']
        )

        new_user_ids = set()

        user_to_put = User(
            id=str(uuid.uuid4()),
            name='user1',
            address='nowhere',
            age=83,
            points=0
        )

        result = user_table.put_user(user=user_to_put)

        self.assertTrue(result)
        new_user_ids.add(user_to_put.id)

        user_to_put = User(
            id=str(uuid.uuid4()),
            name='user2',
            address='nowhere',
            age=83,
            points=0
        )

        result = user_table.put_user(user=user_to_put)

        self.assertTrue(result)
        new_user_ids.add(user_to_put.id)

        user_to_put = User(
            id=str(uuid.uuid4()),
            name='user3',
            address='nowhere',
            age=83,
            points=0
        )

        result = user_table.put_user(user=user_to_put)

        self.assertTrue(result)
        new_user_ids.add(user_to_put.id)

        users = user_table.get_all_users()
        all_user_ids = set([user.id for user in users])

        self.assertTrue(new_user_ids.issubset(all_user_ids))
