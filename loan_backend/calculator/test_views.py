from rest_framework.test import APIClient
from django.test import TestCase

from django.contrib.auth.models import User
from .models import Operation, Record
from .views import RecordList, OperationRequest


class TestRecordListView(TestCase):
    """
    Test `RecordList` endpoint
    """
    def setUp(self):
        # API Client
        self.client = APIClient()
        # Set up operations
        op1 = Operation.objects.create(type=1, cost=5)
        op2 = Operation.objects.create(type=2, cost=5)

        # Set up a user
        self.user = User.objects.create_user(username='tester', email='tester@island.com', password='glasser')
        self.other_user = User.objects.create_user(
            username='other_tester',
            email='other_tester@island.com',
            password='other_glasser'
        )

        # Set up some records
        Record.objects.create(
            operation=op1,
            user=self.user,
            amount=op1.cost,
            user_balance=90,
            operation_response="250"
        )
        Record.objects.create(
            operation=op2,
            user=self.user,
            amount=op2.cost,
            user_balance=85,
            operation_response="50"
        )
        Record.objects.create(
            operation=op1,
            user=self.user,
            amount=op1.cost,
            user_balance=80,
            operation_response="500"
        )

        # Other user records
        Record.objects.create(
            operation=op1,
            user=self.other_user,
            amount=op1.cost,
            user_balance=30,
            operation_response="3500"
        )
        Record.objects.create(
            operation=op1,
            user=self.other_user,
            amount=op1.cost,
            user_balance=25,
            operation_response="11500"
        )

    def test_returns_record_for_given_user(self):
        """
        Returned records by this endpoint should belong
        to the user sent as a parameter.
        """
        response = self.client.get(f'/calculator/records/{self.user.pk}/')

        # Records for other user should not be present in this response
        self.assertEqual(len(response.data), Record.objects.filter(user=self.user).count())


class TestOperationRequestView(TestCase):
    """
    Test `OperationRequest` endpoint
    """
    def setUp(self):
        # API Client
        self.client = APIClient()

    def test_addition_operation(self):
        """
        Operation sent is addition and expected result
        matches it
        """
        pass

    def test_subtract_operation(self):
        """
        Operation sent is subtract and expected result
        matches it
        """
        pass

    def test_multiplication_operation(self):
        """
        Operation sent is multiplication and expected result
        matches it
        """
        pass

    def test_division_operation(self):
        """
        Operation sent is division and expected result
        matches it
        """
        pass

    def test_square_root_operation(self):
        """
        Operation sent is square root and expected result
        matches it
        """
        pass

    def test_random_string_operation(self):
        """
        Operation sent is random string and expected result
        matches it. Special case as any operation outside
        defined values will be treated like this.
        """
        pass

    def test_no_operation_should_fail(self):
        """
        Requesting without operation should quickly return
        a bad formed request.
        """
        body = {'operand_a': 32, 'operand_b': 28}
        response = self.client.post('/calculator/operation/', body, format='json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], 'Operation is required')
