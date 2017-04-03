import logging
import yaml
from pps_pub_service import PpsPubService

logger = logging.getLogger(__name__)


class PublishService(object):

    def __init__(self):
        with open("resources/dis_config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        PROJ_ENV = cfg['proj_env']
        self.publish_queue = cfg[PROJ_ENV]['publish_queue']
        logger.debug('Publish Queue - %s', self.publish_queue)

    def publish_message(self, banter_message):
        publishInstance = self.get_instance(self.publish_queue)
        logger.debug('Publish Instance - %s', publishInstance)
        if publishInstance:
            return publishInstance.publish_message(banter_message)
        return False

    def get_instance(self, publish_queue):
        ins = None
        if publish_queue == 'pypubsub':
            ins = PpsPubService()
        return ins
