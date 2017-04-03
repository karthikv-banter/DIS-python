import yaml
import logging
from pps_pub_service import PpsPubService

logger = logging.getLogger(__name__)


class PublishInstance(object):

    def __init__(self):
        with open("resources/config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        self.publish_queue = cfg['publish_queue']
        logger.debug('Publish Queue - %s', self.publish_queue)

    def get_instance(self):
        ins = None
        if self.publish_queue == 'pypubsub':
            ins = PpsPubService()
        return ins
