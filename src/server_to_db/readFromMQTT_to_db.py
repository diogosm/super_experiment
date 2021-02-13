#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import json
from urllib.request import urlopen
import time
from datetime import datetime

class Dados:
    def __init__(self):
        self.data = ""
        self.conn = None
        self.last_updated = datetime.now()
        self.saved = 0
        self.READ_API_KEY="Q2H9IGQP36BM9GAT"
        self.CHANNEL_ID="1301242"

    def connect(self):
        self.conn = urlopen("https://api.thingspeak.com/channels/%s/feeds.json?api_key=%s&results=10" \
                % (self.CHANNEL_ID, self.READ_API_KEY))
        if self.conn.getcode() == 200:
            self.last_updated = datetime.now()
            self.saved = 0

    def disconnect(self):
        self.conn.close()

    def getData(self):
        http_response = self.conn.getcode()
        if self.conn is not None and http_response == 200: ## SUCESSO
            response = self.conn.read()
            self.data = json.loads(response)

            #print(json.dumps(data, indent=4))


def printDados(classe):
    print(", ".join("%s: %s\n" % val for val in vars(classe).items()))


def main():
    dados = Dados()

    dados.connect()
    dados.getData()
    dados.disconnect()

    printDados(dados)


if __name__ == "__main__":
    main()
    time.sleep(5)
