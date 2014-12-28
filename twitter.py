__author__ = 'Fundor333'

from twython import TwythonStreamer

from DatabaseMongoClass import database
from datitwitter import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET


NAMEDB = "twitter"
DBM = database(NAMEDB, 'localhost', 27017)
COLLECTIONNAME = "tweet"


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code
        self.disconnect()


def main():
    stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.statuses.filter(locations="10.623150,44.791538,13.101060,46.680580")


if __name__ == '__main__':
    main()