import datetime


class RequestType(object):
    SMS = 'SMS'
    REST = 'REST'
    FACEBOOK = 'FACEBOOK'


class BanterMessageID:
    @staticmethod
    def buildFromSMS(sid):
        return RequestType.SMS + '_' + sid

    @staticmethod
    def buildFromREST(id):
        return RequestType.REST + '_' + id

    @staticmethod
    def buildFromFacebook(mid):
        return RequestType.FACEBOOK + '_' + mid


class BanterMessage(object):
    # timestamp
    # input
    # request type
    # partner
    # sms
    #   sid
    #   sending number
    #   receiving number
    #   timestamp
    # FACEBOOK
    #   mid
    #   facebook id
    #   timestamp
    # REST
    #   user id - how to route
    #   message id
    def __init__(self, id, text, requestType, partner, sourceInfo):
        self.id = id
        self.input = {'text': text}
        self.output = {'text': None, 'link': None}
        self.requestType = requestType
        self.partner = partner
        self.ts = datetime.datetime.now()
        self.sourceInfo = sourceInfo

    def __str__(self):
        return """id - {}, text - {}, requestType - {}, partner - {}, sourceInfo - {}""".format(
                                                                                            self.id,
                                                                                            self.input['text'],
                                                                                            self.requestType,
                                                                                            self.partner,
                                                                                            self.sourceInfo)
