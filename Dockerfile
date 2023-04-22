ARG NETBOX_VARIANT=v3.4

FROM netboxcommunity/netbox:${NETBOX_VARIANT}

RUN mkdir -pv /plugins/netbox-device-lifecycle-mgmt
COPY . /plugins/netbox-device-lifecycle-mgmt

RUN /opt/netbox/venv/bin/python3 /plugins/netbox-device-lifecycle-mgmt/setup.py develop
RUN cp -rf /plugins/netbox-device-lifecycle-mgmt/netbox_device_lifecycle_mgmt/ /opt/netbox/venv/lib/python3.10/site-packages/netbox_device_lifecycle_mgmt
