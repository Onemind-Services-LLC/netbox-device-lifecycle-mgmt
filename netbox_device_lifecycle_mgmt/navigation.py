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
        ),
    ),
)
