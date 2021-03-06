# ZiGate component for Home Assistant
A new component to use the ZiGate (http://zigate.fr)

[![Build Status](https://travis-ci.org/doudz/homeassistant-zigate.svg?branch=master)](https://travis-ci.org/doudz/homeassistant-zigate)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/sebramage)

Currently it supports sensor, binary_sensor and switch, light, cover and climate

To install:
- if not exists, create folder 'custom\_components' under your home assitant directory (beside configuration.yaml)
- copy all the files in your hass folder, under 'custom\_components' like that :

```
custom_components/
└── zigate
    ├── __init__.py
    ├── services.yaml
    ├── switch.py
    ├── sensor.py
    ├── light.py
    ├── binary_sensor.py
    ├── cover.py
    └── climate.py
```
    
- adapt your configuration.yaml

To pair a new device, go in developer/services and call the 'zigate.permit\_join' service.
You have 30 seconds to pair your device.

Configuration example :

```
# Enable ZiGate (port will be auto-discovered)
zigate:

```
or

```
# Enable ZiGate
zigate:
  port: /dev/ttyUSB0
  channel: 24
  enable_led : false

```

or
if you want to use Wifi ZiGate (or usb zigate forwarded with ser2net for example)
Port is optionnal, default is 9999 

```
# Enable ZiGate Wifi
zigate:
  host: 192.168.0.10:9999

```

If you want to use PiZiGate, just add `gpio: true`. Other options are still available (channel, etc)

```
# Enable PiZiGate
zigate:
  gpio: true

```

If you're using Rpi3, you can have some trouble trying to use PiZiGate.
If needed, add the following line into config.txt (If you're using Hass.io you have to access that on the SD card directly. Simply plug it into your PC and edit it there. The config.txt is not accessible from your Hass.io system, you may need to open the SD card on a Windows or Linux system.):

```
dtoverlay=pi3-miniuart-bt
enable_uart=1
```


# Package

Additionnally you could add the zigate package to have a new tab with all zigate devices and a "permit join" switch.

To install, just copy the "packages" folder in your hass config folder and if needed add the following in your configuration.yaml

```
homeassistant:
  packages: !include_dir_named packages
```

## How enable debug log

```yaml
logger:
  default: error
  logs:
    zigate: debug
    custom_components.zigate: debug

```
Alternatively you could call the service `logger.set_level` with data `{"custom_components.zigate": "debug", "zigate": "debug"}`

## How to adjust device parameter

Some devices have the ability to change some parameters, for example on the Xiaomi vibration sensor you can adujst the sensibility. You'll be able to do that using the service `write_attribute` with parameters :
`{ "addr": "8c37", "endpoint":"1", "cluster":"0", "attribute_id":"0xFF0D", "manufacturer_code":"0x115F", "attribute_type":"0x20", "value":"0x01" }`

In this example, the value is the sensiblity, it could be 0x01 for "high sens", 0x0B for "medium" and 0x15 for "low"

## Battery level

I recommand the following package to create a nice battery tab with alerts !
[battery_alert.yaml](https://github.com/notoriousbdg/Home-AssistantConfig/blob/master/packages/battery_alert.yaml)


## custom panel

You can add a custom panel to display the network map.
To do so, copy the panels folder in your hass config folder like this :

```
panels/
└── zigate.html
```

and the following in your configuration.yaml

```yaml
panel_custom:
  - name: zigate
    sidebar_title: ZiGate
    sidebar_icon: mdi:zigbee
```
