from django.test import TestCase
from django.urls import reverse
from api.models import Token
from rest_framework.test import APIClient
from django.contrib.auth.models import User, Permission
import yaml


class SchemaValidationTestCase(TestCase):
    script_schema = """
    $id: https://github.com/lsst-ts/ts_salobj/TestScript.yaml
    $schema: http://json-schema.org/draft-07/schema#
    additionalProperties: false
    description: Configuration for TestScript
    properties:
        fail_cleanup:
            default: false
            description: If true then raise an exception in the "cleanup" method.
            type: boolean
        fail_run:
            default: false
            description: If true then raise an exception in the "run" method afer the "start" checkpoint but before waiting.
            type: boolean
        wait_time:
            default: 0
            description: Time to wait, in seconds
            minimum: 0
            type: number
    required:
    - wait_time
    - fail_run
    - fail_cleanup
    title: TestScript v1
    type: object
    """
    maxDiff = None

    def setUp(self):
        """Define the test suite setup."""
        # Arrange:
        self.client = APIClient()
        self.username = 'test'
        self.password = 'password'
        self.user = User.objects.create_user(
            username=self.username,
            password='password',
            email='test@user.cl',
            first_name='First',
            last_name='Last',
        )
        self.user.user_permissions.add(Permission.objects.get(name='Execute Commands'))
        self.login_url = reverse('login')
        self.validate_token_url = reverse('validate-token')
        self.logout_url = reverse('logout')
        self.expected_permissions = {
            'execute_commands': True,
        }

        data = {'username': self.username, 'password': self.password}
        response = self.client.post(self.login_url, data, format='json')
        token = Token.objects.filter(user__username=self.username).first()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_valid_config(self):
        """Test schema validation works for a valid config yaml string"""
        # Act:
        url = reverse('validate-config-schema')
        data = {
            'config': "wait_time: 3600",
            'schema': self.script_schema
        }
        response = self.client.post(url, data, format='json')

        # Assert:
        expected_data = {
            "title": "None",
            "output": {'wait_time': 3600, 'fail_cleanup': False, 'fail_run': False}
        }

        self.assertEqual(
            response.data,
            expected_data
        )

    def test_syntax_error(self):
        """Test validation output of an unparsable config file"""
        configs = [
            "wait_time: -\na:""",  # ScannerError
            "fail_cleanup: \nw:'",  # ScannerError
            ":"  # ParserError
        ]

        expected_data = [
            {'error': {'context': None,
                       'note': None,
                       'problem': 'sequence entries are not allowed here',
                       'problem_mark': {'buffer': 'wait_time: -\na:\x00',
                                        'column': 11,
                                        'index': 11,
                                        'line': 0,
                                        'name': '<unicode string>',
                                        'pointer': 11}},
             'title': 'ERROR WHILE PARSING YAML STRING'},
            {'error': {'context': 'while scanning a simple key',
                       'note': None,
                       'problem': "could not find expected ':'",
                       'problem_mark': {'buffer': "fail_cleanup: \nw:'\x00",
                                        'column': 3,
                                        'index': 18,
                                        'line': 1,
                                        'name': '<unicode string>',
                                        'pointer': 18}},
             'title': 'ERROR WHILE PARSING YAML STRING'},
            {'error': {'context': 'while parsing a block mapping',
                       'note': None,
                       'problem': "expected <block end>, but found ':'",
                       'problem_mark': {'buffer': ':\x00',
                                        'column': 0,
                                        'index': 0,
                                        'line': 0,
                                        'name': '<unicode string>',
                                        'pointer': 0}},
             'title': 'ERROR WHILE PARSING YAML STRING'}
            ]

        for config, expected_datum in zip(configs, expected_data):
            # Act:
            url = reverse('validate-config-schema')
            request_data = {
                'config': config,
                'schema': self.script_schema
            }
            response = self.client.post(url, request_data, format='json')
            # Assert:
            self.assertEqual(
                response.data,
                expected_datum
            )

    def test_invalid_config(self):
        """Test validation output of an invalid config file"""

        configs = [
            "wait_time: 'asd'",
        ]
        for config in configs:
            # Act:
            url = reverse('validate-config-schema')
            request_data = {
                'config': config,
                'schema': self.script_schema
            }
            response = self.client.post(url, request_data, format='json')

            # Assert:
            expected_data = {
                'error': {
                    'cause': None,
                    'context': [],
                    'instance': 'asd',
                    'message': "'asd' is not of type 'number'",
                    'parent': None,
                    'path': ['wait_time'],
                    'relative_path': ['wait_time'],
                    'relative_schema_path': ['properties', 'wait_time', 'type'],
                    'schema': {
                        'default': 0,
                        'description': 'Time to wait, in seconds',
                        'minimum': 0,
                        'type': 'number'
                    },
                    'schema_path': ['properties', 'wait_time', 'type'],
                    'validator': 'type',
                    'validator_value': 'number'
                },
                'title': 'INVALID CONFIG YAML'
            }

            self.assertEqual(
                response.data,
                expected_data
            )
