import yaml
import unittest
from mock import patch
from banter_message import BanterMessage, BanterMessageID, RequestType
from pps_pub_service import PpsPubService
from pubsub import pub


class Listener:

    def __init__(self):
        self.message_counter = 0

    def onTestTopic(self, banterMessage):
        assert banterMessage.id == 'FACEBOOK_store-info1'
        assert banterMessage.input['text'] == 'in'
        assert banterMessage.requestType == 'FACEBOOK'
        assert banterMessage.partner == 'menkens'
        assert banterMessage.sourceInfo == {}

    def onTestTopicMultiple(self, banterMessage):
        self.message_counter += 1


class TestPublishService(unittest.TestCase):

    def setUp(self):
        self.ppsPubService = PpsPubService()
        self.listenerObj = Listener()
        with open("resources/dis_config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        PROJ_ENV = cfg['proj_env']
        self.topic = cfg[PROJ_ENV]['pypubsub']['topic']
        self.banterMessage1 = BanterMessage(BanterMessageID.buildFromFacebook('store-info1'),
                                      'in',
                                      RequestType.FACEBOOK,
                                      'menkens',
                                      {})
        self.banterMessage2 = BanterMessage(BanterMessageID.buildFromFacebook('store-info2'),
                                      'in',
                                      RequestType.FACEBOOK,
                                      'menkens',
                                      {})
        self.banterMessage3 = BanterMessage(BanterMessageID.buildFromFacebook('store-info3'),
                                      'in',
                                      RequestType.FACEBOOK,
                                      'menkens',
                                      {})

    def test_published_message_in_queue(self):
        pub.subscribe(self.listenerObj.onTestTopic, self.topic)
        self.ppsPubService.publish_message(self.banterMessage1)

    def test_multiple_same_published_messages_in_queue(self):
        pub.subscribe(self.listenerObj.onTestTopicMultiple, self.topic)
        self.ppsPubService.publish_message(self.banterMessage1)
        self.ppsPubService.publish_message(self.banterMessage1)
        assert self.listenerObj.message_counter == 2

    def test_multiple_different_published_messages_in_queue(self):
        pub.subscribe(self.listenerObj.onTestTopicMultiple, self.topic)
        self.ppsPubService.publish_message(self.banterMessage1)
        self.ppsPubService.publish_message(self.banterMessage2)
        self.ppsPubService.publish_message(self.banterMessage3)
        assert self.listenerObj.message_counter == 3
