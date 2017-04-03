from pubsub import pub


class Listener:
    def onTestTopic(self, signal, sender, banterMessage):
        print('Method Listener.onTestTopic received: ', repr(signal), repr(sender), repr(banterMessage))
        sender.set_publish_successful(True)

    def __call__(self, **kwargs):
        print('Listener instance received: ', kwargs)


listenerObj = Listener()


pub.subscribe(listenerObj.onTestTopic, 'test_topic')
