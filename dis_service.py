import time
import logging
import yaml
from banter_message import BanterMessage, BanterMessageID, RequestType
from publish_service import PublishService

logger = logging.getLogger(__name__)


class DISService(object):

    def __init__(self):
        self.publish_service = PublishService()
        with open("resources/dis_config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        PROJ_ENV = cfg['proj_env']
        self.publish_wait_timeout = cfg[PROJ_ENV]['publish_wait_timeout']
        logger.debug('Publish wait timeout - %d', self.publish_wait_timeout)

    def dispatch(self, banter_message):
        send_status = False
        if banter_message:
            send_status = self.publish_service.publish_message(banter_message)
            if not send_status:
                time.sleep(self.publish_wait_timeout)
                send_status = self.publish_service.publish_message(banter_message)
        return send_status
