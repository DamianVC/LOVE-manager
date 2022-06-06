from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from api.models import ScriptConfiguration, Token
from rest_framework.test import APIClient
import dateutil.parser


class ScriptQueueTestCase(TestCase):
    def setUp(self):
        """Define the test suite setup.
        Define a general arrange, this is the same for all the future declared functions.
        """
        self.client = APIClient()

        self.user = User.objects.create_user(
            username="user",
            password="password",
            email="test@user.cl",
            first_name="First",
            last_name="Last",
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        new_script_obj = {
            "script_path": "auxtel/test.py",
            "config_name": "test_script",
            "config_schema": "[test,config]",
            "script_type": "standard",
        }
        new_script_obj2 = {
            "script_path": "maintel/test2.py",
            "config_name": "test_script2",
            "config_schema": "[test2,config2]",
            "script_type": "external",
        }
        new_script_obj3 = {
            "script_path": "auxtel/test.py",
            "config_name": "test_script2",
            "config_schema": "[test,config_test2]",
            "script_type": "standard",
        }

        self.new_script = ScriptConfiguration.objects.create(
            script_path=new_script_obj["script_path"],
            config_name=new_script_obj["config_name"],
            config_schema=new_script_obj["config_schema"],
            script_type=new_script_obj["script_type"],
        )
        self.new_script2 = ScriptConfiguration.objects.create(
            script_path=new_script_obj2["script_path"],
            config_name=new_script_obj2["config_name"],
            config_schema=new_script_obj2["config_schema"],
            script_type=new_script_obj2["script_type"],
        )
        self.new_script3 = ScriptConfiguration.objects.create(
            script_path=new_script_obj3["script_path"],
            config_name=new_script_obj3["config_name"],
            config_schema=new_script_obj3["config_schema"],
            script_type=new_script_obj3["script_type"],
        )

    def test_scriptconfiguration_listbydate(self):
        """Test listing all the scripts configurations by their date
        This request should return an object sorted by the newest to the oldest date
        """
        # Act:
        url = reverse("script-configuration-list")
        response = self.client.get(url, format="json")

        # Assert
        self.assertEqual(response.status_code, 200)
        new_script2_datetime = dateutil.parser.isoparse(
            response.data[0]["creation_timestamp"]
        )
        new_script_datetime = dateutil.parser.isoparse(
            response.data[1]["creation_timestamp"]
        )
        self.assertTrue(new_script2_datetime > new_script_datetime)
        self.assertEqual(len(response.data), 3)

    def test_scriptconfiguration_listbypath(self):
        """Test listing the scripts by their path
        This request should return all the scripts that have the same path AND type
        """
        # Act:
        url = reverse("script-configuration-list")
        response = self.client.get(
            url
            + "?path="
            + self.new_script.script_path
            + "&type="
            + self.new_script.script_type,
            format="json",
        )
        print(response)
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        new_script3_datetime = dateutil.parser.isoparse(
            response.data[0]["creation_timestamp"]
        )
        new_script_datetime = dateutil.parser.isoparse(
            response.data[1]["creation_timestamp"]
        )
        self.assertTrue(new_script3_datetime > new_script_datetime)

    def test_scriptconfiguration_create(self):
        """Test creation for a new script configuration object"""
        # Act:
        url = reverse("script-configuration-list")
        payload = {
            "script_path": "pathB/test2",
            "config_name": "test_script2",
            "config_schema": "[test2,config2]",
            "script_type": "external",
        }
        response = self.client.post(url, payload, format="json")

        # Assert
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["script_path"], payload["script_path"])
        self.assertEqual(response.data["config_name"], payload["config_name"])
        self.assertEqual(response.data["config_schema"], payload["config_schema"])
        self.assertEqual(response.data["script_type"], payload["script_type"])

    def test_scriptconfiguration_update(self):
        """Test updating the config_schema of a script configuration"""

        # Act:
        url = reverse("script-configuration-detail", args=[self.new_script.pk])
        payload = {"config_schema": "[TEST, CONFIGTEST]"}
        response = self.client.patch(url, payload, format="json")

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["script_path"], self.new_script.script_path)
        self.assertEqual(response.data["config_name"], self.new_script.config_name)
        self.assertEqual(response.data["config_schema"], payload["config_schema"])
        self.assertEqual(response.data["script_type"], self.new_script.script_type)
