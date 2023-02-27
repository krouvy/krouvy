events = [
    {
        "timestamp": 1554583508000,
        "type": "itemViewEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
        "timestamp": 1555296337000,
        "type": "itemViewEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
        "timestamp": 1549461608000,
        "type": "itemBuyEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]


class Event:
    def __init__(self, timestamp=0, type='', session_id=''):
        self.timestamp = timestamp
        self.type = type
        self.session_id = session_id

    def init_values(self, dict):
        self.timestamp = dict.get("timestamp")
        self.type = dict.get("type")
        self.session_id = dict.get("session_id")


for event in events:
    for_event = Event()
    for_event.init_values(event)
    print(for_event.timestamp)
