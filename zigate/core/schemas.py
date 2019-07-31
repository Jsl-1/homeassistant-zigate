import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from ..const import (
    ADDR,
    IEEE,
    ATTR_ENTITY_ID,
)

REFRESH_DEVICE_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
})

DISCOVER_DEVICE_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
})

RAW_COMMAND_SCHEMA = vol.Schema({
    vol.Required('cmd'): cv.string,
    vol.Optional('data'): cv.string,
})

IDENTIFY_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
})

REMOVE_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
})

READ_ATTRIBUTE_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
    vol.Required('endpoint'): cv.string,
    vol.Required('cluster'): cv.string,
    vol.Required('attribute_id'): cv.string,
    vol.Optional('manufacturer_code'): cv.string,
})

WRITE_ATTRIBUTE_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
    vol.Required('endpoint'): cv.string,
    vol.Required('cluster'): cv.string,
    vol.Required('attribute_id'): cv.string,
    vol.Required('attribute_type'): cv.string,
    vol.Required('value'): cv.string,
    vol.Optional('manufacturer_code'): cv.string,
})

ADD_GROUP_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
    vol.Required('endpoint'): cv.string,
    vol.Optional('group_addr'): cv.string,
})

REMOVE_GROUP_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
    vol.Required('endpoint'): cv.string,
    vol.Optional('group_addr'): cv.string,
})

GET_GROUP_MEMBERSHIP_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
    vol.Required('endpoint'): cv.string,
})

ACTION_ONOFF_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
    vol.Required('onoff'): cv.string,
    vol.Optional('endpoint'): cv.string,
    vol.Optional('on_time'): cv.string,
    vol.Optional('off_time'): cv.string,
    vol.Optional('effect'): cv.string,
    vol.Optional('gradient'): cv.string,
})

OTA_LOAD_IMAGE_SCHEMA = vol.Schema({
    vol.Required('imagepath'): cv.string,
})

OTA_IMAGE_NOTIFY_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
    vol.Optional('destination_enpoint'): cv.string,
    vol.Optional('payload_type'): cv.string,
})

VIEW_SCENE_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
    vol.Required('endpoint'): cv.string,
    vol.Required('group_addr'): cv.string,
    vol.Required('scene'): cv.string,
})

ADD_SCENE_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
    vol.Required('endpoint'): cv.string,
    vol.Required('group_addr'): cv.string,
    vol.Required('scene'): cv.string,
    vol.Required('name'): cv.string,
    vol.Optional('transition'): cv.string,
})

REMOVE_SCENE_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
    vol.Required('endpoint'): cv.string,
    vol.Required('group_addr'): cv.string,
    vol.Optional('scene'): cv.string,
})

STORE_SCENE_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
    vol.Required('endpoint'): cv.string,
    vol.Required('group_addr'): cv.string,
    vol.Required('scene'): cv.string,
})

RECALL_SCENE_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
    vol.Required('endpoint'): cv.string,
    vol.Required('group_addr'): cv.string,
    vol.Required('scene'): cv.string,
})

SCENE_MEMBERSHIP_REQUEST_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
    vol.Required('endpoint'): cv.string,
    vol.Required('group_addr'): cv.string,
})

COPY_SCENE_SCHEMA = vol.Schema({
    vol.Optional(ADDR): cv.string,
    vol.Optional(IEEE): cv.string,
    vol.Optional(ATTR_ENTITY_ID): cv.entity_id,
    vol.Required('endpoint'): cv.string,
    vol.Required('from_group_addr'): cv.string,
    vol.Required('from_scene'): cv.string,
    vol.Required('to_group_addr'): cv.string,
    vol.Required('to_scene'): cv.string,
})

BUILD_NETWORK_TABLE_SCHEMA = vol.Schema({
    vol.Optional('force'): cv.boolean,
})
