import unittest
from mock import patch
from banter_message import BanterMessage, BanterMessageID, RequestType
from publish_service import PublishService
from pps_pub_service import PpsPubService


class TestPublishService(unittest.TestCase):

    def setUp(self):
        self.banterMessage = BanterMessage(BanterMessageID.buildFromFacebook('store-info1'),
                                      'in',
                                      RequestType.FACEBOOK,
                                      'menkens',
                                      {})

    def test_get_instance_with_null_string(self):
        publishService = PublishService()
        assert publishService.get_instance('') is None

    def test_get_instance_with_pypubsub_string(self):
        publishService = PublishService()
        assert isinstance(publishService.get_instance('pypubsub'), PpsPubService)

    def test_get_instance_with_Pypubsub_string(self):
        publishService = PublishService()
        assert publishService.get_instance('Pypubsub') is None

    def test_get_instance_with_other_string(self):
        publishService = PublishService()
        assert publishService.get_instance('localpubsub') is None

    @patch('publish_service.PublishService.get_instance')
    def test_publish_message(self, mock_get_instance):
        mock_get_instance.return_value = PpsPubService()
        publishService = PublishService()
        assert publishService.publish_message(self.banterMessage) == True

    @patch('publish_service.PublishService.get_instance')
    def test_publish_message_with_null_publish_instance(self, mock_get_instance):
        mock_get_instance.return_value = None
        publishService = PublishService()
        assert publishService.publish_message(self.banterMessage) == False

    @patch('publish_service.PpsPubService.publish_message')
    def test_publish_message_with_null_publish_instance(self, mock_publish_message):
        mock_publish_message.return_value = False
        publishService = PublishService()
        assert publishService.publish_message(self.banterMessage) == False
