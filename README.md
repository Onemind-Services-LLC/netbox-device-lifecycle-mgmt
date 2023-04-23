# Device Lifecycle Management

A plugin for [NetBox](https://github.com/netbox-community/netbox) that provides a way to track the lifecycle of devices.
You can manage devices, device types, inventory items, module types and even software running on devices.

## Installation

* Install NetBox as per NetBox documentation
* Add to local_requirements.txt:
  * `git+https://github.com/Onemind-Services-LLC/netbox-device-lifecycle-mgmt@dev`
* Install requirements: `./venv/bin/pip install -r local_requirements.txt`
* Add to PLUGINS in NetBox configuration:
  * `'netbox_device_lifecycle_mgmt',`
* Run migration: `./venv/bin/python netbox/manage.py migrate`

## Configuration

None
