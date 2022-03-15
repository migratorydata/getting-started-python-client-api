import time

import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.migratorydata_client_python import *
from config import Config

# Define the listener to handle live message and status notifications
class MyListener(MigratoryDataListener):
    def __init__(self):
        pass

    def on_status(self, status, info):
        print("Got status " + status + " - " + info)

    def on_message(self, message):
        print("Got message " + str(message))

def run_example():

    client = MigratoryDataClient()

    client.set_entitlement_token(Config.token)

    # attach your MigratoryDataListener
    client.set_listener(MyListener())

    client.set_encryption(Config.encryption)

    client.set_servers(Config.server)

    client.connect()

    client.subscribe([Config.subject])

    time.sleep(1)

    # publish a message every 3 seconds
    count = 1
    while True:
        content = "data - " + str(count)
        closure = "id" + str(count)
        client.publish(MigratoryDataMessage(Config.subject, content.encode('utf-8'), closure))
        count += 1
        time.sleep(2)

    # disconnect client from server
    client.disconnect() 

if __name__ == '__main__':
    run_example()