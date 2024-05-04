"""Constants for integration_blueprint."""
from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

NAME = "Ecodan"
DOMAIN = "ha_ecodan"
VERSION = "0.1.0"
ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"
CONF_DEVICE_ID = "device_id"