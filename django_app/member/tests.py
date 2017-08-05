from django.test import TestCase, TransactionTestCase


# Create your tests here.
from member.models import User, Relation


class UserModelTest(TransactionTestCase):
    def test_user(self):
        test_user = User.objects.create(email='123@123.com', nickname='test')
        match_user = User.objects.first()

        self.assertEquals(test_user, match_user)

    def test_relation(self):
        user1 = User.objects.create(email='1231@123.com', nickname='test1')
        user2 = User.objects.create(email='1232@123.com', nickname='test2')

        relation = Relation.objects.create(user1=user1, user2=user2)
        relation_m = Relation.objects.first()

        self.assertEqual(relation, relation_m)
        self.assertEqual(user1, relation_m.user1)
        self.assertEqual(user2, relation_m.user2)
