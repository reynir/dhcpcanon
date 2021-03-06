# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:expandtab 2
# Copyright 2016, 2017 juga (juga at riseup dot net), MIT license.
"""."""
from datetime import datetime

from dhcpcanon.clientscript import ClientScript
from dhcpcanon.dhcpcap import DHCPCAP
from dhcpcanon.dhcpcaplease import DHCPCAPLease

fsm_preinit = {
    'current_state': 0,
    'request_attempts': 0,
    'discover_attempts': 0,
    'time_sent_request': None,
    'client': DHCPCAP(iface='eth0', client_mac='00:01:02:03:04:05',
                      client_ip='0.0.0.0', client_port=68, xid=900000000,
                      server_mac='ff:ff:ff:ff:ff:ff',
                      server_ip='255.255.255.255', server_port=67,
                      event=None,
                      lease=DHCPCAPLease(address='', server_id='',
                                         next_server='', router='',
                                         subnet_mask='',
                                         broadcast_address='',
                                         domain='', name_server='',
                                         subnet='', lease_time='',
                                         renewal_time='',
                                         rebinding_time='',
                                         interface='eth0',
                                         subnet_mask_cidr='',
                                         network='', expiry='',
                                         renew='', rebind=''),),
    'script': ClientScript(scriptname='/sbin/dhcpcanon-script',
                           env={'rebind': '', 'medium': '',
                                'broadcast_address': '', 'renew': '',
                                'domain_name_servers': '',
                                'dhcp_server_identifier': '',
                                'pid': '25318', 'domain_name': '',
                                'network_number': '', 'subnet_mask': '',
                                'reason': 'INIT',
                                'client': 'dhcpcanon',
                                'next_server': '', 'expiry': '',
                                'routers': '', 'interface': 'eth0',
                                'dhcp_lease_time': '', 'ip_address': '',
                                'dhcp_renewal_time': '',
                                'dhcp_rebinding_time': ''}),
    }


# client after send discover in state 1
fsm_init = {
    'current_state': 1,
    'request_attempts': 0,
    'discover_attempts': 1,
    'time_sent_request': None,
    'client': DHCPCAP(iface='eth0', client_mac='00:01:02:03:04:05',
                      client_ip='0.0.0.0', client_port=68, xid=900000000,
                      server_mac='ff:ff:ff:ff:ff:ff',
                      server_ip='255.255.255.255', server_port=67,
                      event=None,
                      lease=DHCPCAPLease(address='', server_id='',
                                         next_server='', router='',
                                         subnet_mask='',
                                         broadcast_address='',
                                         domain='', name_server='',
                                         subnet='', lease_time='',
                                         renewal_time='',
                                         rebinding_time='',
                                         interface='eth0',
                                         subnet_mask_cidr='',
                                         network='', expiry='',
                                         renew='', rebind=''),),
    'script': ClientScript(scriptname='/sbin/dhcpcanon-script',
                           env={'rebind': '', 'medium': '',
                                'broadcast_address': '', 'renew': '',
                                'domain_name_servers': '',
                                'dhcp_server_identifier': '',
                                'pid': '25318', 'domain_name': '',
                                'network_number': '', 'subnet_mask': '',
                                'reason': 'PREINIT',
                                'client': '',
                                'next_server': '', 'expiry': '',
                                'routers': '', 'interface': '',
                                'dhcp_lease_time': '', 'ip_address': '',
                                'dhcp_renewal_time': '',
                                'dhcp_rebinding_time': ''}),
    }


fsm_selecting = {
    'current_state': 2,
    'request_attempts': 0,
    'discover_attempts': 1,
    'time_sent_request': datetime(2017, 6, 23),
    'client': DHCPCAP(iface='eth0',
                      client_mac='00:01:02:03:04:05',
                      client_ip='0.0.0.0', client_port=68, xid=900000000,
                      server_mac='ff:ff:ff:ff:ff:ff',
                      server_ip='255.255.255.255', server_port=67,
                      event=None,
                      lease=DHCPCAPLease(address='192.168.1.23',
                                         server_id='192.168.1.1',
                                         next_server='192.168.1.1',
                                         router='192.168.1.1',
                                         subnet_mask='255.255.255.0',
                                         broadcast_address='192.168.1.255',
                                         domain='localdomain',
                                         name_server='192.168.1.1',
                                         subnet='192.168.1.0',
                                         lease_time='43200',
                                         renewal_time='21600',
                                         rebinding_time='37800',
                                         interface='eth0',
                                         subnet_mask_cidr='24',
                                         network='', expiry='',
                                         renew='', rebind=''),),
    'script': ClientScript(scriptname='/sbin/dhcpcanon-script',
                           env={'rebind': '', 'medium': '',
                                'broadcast_address': '',
                                'renew': '',
                                'domain_name_servers': '',
                                'dhcp_server_identifier': '',
                                'pid': '25318', 'domain_name': '',
                                'network_number': '',
                                'subnet_mask': '',
                                'reason': 'PREINIT',
                                'client': 'dhcpcanon',
                                'next_server': '', 'expiry': '',
                                'routers': '',
                                'interface': 'eth0',
                                'dhcp_lease_time': '',
                                'ip_address': '192.168.1.23',
                                'dhcp_renewal_time': '21600',
                                'dhcp_rebinding_time': '37800'}),
    }


fsm_requesting = {
    'current_state': 3,
    'request_attempts': 0,
    'discover_attempts': 1,
    'time_sent_request': datetime(2017, 6, 23),
    'client': DHCPCAP(iface='eth0', client_mac='00:01:02:03:04:05',
                      client_ip='192.168.1.23', client_port=68, xid=900000000,
                      server_mac='00:0a:0b:0c:0d:0f',
                      server_ip='192.168.1.1', server_port=67,
                      event=4,
                      lease=DHCPCAPLease(address='192.168.1.23',
                                         server_id='192.168.1.1',
                                         next_server='192.168.1.1',
                                         router='192.168.1.1',
                                         subnet_mask='255.255.255.0',
                                         broadcast_address='192.168.1.255',
                                         domain='localdomain',
                                         name_server='192.168.1.1',
                                         subnet='192.168.1.0',
                                         lease_time='43200',
                                         renewal_time='21600',
                                         rebinding_time='37800',
                                         interface='eth0',
                                         subnet_mask_cidr='24',
                                         network='',
                                         expiry='17-06-23 12:00:00',
                                         renew='17-06-23 06:00:00',
                                         rebind='17-06-23 10:30:00'),),
    'script': ClientScript(scriptname='/sbin/dhcpcanon-script',
                           env={'rebind': '', 'medium': '',
                                'broadcast_address': '',
                                'renew': '',
                                'domain_name_servers': '',
                                'dhcp_server_identifier': '',
                                'pid': '25318', 'domain_name': '',
                                'network_number': '',
                                'subnet_mask': '',
                                'reason': 'PREINIT',
                                'client': 'dhcpcanon',
                                'next_server': '',
                                'expiry': '', 'routers': '',
                                'interface': 'eth0',
                                'dhcp_lease_time': '',
                                'ip_address': '',
                                'dhcp_renewal_time': '',
                                'dhcp_rebinding_time': ''}),
    }


fsm_bound = {
    'current_state': 4,
    'request_attempts': 0,
    'discover_attempts': 1,
    'time_sent_request': datetime(2017, 6, 23),
    'client': DHCPCAP(iface='eth0', client_mac='00:01:02:03:04:05',
                      client_ip='192.168.1.23', client_port=68, xid=900000000,
                      server_mac='00:0a:0b:0c:0d:0f',
                      server_ip='192.168.1.1', server_port=67,
                      event=4,
                      lease=DHCPCAPLease(address='192.168.1.23',
                                         server_id='192.168.1.1',
                                         next_server='192.168.1.1',
                                         router='192.168.1.1',
                                         subnet_mask='255.255.255.0',
                                         broadcast_address='192.168.1.255',
                                         domain='localdomain',
                                         name_server='192.168.1.1',
                                         subnet='192.168.1.0',
                                         lease_time='43200',
                                         renewal_time='21600',
                                         rebinding_time='37800',
                                         interface='eth0',
                                         subnet_mask_cidr='24',
                                         network='',
                                         expiry='17-06-23 12:00:00',
                                         renew='17-06-23 06:00:00',
                                         rebind='17-06-23 10:30:00'),),
    'script': ClientScript(scriptname='/sbin/dhcpcanon-script',
                           env={'rebind': '17-06-23 10:30:00', 'medium': '',
                                'broadcast_address': '192.168.1.255',
                                'renew': '17-06-23 06:00:00',
                                'domain_name_servers': '192.168.1.1',
                                'dhcp_server_identifier': '192.168.1.1',
                                'pid': '25318', 'domain_name': 'localdomain',
                                'network_number': '24',
                                'subnet_mask': '255.255.255.0',
                                'reason': 'PREINIT',
                                'client': 'dhcpcanon',
                                'next_server': '192.168.1.1',
                                'expiry': '17-06-23 12:00:00',
                                'routers': '192.168.1.1',
                                'interface': 'eth0',
                                'dhcp_lease_time': '43200',
                                'ip_address': '',
                                'dhcp_renewal_time': '21600',
                                'dhcp_rebinding_time': '37800'}),
    }
# without script
###############################################################################

# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:expandtab 2
# Copyright 2016, 2017 juga (juga at riseup dot net), MIT license.
"""."""
from datetime import datetime

from dhcpcanon.clientscript import ClientScript
from dhcpcanon.dhcpcap import DHCPCAP
from dhcpcanon.dhcpcaplease import DHCPCAPLease

fsm_preinit = {
    'current_state': 0,
    'request_attempts': 0,
    'discover_attempts': 0,
    'time_sent_request': None,
    'client': DHCPCAP(iface='eth0', client_mac='00:01:02:03:04:05',
                      client_ip='0.0.0.0', client_port=68, xid=900000000,
                      server_mac='ff:ff:ff:ff:ff:ff',
                      server_ip='255.255.255.255', server_port=67,
                      event=None,
                      lease=DHCPCAPLease(address='', server_id='',
                                         next_server='', router='',
                                         subnet_mask='',
                                         broadcast_address='',
                                         domain='', name_server='',
                                         subnet='', lease_time='',
                                         renewal_time='',
                                         rebinding_time='',
                                         interface='eth0',
                                         subnet_mask_cidr='',
                                         network='', expiry='',
                                         renew='', rebind=''),),
    'script': None,
    }


# client after send discover in state 1
fsm_init = {
    'current_state': 1,
    'request_attempts': 0,
    'discover_attempts': 1,
    'time_sent_request': None,
    'client': DHCPCAP(iface='eth0', client_mac='00:01:02:03:04:05',
                      client_ip='0.0.0.0', client_port=68, xid=900000000,
                      server_mac='ff:ff:ff:ff:ff:ff',
                      server_ip='255.255.255.255', server_port=67,
                      event=None,
                      lease=DHCPCAPLease(address='', server_id='',
                                         next_server='', router='',
                                         subnet_mask='',
                                         broadcast_address='',
                                         domain='', name_server='',
                                         subnet='', lease_time='',
                                         renewal_time='',
                                         rebinding_time='',
                                         interface='eth0',
                                         subnet_mask_cidr='',
                                         network='', expiry='',
                                         renew='', rebind=''),),
    'script': None,
    }


fsm_selecting = {
    'current_state': 2,
    'request_attempts': 0,
    'discover_attempts': 1,
    'time_sent_request': datetime(2017, 6, 23),
    'client': DHCPCAP(iface='eth0',
                      client_mac='00:01:02:03:04:05',
                      client_ip='0.0.0.0', client_port=68, xid=900000000,
                      server_mac='ff:ff:ff:ff:ff:ff',
                      server_ip='255.255.255.255', server_port=67,
                      event=None,
                      lease=DHCPCAPLease(address='192.168.1.23',
                                         server_id='192.168.1.1',
                                         next_server='192.168.1.1',
                                         router='192.168.1.1',
                                         subnet_mask='255.255.255.0',
                                         broadcast_address='192.168.1.255',
                                         domain='localdomain',
                                         name_server='192.168.1.1 8.8.8.8',
                                         subnet='192.168.1.0',
                                         lease_time='43200',
                                         renewal_time='21600',
                                         rebinding_time='37800',
                                         interface='eth0',
                                         subnet_mask_cidr='24',
                                         network='', expiry='',
                                         renew='', rebind=''),),
    'script': None,
    }


fsm_requesting = {
    'current_state': 3,
    'request_attempts': 0,
    'discover_attempts': 1,
    'time_sent_request': datetime(2017, 6, 23),
    'client': DHCPCAP(iface='eth0', client_mac='00:01:02:03:04:05',
                      client_ip='192.168.1.23', client_port=68, xid=900000000,
                      server_mac='00:0a:0b:0c:0d:0f',
                      server_ip='192.168.1.1', server_port=67,
                      event=4,
                      lease=DHCPCAPLease(address='192.168.1.23',
                                         server_id='192.168.1.1',
                                         next_server='192.168.1.1',
                                         router='192.168.1.1',
                                         subnet_mask='255.255.255.0',
                                         broadcast_address='192.168.1.255',
                                         domain='localdomain',
                                         name_server='192.168.1.1 8.8.8.8',
                                         subnet='192.168.1.0',
                                         lease_time='43200',
                                         renewal_time='21600',
                                         rebinding_time='37800',
                                         interface='eth0',
                                         subnet_mask_cidr='24',
                                         network='',
                                         expiry='17-06-23 12:00:00',
                                         renew='17-06-23 06:00:00',
                                         rebind='17-06-23 10:30:00'),),
    'script': None,
    }


fsm_bound = {
    'current_state': 4,
    'request_attempts': 0,
    'discover_attempts': 1,
    'time_sent_request': datetime(2017, 6, 23),
    'client': DHCPCAP(iface='eth0', client_mac='00:01:02:03:04:05',
                      client_ip='192.168.1.23', client_port=68, xid=900000000,
                      server_mac='00:0a:0b:0c:0d:0f',
                      server_ip='192.168.1.1', server_port=67,
                      event=4,
                      lease=DHCPCAPLease(address='192.168.1.23',
                                         server_id='192.168.1.1',
                                         next_server='192.168.1.1',
                                         router='192.168.1.1',
                                         subnet_mask='255.255.255.0',
                                         broadcast_address='192.168.1.255',
                                         domain='localdomain',
                                         name_server='192.168.1.1 8.8.8.8',
                                         subnet='192.168.1.0',
                                         lease_time='43200',
                                         renewal_time='21600',
                                         rebinding_time='37800',
                                         interface='eth0',
                                         subnet_mask_cidr='24',
                                         network='',
                                         expiry='17-06-23 12:00:00',
                                         renew='17-06-23 06:00:00',
                                         rebind='17-06-23 10:30:00'),),
    'script': None,
    }
