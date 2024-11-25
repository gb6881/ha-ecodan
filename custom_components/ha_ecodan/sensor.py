from dataclasses import dataclass

from homeassistant.const import UnitOfTemperature, UnitOfEnergy
from homeassistant.components.sensor import SensorEntity, SensorEntityDescription, SensorDeviceClass, SensorStateClass

from custom_components.ha_ecodan import EcodanDataUpdateCoordinator, DOMAIN
from .pyecodan.device import DeviceStateKeys
from .entity import EcodanEntity


@dataclass(kw_only=True)
class EcodanSensorEntityDescription(SensorEntityDescription):
    """A Sensor Description for Ecodan Sensors."""

    state_key: str


ENTITY_DESCRIPTIONS = (
    EcodanSensorEntityDescription(
        key="ha_ecodan",
        name="Flow Temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        state_key=DeviceStateKeys.FlowTemperature,
    ),
    EcodanSensorEntityDescription(
        key="ha_ecodan",
        name="Return Temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        state_key=DeviceStateKeys.ReturnTemperature,
    ),
    EcodanSensorEntityDescription(
        key="ha_ecodan",
        name="Flow Temperature (Zone 1)",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        state_key=DeviceStateKeys.FlowTemperatureZone1,
    ),
    EcodanSensorEntityDescription(
        key="ha_ecodan",
        name="Return Temperature (Zone 1)",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        state_key=DeviceStateKeys.ReturnTemperatureZone1,
    ),
    EcodanSensorEntityDescription(
        key="ha_ecodan",
        name="Flow Temperature (Zone 2)",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        state_key=DeviceStateKeys.FlowTemperatureZone2,
    ),
    EcodanSensorEntityDescription(
        key="ha_ecodan",
        name="Return Temperature (Zone 2)",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        state_key=DeviceStateKeys.ReturnTemperatureZone2,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Return Temperature (Boiler)",
            icon="mdi:thermometer",
            native_unit_of_measurement=UnitOfTemperature.CELSIUS,
            device_class=SensorDeviceClass.TEMPERATURE,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.ReturnTemperatureBoiler,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Tank Temperature",
            icon="mdi:thermometer",
            native_unit_of_measurement=UnitOfTemperature.CELSIUS,
            device_class=SensorDeviceClass.TEMPERATURE,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.TankWaterTemperature,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Mixing Tank Water Temperature",
            icon="mdi:thermometer",
            native_unit_of_measurement=UnitOfTemperature.CELSIUS,
            device_class=SensorDeviceClass.TEMPERATURE,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.MixingTankWaterTemperature,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Condensing Temperature",
            icon="mdi:thermometer",
            native_unit_of_measurement=UnitOfTemperature.CELSIUS,
            device_class=SensorDeviceClass.TEMPERATURE,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.CondensingTemperature,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Heat pump frequencey",
            icon="mdi:thermometer",
            device_class=SensorDeviceClass.FREQUENCY,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.HeatPumpFrequency,
    ),
    EcodanSensorEntityDescription(
        key="ha_ecodan",
        name="Outdoor Temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        state_key=DeviceStateKeys.OutdoorTemperature,
    ),
    EcodanSensorEntityDescription(
        key="ha_ecodan",
        name="Hot Water Temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        state_key=DeviceStateKeys.HotWaterTemperature,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Current Energy (consumed)",
            icon="mdi:meter-electric-outline",
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.CurrentEnergyConsumed,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Current Energy (produced)",
            icon="mdi:heat-pump",
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.CurrentEnergyProduced,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Heating Energy consumed (Zone 1)",
            icon="mdi:meter-electric-outline",
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.HeatingEnergyConsumedRate1,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Heating Energy produced (Zone 1)",
            icon="mdi:heat-pump",
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.HeatingEnergyProducedRate1,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Heating Energy consumed (Zone 2)",
            icon="mdi:meter-electric-outline",
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.HeatingEnergyConsumedRate2,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Heating Energy produced (Zone 2)",
            icon="mdi:heat-pump",
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.HeatingEnergyProducedRate2,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Hot Water Energy consumed (Zone 1)",
            icon="mdi:meter-electric-outline",
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.HotWaterEnergyConsumedRate1,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Hot Water Energy produced (Zone 1)",
            icon="mdi:heat-pump",
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.HotWaterEnergyProducedRate1,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Hot Water Energy consumed (Zone 2)",
            icon="mdi:meter-electric-outline",
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.HotWaterEnergyConsumedRate2,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Hot Water Energy produced (Zone 2)",
            icon="mdi:heat-pump",
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.HotWaterEnergyProducedRate2,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Daily Heating Energy Consumed",
            icon="mdi:meter-electric-outline",
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.DailyHeatingEnergyConsumed,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Daily Heating Energy Produced",
            icon="mdi:heat-pump",
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.DailyHeatingEnergyProduced,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Daily Hot Water Energy Consumed",
            icon="mdi:meter-electric-outline",
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.DailyHotWaterEnergyConsumed,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Daily Hot Water Energy Produced",
            icon="mdi:heat-pump",
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.DailyHotWaterEnergyProduced,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Last Legionella Activation Time",
            icon="mdi:heat-pump",
            device_class=SensorDeviceClass.DATE,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.LastLegionellaActivationTime,
    ),
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Daily Energy Consumed Date",
            icon="mdi:heat-pump",
            device_class=SensorDeviceClass.DATE,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.DailyEnergyConsumedDate,
    )
    EcodanSensorEntityDescription(
            key="ha_ecodan",
            name="Daily Energy Produced Date",
            icon="mdi:heat-pump",
            device_class=SensorDeviceClass.DATE,
            state_class=SensorStateClass.MEASUREMENT,
            state_key=DeviceStateKeys.DailyEnergyProducedDate,
    )
)


async def async_setup_entry(hass, entry, async_add_devices):
    """Set up the sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        EcodanSensor(
            coordinator=coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class EcodanSensor(EcodanEntity, SensorEntity):
    """A Sensor Entity for the Ecodan platform."""

    def __init__(self, coordinator: EcodanDataUpdateCoordinator, entity_description: EcodanSensorEntityDescription):
        """Create an Ecodan sensor."""
        super().__init__(coordinator)
        self.entity_description = entity_description
        self._attr_unique_id = f"{coordinator.device.id}_{entity_description.state_key}".lower()

    @property
    def native_value(self) -> str:
        """Return the value of the sensor."""
        return self.coordinator.data.get(self.entity_description.state_key)
