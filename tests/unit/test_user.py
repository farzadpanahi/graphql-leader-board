from unittest import TestCase

from models.user import User


class TestUser(TestCase):
    def test_add_point_new_obj(self):
        user = User(
            id='123',
            name='test name',
            address='earth',
            age=32
        )

        result = user.add_point()

        self.assertTrue(result)
        self.assertEqual(user.points, 1)

    def test_add_point_current_obj(self):
        user = User(
            id='123',
            name='test name',
            address='earth',
            age=32,
            points=22
        )

        result = user.add_point()

        self.assertTrue(result)
        self.assertEqual(user.points, 23)

    def test_sub_point_new_obj(self):
        user = User(
            id='123',
            name='test name',
            address='earth',
            age=32
        )

        result = user.sub_point()

        self.assertFalse(result)
        self.assertEqual(user.points, 0)

    def test_sub_point_current_obj_points_eq_1(self):
        user = User(
            id='123',
            name='test name',
            address='earth',
            age=32,
            points=1
        )

        result = user.sub_point()

        self.assertTrue(result)
        self.assertEqual(user.points, 0)

    def test_sub_point_current_obj(self):
        user = User(
            id='123',
            name='test name',
            address='earth',
            age=32,
            points=22
        )

        result = user.sub_point()

        self.assertTrue(result)
        self.assertEqual(user.points, 21)


