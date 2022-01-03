import logging

log = logging.getLogger(__name__)


class FMCDevices:
    def get_fmc_device_records_list(self, domain_uuid, expanded=True, offset=0, limit=999):
        log.error(f"domain_uuid: {domain_uuid}")
        log.error(f"expanded: {expanded}")
        return self.get(
            f"{self.CONFIG_PREFIX}/domain/{domain_uuid}/devices/devicerecords",
            params={"offset": offset, "limit": limit, "expanded": expanded},
        )["items"]

    def get_fmc_device_records(self, domain_uuid, object_id):
        return self.get(f"{self.CONFIG_PREFIX}/domain/{domain_uuid}/devices/devicerecords/{object_id}")

    def create_fmc_device_record(self, domain_uuid, name, host, reg_key, license_caps, **kwargs):
        nat_id = kwargs.get("nat_id")
        acp = kwargs.get("acp")
        perf_tier = kwargs.get("perf_tier")
        device_group = kwargs.get("group")
        description = kwargs.get("description")
        # "deviceGroup": device_group,
        # "description": description,
        # "natID": nat_id,
        # "performanceTier": perf_tier,

        device_data = {
            "name": name,
            "hostName": host,
            "regKey": reg_key,
            "accessPolicy": acp,
            "license_caps": license_caps,
            "accessPolicy": {"id": acp, "type": "AccessPolicy"},
            "type": "Device",
        }
        return self.post(f"{self.CONFIG_PREFIX}/domain/{domain_uuid}/devices/devicerecords", data=device_data)

    def update_fmc_device_records(self, domain_uuid, device_record):
        device_data = {
            "id": device_record["id"],
            "name": device_record["name"],
            "type": device_record["type"],
            "hostName": device_record["hostName"],
            "prohibitPacketTransfer": device_record["prohibitPacketTransfer"],
        }
        log.debug(f"Device Record Update Data: {device_data}")
        return self.put(
            f'{self.CONFIG_PREFIX}/domain/{domain_uuid}/devices/devicerecords/{device_record["id"]}',
            data=device_data,
        )

    def delete_fmc_device_records(self, domain_uuid, device_record):
        return self.delete(
            f'{self.CONFIG_PREFIX}/domain/{domain_uuid}/devices/devicerecords/{device_record["id"]}',
        )

    def get_ftd_device_physical_interfaces_list(self, domain_uuid, container_uuid, expanded=True, offset=0, limit=999):
        return self.get(
            f"{self.CONFIG_PREFIX}/domain/{domain_uuid}/devices/devicerecords/{container_uuid}/physicalinterfaces",
            params={"offset": offset, "limit": limit, "expanded": expanded},
        )["items"]

    def get_ftd_device_physical_interface(self, domain_uuid, container_uuid, intf_id):
        return self.get(
            f"{self.CONFIG_PREFIX}/domain/{domain_uuid}/devices/devicerecords/{container_uuid}/physicalinterfaces/{intf_id}",
        )

    def get_ftd_device_vlan_interface_list(self, domain_uuid, container_uuid, expanded=True, offset=0, limit=999):
        # /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/vlaninterfaces/{objectId}
        vlan_ifaces = self.get(
            f"{self.CONFIG_PREFIX}/domain/{domain_uuid}/devices/devicerecords/{container_uuid}/vlaninterfaces",
            params={"offset": offset, "limit": limit, "expanded": expanded},
        )
        return vlan_ifaces.get("items")

    def get_ftd_device_vlan_interface(self, domain_uuid, container_uuid, intf_id):
        return self.get(
            f"{self.CONFIG_PREFIX}/domain/{domain_uuid}/devices/devicerecords/{container_uuid}/vlaninterfaces/{intf_id}",
        )
