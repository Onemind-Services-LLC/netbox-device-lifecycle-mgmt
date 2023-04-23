from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
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
)
