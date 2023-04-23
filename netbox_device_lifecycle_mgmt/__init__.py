from importlib.metadata import metadata

from extras.plugins import PluginConfig

metadata = metadata('netbox_device_lifecycle_mgmt')


class NetBoxDeviceLCMConfig(PluginConfig):
    name = metadata.get('Name').replace('-', '_')
    verbose_name = 'Device Lifecycle Management'
    description = metadata.get('Description')
    version = metadata.get('Version')
    author = metadata.get('Author')
    author_email = metadata.get('Author-email')
    base_url = 'device-lcm'
    min_version = '3.5.0'
    max_version = '3.5.99'
    required_settings = []


config = NetBoxDeviceLCMConfig
