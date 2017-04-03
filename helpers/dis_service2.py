#from pydispatch import dispatcher
from banter_message import BanterMessage, BanterMessageID, RequestType
from pubsub import pub
import pypubsub_topic
#import pypubsub_sender as publisher
import pypubsub_listener
import time
import logging
#import pypubsub_notifhandler
#import exchandle


logger = logging.getLogger(__name__)
timeoutSeconds = 2


class DISService(object):
    def dispatch(self, banterMessage):

        publish_successful = self.publish_message(banterMessage)
        return publish_successful


    def __init__(self):
      self.publish_successful = False


    def set_publish_successful(self, val):
        self.publish_successful = val


    def publish_message(self, banterMessage):
        # Assuming message is valid
        # publish_successful = dispatcher.send(signal='INCOMING_MESSAGE', sender=self, banterMessage=banterMessage)

        try:

            #pub.addTopicDefnProvider(pypubsub_topic, pub.TOPIC_TREE_FROM_CLASS)
            #pub.setTopicUnspecifiedFatal()
            #pub.setNotificationFlags(sendMessage=True)

            #print('-----------------------')
            pub.sendMessage('test_topic', signal='INCOMING_MESSAGE', sender=self, banterMessage=banterMessage)
            #print('------- Publish Successful ---------- ' + str(self.publish_successful))
            if self.publish_successful:
                #print('------- Publish Successful ----------')
                return True
            else:
                #print('------- Sleep and Retry ----------')
                time.sleep(timeoutSeconds)
                #publish_successful = dispatcher.send(signal='INCOMING_MESSAGE', sender=self, banterMessage=banterMessage)
                pub.sendMessage('test_topic', signal='INCOMING_MESSAGE', sender=self, banterMessage=banterMessage)
                if self.publish_successful:
                    #print('------- Publish Successful ----------')
                    return True
                else:
                    #print('------- Publish Not Successful ----------')
                    return False

            #print('------- done ----------')

        except Exception:
            import traceback

            traceback.print_exc()

        #print('------ exiting --------')



if __name__ == "__main__":
    d = DISService()
    banterMessage = BanterMessage(BanterMessageID.buildFromFacebook('himom'),
                                  'in',
                                  RequestType.FACEBOOK,
                                  'menkens',
                                  {})
    print d.dispatch(banterMessage)
