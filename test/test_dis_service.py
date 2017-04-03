import unittest
from mock import patch
from dis_service import DISService
from banter_message import BanterMessage, BanterMessageID, RequestType
from publish_service import PublishService


class TestDISService(unittest.TestCase):

    def setUp(self):
        self.banterMessage = BanterMessage(BanterMessageID.buildFromFacebook('store-info1'),
                                      'in',
                                      RequestType.FACEBOOK,
                                      'menkens',
                                      {})
        self.banterMessageNone = None

    def test_sender_return_value(self):
        disService = DISService()
        assert disService.dispatch(self.banterMessage) == True

    def test_sender_return_value_with_null_message(self):
        disService = DISService()
        assert disService.dispatch(self.banterMessageNone) == False

    @patch('dis_service.PublishService.publish_message')
    def test_sender_wait_true(self, mock_publish_message):
        mock_publish_message.side_effect = [False, True]
        disService = DISService()
        assert disService.dispatch(self.banterMessage) == True

    @patch('dis_service.PublishService.publish_message')
    def test_sender_wait_false(self, mock_publish_message):
        mock_publish_message.side_effect = [False, False]
        disService = DISService()
        assert disService.dispatch(self.banterMessage) == False
