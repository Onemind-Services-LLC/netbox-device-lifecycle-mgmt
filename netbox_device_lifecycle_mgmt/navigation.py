from django.conf import settings

from extras.plugins import PluginMenu, PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

plugin_settings = settings.PLUGINS_CONFIG.get('netbox_device_lifecycle_mgmt')

hardware_buttons = (
    PluginMenuItem(
        link='plugins:netbox_device_lifecycle_mgmt:hardwarenotice_list',
        link_text='Hardware Notices',
        permissions=['netbox_device_lifecycle_mgmt.view_hardwarenotice'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_device_lifecycle_mgmt:hardwarenotice_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['netbox_device_lifecycle_mgmt.add_hardwarenotice'],
            ),
            PluginMenuButton(
                link='plugins:netbox_device_lifecycle_mgmt:hardwarenotice_import',
                title='Import',
                icon_class='mdi mdi-upload',
                color=ButtonColorChoices.CYAN,
                permissions=['netbox_device_lifecycle_mgmt.add_hardwarenotice'],
            ),
        ),
    ),
)

software_buttons = (
    PluginMenuItem(
        link='plugins:netbox_device_lifecycle_mgmt:softwarenotice_list',
        link_text='Software Notices',
        permissions=['netbox_device_lifecycle_mgmt.view_softwarenotice'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_device_lifecycle_mgmt:softwarenotice_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['netbox_device_lifecycle_mgmt.add_softwarenotice'],
            ),
            PluginMenuButton(
                link='plugins:netbox_device_lifecycle_mgmt:softwarenotice_import',
                title='Import',
                icon_class='mdi mdi-upload',
                color=ButtonColorChoices.CYAN,
                permissions=['netbox_device_lifecycle_mgmt.add_softwarenotice'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:netbox_device_lifecycle_mgmt:softwareimage_list',
        link_text='Software Images',
        permissions=['netbox_device_lifecycle_mgmt.view_softwareimage'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_device_lifecycle_mgmt:softwareimage_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['netbox_device_lifecycle_mgmt.add_softwareimage'],
            ),
            PluginMenuButton(
                link='plugins:netbox_device_lifecycle_mgmt:softwareimage_import',
                title='Import',
                icon_class='mdi mdi-upload',
                color=ButtonColorChoices.CYAN,
                permissions=['netbox_device_lifecycle_mgmt.add_softwareimage'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:netbox_device_lifecycle_mgmt:softwareimageassociation_list',
        link_text='Software Associations',
        permissions=['netbox_device_lifecycle_mgmt.view_softwareimageassociation'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_device_lifecycle_mgmt:softwareimageassociation_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['netbox_device_lifecycle_mgmt.add_softwareimageassociation'],
            ),
            PluginMenuButton(
                link='plugins:netbox_device_lifecycle_mgmt:softwareimageassociation_import',
                title='Import',
                icon_class='mdi mdi-upload',
                color=ButtonColorChoices.CYAN,
                permissions=['netbox_device_lifecycle_mgmt.add_softwareimageassociation'],
            ),
        ),
    ),
)

contract_buttons = (
    PluginMenuItem(
        link='plugins:netbox_device_lifecycle_mgmt:serviceprovider_list',
        link_text='Service Providers',
        permissions=['netbox_device_lifecycle_mgmt.view_serviceprovider'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_device_lifecycle_mgmt:serviceprovider_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['netbox_device_lifecycle_mgmt.add_serviceprovider'],
            ),
            PluginMenuButton(
                link='plugins:netbox_device_lifecycle_mgmt:serviceprovider_import',
                title='Import',
                icon_class='mdi mdi-upload',
                color=ButtonColorChoices.CYAN,
                permissions=['netbox_device_lifecycle_mgmt.add_serviceprovider'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:netbox_device_lifecycle_mgmt:contract_list',
        link_text='Contracts',
        permissions=['netbox_device_lifecycle_mgmt.view_contract'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_device_lifecycle_mgmt:contract_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['netbox_device_lifecycle_mgmt.add_contract'],
            ),
            PluginMenuButton(
                link='plugins:netbox_device_lifecycle_mgmt:contract_import',
                title='Import',
                icon_class='mdi mdi-upload',
                color=ButtonColorChoices.CYAN,
                permissions=['netbox_device_lifecycle_mgmt.add_contract'],
            ),
        ),
    ),
)

if plugin_settings.get('top_level_menu', False):
    menu = PluginMenu(
        label='Device Lifecycle',
        icon_class='mdi mdi-devices',
        groups=(
            ('Hardware', hardware_buttons),
            ('Software', software_buttons),
            ('Contracts', contract_buttons),
        ),
    )
else:
    menu_items = hardware_buttons + software_buttons + contract_buttons
