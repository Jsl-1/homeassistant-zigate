import datetime
from homeassistant.components.group import \
    ENTITY_ID_FORMAT as GROUP_ENTITY_ID_FORMAT

from homeassistant.const import (CONF_HOST, CONF_PORT)

DOMAIN = 'zigate'
DATA_ZIGATE = 'zigate'
DATA_ZIGATE_GATEWAYS = 'zigate_gateways'
DATA_ZIGATE_COMPONENTS = 'zigate_components'
DATA_ZIGATE_DEVICES = 'zigate_devices'
DATA_ZIGATE_ATTRS = 'zigate_attributes'
DATA_ZIGATE_CONFIG = 'zigate_config'

# SUPPORTED_PLATFORMS = ('sensor',
#                        'binary_sensor')
#                        'switch',
#                        'light',
#                        'cover',
#                        'climate')
SUPPORTED_PLATFORMS = ('sensor',)

CONF_ZIGATE_GATEWAY_ID = 'gateway_id'
CONF_ZIGATE_CHANNEL= 'channel'
CONF_ZIGATE_GPIO = 'gpio'
CONF_ZIGATE_ENABLE_LED = 'enable_led'
CONF_ZIGATE_POLLING = 'polling'

ZIGATE_BASE_COMPONENT_ID = 'zigate'

ADDR = 'addr'
IEEE = 'ieee'

SCAN_INTERVAL = datetime.timedelta(seconds=60)
GROUP_NAME_ALL_ZIGATE = 'all zigate'
ENTITY_ID_ALL_ZIGATE = GROUP_ENTITY_ID_FORMAT.format('all_zigate')



