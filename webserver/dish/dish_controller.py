"""Local dish controller management."""
from datetime import datetime

from webserver import mqtt

from enum import Enum


class DishControllerMode(Enum):
    TRACKING = "tracking"
    FIXED = "fixed"


class DishController:
    """Abstracts a single dish controller."""

    def __init__(self, interferometer_id: str):
        """Initialize DishController instance."""
        self._interferometer_id = interferometer_id
        self._last_seen = datetime.now()
        self._el_cmd_topic = f"cmd/if_{interferometer_id}/el"
        self._az_cmd_topic = f"cmd/if_{interferometer_id}/az"
        self._mode_cmd_topic = f"cmd/if_{interferometer_id}/mode"
        self._el_tlm_topic = f"sensor/if_{interferometer_id}/el"
        self._az_tlm_topic = f"sensor/if_{interferometer_id}/az"
        self._mode = DishControllerMode.FIXED
        self._target_az = 0.0
        self._target_el = 90.0
        self._el = 90.0
        self._az = 0.0

        # 2 is the highest quality of service in MQTT (broker will do its utmost to deliver the message)
        self._qos = 2

    @property
    def interferometer_id(self) -> str:
        """Getter for interferometer_id"""
        return self._interferometer_id

    @property
    def target_elevation(self) -> str:
        """Getter for target_elevation"""
        return self._target_el

    @property
    def target_azimuth(self) -> str:
        """Getter for target_azimuth"""
        return self._target_az

    @property
    def elevation(self) -> str:
        """Getter for target_elevation"""
        return self._el

    @property
    def azimuth(self) -> str:
        """Getter for target_azimuth"""
        return self._az

    def publish_elevation(self, elevation: float) -> None:
        """Publishes a message to the elevation topic."""
        self._target_el = elevation
        mqtt.publish(topic=self._el_cmd_topic, payload=elevation, qos=self._qos)

    def publish_azimuth(self, azimuth: float) -> None:
        """Publishes a message to the azimuth topic."""
        self._target_az = azimuth
        mqtt.publish(topic=self._az_cmd_topic, payload=azimuth, qos=self._qos)

    def publish_mode(self, mode: DishControllerMode) -> None:
        """Publishes a message to the mode topic."""
        self._mode = mode
        mqtt.publish(topic=self._mode_cmd_topic, payload=mode.value, qos=self._qos)
