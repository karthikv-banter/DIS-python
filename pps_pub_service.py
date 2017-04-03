import yaml
import logging
from pubsub import pub

logger = logging.getLogger(__name__)


class PpsPubService(object):

    def __init__(self):
        with open("resources/dis_config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        PROJ_ENV = cfg['proj_env']
        self.topic = cfg[PROJ_ENV]['pypubsub']['topic']

    def publish_message(self, banterMessage):
        pub.sendMessage(self.topic, banterMessage=banterMessage)
        logger.debug('Pypubsub message - %s', str(banterMessage))
        return True

    def __str__(self):
        return 'from PpsPubService'
