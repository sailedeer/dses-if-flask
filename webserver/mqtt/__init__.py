"""MQTT related utilities for the webserver."""

import json
import logging
from time import time_ns
from typing import Any, Dict

from flask_mqtt import Mqtt
from paho.mqtt.client import MQTTMessage

from webserver.dish import DishController, dishes

logger = logging.getLogger(__name__)

mqtt_client = Mqtt()


@mqtt_client.on_connect()
def handle_connect(_, __, ___, ____):
    """Handle first connection set-up."""
    mqtt_client.subscribe("ctrl/rollcall")


@mqtt_client.on_topic("ctrl/rollcall")
def handle_rollcall_topic(_, __, message: MQTTMessage):
    """Handle rollcall messages."""
    payload: Dict[str, Any] = {}
    try:
        payload = json.loads(message.payload)
    except json.JSONDecodeError:
        # ill-formatted, just drop the packet
        logger.error("Ill-formatted rollcall message with ID: %d.", message.mid)
        return
    if_id = payload.get("id")
    if if_id and if_id not in dishes:
        dishes[if_id] = DishController(interferometer_id=if_id)
    elif if_id in dishes:
        dishes[if_id].last_seen = time_ns()
