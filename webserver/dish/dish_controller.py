"""Local dish controller management."""
from datetime import datetime
from typing import Dict

from paho.mqtt.client import Client

dishes: Dict[str, "DishController"] = {}

DEFAULT_QOS: int = 2


class DishController:
    """Abstracts a single dish controller."""

    def __init__(self, interferometer_id: str, client: Client):
        """Initialize DishController instance."""
        self._interferometer_id = interferometer_id
        self._client = client
        self._last_seen = datetime.now()
        self._target_az = 0.0
        self._target_el = 90.0
        self._el = 90.0
        self._az = 0.0

    @property
    def interferometer_id(self) -> str:
        """Getter for interferometer_id"""
        return self._interferometer_id

    @property
    def target_elevation(self) -> float:
        """Getter for target_elevation"""
        return self._target_el

    @property
    def target_azimuth(self) -> float:
        """Getter for target_azimuth"""
        return self._target_az

    @property
    def elevation(self) -> float:
        """Getter for target_elevation"""
        return self._el

    @property
    def azimuth(self) -> float:
        """Getter for target_azimuth"""
        return self._az

    def publish_elevation(self, elevation: float) -> None:
        """Publishes a message to the elevation topic."""
        self._target_el = elevation
        self._client.publish(
            topic=f"cmd/if_{self._interferometer_id}/el",
            payload=elevation,
            qos=DEFAULT_QOS,
        )

    def publish_azimuth(self, azimuth: float) -> None:
        """Publishes a message to the azimuth topic."""
        self._target_az = azimuth
        self._client.publish(
            topic=f"cmd/if_{self._interferometer_id}/az",
            payload=azimuth,
            qos=DEFAULT_QOS,
        )
