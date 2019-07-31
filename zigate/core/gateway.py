"""
ZiGate gateway.
"""
import logging
import os


from ..const import (CONF_HOST, CONF_PORT,
                     CONF_ZIGATE_CHANNEL, CONF_ZIGATE_GPIO,
                     CONF_ZIGATE_ENABLE_LED,CONF_ZIGATE_POLLING,
                     CONF_ZIGATE_GATEWAY_ID)

_LOGGER = logging.getLogger(__name__)

class ZigateGateway():
    """Represent a Zigate Gateway"""
    def __init__(self, hass, config_entry):
        port = config_entry.data[CONF_PORT]
        host = config_entry.data[CONF_HOST]
        gpio = config_entry.data[CONF_ZIGATE_GPIO]
        enable_led = config_entry.data[CONF_ZIGATE_ENABLE_LED]
        polling = config_entry.data[CONF_ZIGATE_POLLING]
        channel = config_entry.data[CONF_ZIGATE_CHANNEL]
        zigate_gateway_id = config_entry.data[CONF_ZIGATE_GATEWAY_ID]

        persistent_file = os.path.join(hass.config.config_dir,
                                    '{}.json'.format(zigate_gateway_id))

        import zigate
        self._zigate = zigate.connect(port=port, host=host,
                                        path=persistent_file,
                                        auto_start=False,
                                        gpio=gpio)

        _LOGGER.debug('ZiGate object created %s', zigate)
        

    @property
    def zigate(self):
        return self._zigate

    @property
    def model(self):
        import zigate
        if (self._zigate.__class__.__name__ == "ZigateWifi"):
            return "Zigate Wifi"
        if (self._zigate.__class__.__name__ == "ZiGateGPIO"):
            return "Zigate GPIO"        
        return "Zigate Usb"

