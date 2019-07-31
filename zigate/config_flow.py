import voluptuous as vol
from homeassistant import config_entries
import homeassistant.helpers.config_validation as cv
from homeassistant.const import (CONF_PORT,
                                 CONF_HOST)
from .const import (DOMAIN,
                    CONF_ZIGATE_CHANNEL, CONF_ZIGATE_GATEWAY_ID,
                    CONF_ZIGATE_ENABLE_LED, CONF_ZIGATE_GPIO,
                    CONF_ZIGATE_POLLING)

CONFIG_FLOW_SCHEMA = vol.Schema({
    vol.Optional(CONF_PORT): cv.string,
    vol.Optional(CONF_HOST): cv.string,
    vol.Optional(CONF_ZIGATE_GATEWAY_ID): cv.string,
    vol.Optional(CONF_ZIGATE_CHANNEL): cv.positive_int,
    vol.Optional(CONF_ZIGATE_GPIO): cv.boolean,
    vol.Optional(CONF_ZIGATE_ENABLE_LED): cv.boolean,
    vol.Optional(CONF_ZIGATE_POLLING): cv.boolean,
})

@config_entries.HANDLERS.register(DOMAIN)
class ZigateFlowHandler(config_entries.ConfigFlow):
    """Handle a Zigate config flow."""

    def __init__(self):
        """Initialize the Zigate flow."""
        self.config = None

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        errors = {}
        if user_input is not None:            
        #     try:
        #         CONF_PORT: user_input[CONF_PORT],
        #         CONF_HOST: user_input[CONF_HOST],
        #         CONF_ZIGATE_GATEWAY_ID: user_input[ZIGATE_BASE_COMPONENT_ID],
        #         CONF_ZIGATE_GPIO: user_input[CONF_ZIGATE_GPIO],
        #         CONF_ZIGATE_ENABLE_LED: user_input[CONF_ZIGATE_ENABLE_LED],
        #         CONF_ZIGATE_POLLING: user_input[CONF_ZIGATE_POLLING],
        #         CONF_ZIGATE_CHANNEL: user_input[CONF_ZIGATE_CHANNEL],
        #     except:
            return self.async_abort(reason="already_configured")
            
        return self.async_show_form(
            step_id='user',
            data_schema = vol.Schema(
                {
                    vol.Optional(CONF_PORT): cv.string,
                    vol.Optional(CONF_HOST): cv.string,
                    vol.Optional(CONF_ZIGATE_GATEWAY_ID): cv.string,
                    vol.Optional(CONF_ZIGATE_CHANNEL): cv.positive_int,
                    vol.Optional(CONF_ZIGATE_GPIO): cv.boolean,
                    vol.Optional(CONF_ZIGATE_ENABLE_LED): cv.boolean,
                    vol.Optional(CONF_ZIGATE_POLLING): cv.boolean,
                }
            ),
            errors=errors,
        )
    
    async def async_step_import(self, import_info):
        """Handle a Zigate config import."""
        if self._async_current_entries():
            return self.async_abort(reason='single_instance_allowed')

        return self.async_create_entry(
            title=import_info[CONF_PORT],
            data=import_info
        )