# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base import serialize
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class RoleTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.conversations.v1.roles.create(friendly_name="friendly_name", type="conversation", permission=['permission'])

        values = {
            'FriendlyName': "friendly_name",
            'Type': "conversation",
            'Permission': serialize.map(['permission'], lambda e: e),
        }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://conversations.twilio.com/v1/Roles',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "Conversation Role",
                "type": "conversation",
                "permissions": [
                    "sendMessage",
                    "leaveConversation",
                    "editOwnMessage",
                    "deleteOwnMessage"
                ],
                "date_created": "2016-03-03T19:47:15Z",
                "date_updated": "2016-03-03T19:47:15Z",
                "url": "https://conversations.twilio.com/v1/Roles/RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.conversations.v1.roles.create(friendly_name="friendly_name", type="conversation", permission=['permission'])

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.conversations.v1.roles("RLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(permission=['permission'])

        values = {'Permission': serialize.map(['permission'], lambda e: e), }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://conversations.twilio.com/v1/Roles/RLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            data=values,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "Conversation Role",
                "type": "conversation",
                "permissions": [
                    "sendMessage",
                    "leaveConversation",
                    "editOwnMessage",
                    "deleteOwnMessage"
                ],
                "date_created": "2016-03-03T19:47:15Z",
                "date_updated": "2016-03-03T19:47:15Z",
                "url": "https://conversations.twilio.com/v1/Roles/RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.conversations.v1.roles("RLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(permission=['permission'])

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.conversations.v1.roles("RLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://conversations.twilio.com/v1/Roles/RLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.conversations.v1.roles("RLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.conversations.v1.roles("RLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://conversations.twilio.com/v1/Roles/RLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "Conversation Role",
                "type": "conversation",
                "permissions": [
                    "sendMessage",
                    "leaveConversation",
                    "editOwnMessage",
                    "deleteOwnMessage"
                ],
                "date_created": "2016-03-03T19:47:15Z",
                "date_updated": "2016-03-03T19:47:15Z",
                "url": "https://conversations.twilio.com/v1/Roles/RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.conversations.v1.roles("RLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.conversations.v1.roles.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://conversations.twilio.com/v1/Roles',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://conversations.twilio.com/v1/Roles?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://conversations.twilio.com/v1/Roles?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "roles"
                },
                "roles": [
                    {
                        "sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "Conversation Role",
                        "type": "conversation",
                        "permissions": [
                            "sendMessage",
                            "leaveConversation",
                            "editOwnMessage",
                            "deleteOwnMessage"
                        ],
                        "date_created": "2016-03-03T19:47:15Z",
                        "date_updated": "2016-03-03T19:47:15Z",
                        "url": "https://conversations.twilio.com/v1/Roles/RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            '''
        ))

        actual = self.client.conversations.v1.roles.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://conversations.twilio.com/v1/Roles?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://conversations.twilio.com/v1/Roles?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "roles"
                },
                "roles": []
            }
            '''
        ))

        actual = self.client.conversations.v1.roles.list()

        self.assertIsNotNone(actual)
