"""
ZiGate platform.

For more details about this platform, please refer to the documentation
https://home-assistant.io/components/ZiGate/
"""
from homeassistant.const import (
    ATTR_BATTERY_LEVEL, TEMP_CELSIUS, DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_TEMPERATURE)
from homeassistant.helpers.entity import Entity

DOMAIN = 'zigate'
DATA_ZIGATE_DEVICES = 'zigate_devices'
DATA_ZIGATE_ATTRS = 'zigate_attributes'

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the ZiGate sensors."""
    if discovery_info is None:
        return
    
    z = hass.data[DOMAIN]
    
    def sync_attributes(**kwargs):
        devs = []
        for device in z.devices:
            for attribute in device.attributes:
                if attribute['cluster'] == 0:
                    continue
                if 'name' in attribute:
                    key = '{}-{}-{}-{}'.format(device.addr,
                                               attribute['endpoint'],
                                               attribute['cluster'],
                                               attribute['attribute'],
                                               )
                    value = attribute.get('value')
                    if value is None:
                        continue
                    if key not in hass.data[DATA_ZIGATE_ATTRS]:
                        if not isinstance(value, bool):
                            entity = ZiGateSensor(device, attribute)
                            devs.append(entity)
                            hass.data[DATA_ZIGATE_ATTRS][key] = entity
    
        add_devices(devs)
        
    sync_attributes()
    import zigate
    zigate.dispatcher.connect(sync_attributes, zigate.ZIGATE_ATTRIBUTE_ADDED, weak=False)


class ZiGateSensor(Entity):
    """Representation of a ZiGate sensor."""

    def __init__(self, device, attribute):
        """Initialize the sensor."""
        self._device = device
        self._attribute = attribute
        self._device_class = None
        self._name = 'zigate_{}_{}'.format(device.addr,
                                           attribute.get('name'))
        self._unique_id = '{}-{}-{}-{}'.format(device.addr,
                                               attribute['endpoint'],
                                               attribute['cluster'],
                                               attribute['attribute'],
                                               )

    @property
    def unique_id(self)->str:
        return self._unique_id

    @property
    def should_poll(self):
        """No polling needed for a ZiGate sensor."""
        return False

    @property
    def device_class(self):
        """Return the device class of the sensor."""
        return self._device_class

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        a = self._device.get_attribute(self._attribute['endpoint'],
                                       self._attribute['cluster'],
                                       self._attribute['attribute'])
        return a.get('value')

    @property
    def unit_of_measurement(self):
        """Return the unit this state is expressed in."""
        return self._attribute.get('unit')

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {
            'addr': self._device.addr,
            'endpoint': self._attribute['endpoint'],
            'cluster': self._attribute['cluster'],
            'attribute': self._attribute['attribute'],
            
        }