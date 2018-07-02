#!/usr/bin/python
# -*- coding: utf-8 -*-

# ======================================================
#
#    File name: unittest_ifconfig_parser
#    Author: threeheadedknight@protonmail.com
#    Date created: 30.06.2018 17:03
#    Python Version: 3.6
#
# ======================================================
import unittest

from ifconfig_parser import IfconfigParser
from tests.test_console_outputs import *


class TestIfconfigParser(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_linux_syntax_001(self):

        console_output = SAMPLE_OUTPUT_LINUX_SYNTAX_1
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 3)

        interface_list = interfaces.list_interfaces()
        self.assertIn('eth0', interface_list)
        self.assertIn('lo', interface_list)
        self.assertIn('wlan0', interface_list)

        _name = 'eth0'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Ethernet')
        self.assertEqual(interface.mac_addr, '09:00:12:90:e3:e5')
        self.assertEqual(interface.ipv4_addr, '192.168.1.29')
        self.assertEqual(interface.ipv4_bcast, '192.168.1.255')
        self.assertEqual(interface.ipv4_mask, '255.255.255.0')
        self.assertEqual(interface.ipv6_addr, 'fe80::a00:27ff:fe70:e3f5')
        self.assertEqual(interface.ipv6_mask, '64')
        self.assertEqual(interface.ipv6_scope, 'Link')
        self.assertEqual(interface.mtu, '1500')
        self.assertEqual(interface.rx_packets, '54071')
        self.assertEqual(interface.rx_errors, '1')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '48515')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

        _name = 'lo'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Local Loopback')
        self.assertEqual(interface.mac_addr, None)
        self.assertEqual(interface.ipv4_addr, '127.0.0.1')
        self.assertEqual(interface.ipv4_bcast, None)
        self.assertEqual(interface.ipv4_mask, '255.0.0.0')
        self.assertEqual(interface.ipv6_addr, '::1')
        self.assertEqual(interface.ipv6_mask, '128')
        self.assertEqual(interface.ipv6_scope, 'Host')
        self.assertEqual(interface.mtu, '16436')
        self.assertEqual(interface.rx_packets, '83')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '83')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

        _name = 'wlan0'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Ethernet')
        self.assertEqual(interface.mac_addr, '58:a2:c2:93:27:36')
        self.assertEqual(interface.ipv4_addr, '192.168.1.64')
        self.assertEqual(interface.ipv4_bcast, '192.168.2.255')
        self.assertEqual(interface.ipv4_mask, '255.255.255.0')
        self.assertEqual(interface.ipv6_addr, 'fe80::6aa3:c4ff:fe93:4746')
        self.assertEqual(interface.ipv6_mask, '64')
        self.assertEqual(interface.ipv6_scope, 'Link')
        self.assertEqual(interface.mtu, '1500')
        self.assertEqual(interface.rx_packets, '436968')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '364103')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

    def test_linux_syntax_002(self):

        console_output = SAMPLE_OUTPUT_LINUX_SYNTAX_2
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 2)

        interface_list = interfaces.list_interfaces()
        self.assertIn('lo', interface_list)
        self.assertIn('p2p1', interface_list)

        _name = 'lo'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Local Loopback')
        self.assertEqual(interface.mac_addr, None)
        self.assertEqual(interface.ipv4_addr, '127.0.0.1')
        self.assertEqual(interface.ipv4_bcast, None)
        self.assertEqual(interface.ipv4_mask, '255.0.0.0')
        self.assertEqual(interface.ipv6_addr, '::1')
        self.assertEqual(interface.ipv6_mask, '128')
        self.assertEqual(interface.ipv6_scope, 'Host')
        self.assertEqual(interface.mtu, '16436')
        self.assertEqual(interface.rx_packets, '8')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '8')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

        _name = 'p2p1'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Ethernet')
        self.assertEqual(interface.mac_addr, '00:1C:C0:AE:B5:E6')
        self.assertEqual(interface.ipv4_addr, '192.168.0.1')
        self.assertEqual(interface.ipv4_bcast, '192.168.0.255')
        self.assertEqual(interface.ipv4_mask, '255.255.255.0')
        self.assertEqual(interface.ipv6_addr, 'fe80::21c:c0ff:feae:b5e6')
        self.assertEqual(interface.ipv6_mask, '64')
        self.assertEqual(interface.ipv6_scope, 'Link')
        self.assertEqual(interface.mtu, '1500')
        self.assertEqual(interface.rx_packets, '41620')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '40231')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

    def test_linux_syntax_003(self):

        console_output = SAMPLE_OUTPUT_LINUX_SYNTAX_3
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 2)

        interface_list = interfaces.list_interfaces()
        self.assertIn('eth0', interface_list)
        self.assertIn('lo', interface_list)

        _name = 'eth0'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Ethernet')
        self.assertEqual(interface.mac_addr, '00:80:C8:F8:4A:51')
        self.assertEqual(interface.ipv4_addr, '192.168.99.35')
        self.assertEqual(interface.ipv4_bcast, '192.168.99.255')
        self.assertEqual(interface.ipv4_mask, '255.255.255.0')
        self.assertEqual(interface.ipv6_addr, None)
        self.assertEqual(interface.ipv6_mask, None)
        self.assertEqual(interface.ipv6_scope, None)
        self.assertEqual(interface.mtu, '1500')
        self.assertEqual(interface.rx_packets, '190312')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '86955')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

        _name = 'lo'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Local Loopback')
        self.assertEqual(interface.mac_addr, None)
        self.assertEqual(interface.ipv4_addr, '127.0.0.1')
        self.assertEqual(interface.ipv4_bcast, None)
        self.assertEqual(interface.ipv4_mask, '255.0.0.0')
        self.assertEqual(interface.ipv6_addr, None)
        self.assertEqual(interface.ipv6_mask, None)
        self.assertEqual(interface.ipv6_scope, None)
        self.assertEqual(interface.mtu, '16436')
        self.assertEqual(interface.rx_packets, '306')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '306')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

    def test_linux_syntax_004(self):
        console_output = SAMPLE_OUTPUT_LINUX_SYNTAX_4
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 2)

        interface_list = interfaces.list_interfaces()
        self.assertIn('eth0', interface_list)
        self.assertIn('lo', interface_list)

        _name = 'eth0'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Ethernet')
        self.assertEqual(interface.mac_addr, '00:0C:29:40:93:9C')
        self.assertEqual(interface.ipv4_addr, '192.168.154.102')
        self.assertEqual(interface.ipv4_bcast, '192.168.154.255')
        self.assertEqual(interface.ipv4_mask, '255.255.255.0')
        self.assertEqual(interface.ipv6_addr, None)
        self.assertEqual(interface.ipv6_mask, None)
        self.assertEqual(interface.ipv6_scope, None)
        self.assertEqual(interface.mtu, '1500')
        self.assertEqual(interface.rx_packets, '1771')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '359')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

        _name = 'lo'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Local Loopback')
        self.assertEqual(interface.mac_addr, None)
        self.assertEqual(interface.ipv4_addr, '127.0.0.1')
        self.assertEqual(interface.ipv4_bcast, None)
        self.assertEqual(interface.ipv4_mask, '255.0.0.0')
        self.assertEqual(interface.ipv6_addr, '::1')
        self.assertEqual(interface.ipv6_mask, '128')
        self.assertEqual(interface.ipv6_scope, 'Host')
        self.assertEqual(interface.mtu, '16436')
        self.assertEqual(interface.rx_packets, '390')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '390')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

    def test_linux_syntax_005(self):
        console_output = SAMPLE_OUTPUT_LINUX_SYNTAX_5
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 4)

        interface_list = interfaces.list_interfaces()
        self.assertIn('eth0', interface_list)
        self.assertIn('eth1', interface_list)
        self.assertIn('lo', interface_list)
        self.assertIn('virbr0', interface_list)

        _name = 'eth0'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Ethernet')
        self.assertEqual(interface.mac_addr, '00:0c:29:9b:49:bc')
        self.assertEqual(interface.ipv4_addr, '192.168.134.128')
        self.assertEqual(interface.ipv4_bcast, '192.168.134.255')
        self.assertEqual(interface.ipv4_mask, '255.255.255.0')
        self.assertEqual(interface.ipv6_addr, 'fe80::20c:29ff:fe9b:49bc')
        self.assertEqual(interface.ipv6_mask, '64')
        self.assertEqual(interface.ipv6_scope, 'Link')
        self.assertEqual(interface.mtu, '1500')
        self.assertEqual(interface.rx_packets, '11545')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '6177')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

        _name = 'eth1'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Ethernet')
        self.assertEqual(interface.mac_addr, '00:0c:29:8b:89:bc')
        self.assertEqual(interface.ipv4_addr, None)
        self.assertEqual(interface.ipv4_bcast, None)
        self.assertEqual(interface.ipv4_mask, None)
        self.assertEqual(interface.ipv6_addr, 'fe80::20c:29ff:fe9b:49bc')
        self.assertEqual(interface.ipv6_mask, '64')
        self.assertEqual(interface.ipv6_scope, 'Link')
        self.assertEqual(interface.mtu, '1500')
        self.assertEqual(interface.rx_packets, '11545')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '6177')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

        _name = 'lo'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Local Loopback')
        self.assertEqual(interface.mac_addr, None)
        self.assertEqual(interface.ipv4_addr, '127.0.0.1')
        self.assertEqual(interface.ipv4_bcast, None)
        self.assertEqual(interface.ipv4_mask, '255.0.0.0')
        self.assertEqual(interface.ipv6_addr, '::1')
        self.assertEqual(interface.ipv6_mask, '128')
        self.assertEqual(interface.ipv6_scope, 'Host')
        self.assertEqual(interface.mtu, '65536')
        self.assertEqual(interface.rx_packets, '0')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '0')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

        _name = 'virbr0'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Ethernet')
        self.assertEqual(interface.mac_addr, '3a:bf:4c:fb:90:b6')
        self.assertEqual(interface.ipv4_addr, '192.168.122.1')
        self.assertEqual(interface.ipv4_bcast, '192.168.122.255')
        self.assertEqual(interface.ipv4_mask, '255.255.255.0')
        self.assertEqual(interface.ipv6_addr, None)
        self.assertEqual(interface.ipv6_mask, None)
        self.assertEqual(interface.ipv6_scope, None)
        self.assertEqual(interface.mtu, '1500')
        self.assertEqual(interface.rx_packets, '0')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '0')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

    def test_linux_syntax_006(self):
        console_output = SAMPLE_OUTPUT_LINUX_SYNTAX_6
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 3)

        interface_list = interfaces.list_interfaces()
        self.assertIn('docker0', interface_list)
        self.assertIn('eth0', interface_list)
        self.assertIn('lo', interface_list)

        _name = 'docker0'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Ethernet')
        self.assertEqual(interface.mac_addr, '02:42:2d:66:fc:f1')
        self.assertEqual(interface.ipv4_addr, '172.17.0.1')
        self.assertEqual(interface.ipv4_bcast, '0.0.0.0')
        self.assertEqual(interface.ipv4_mask, '255.255.0.0')
        self.assertEqual(interface.ipv6_addr, 'fe80::42:2dff:fe66:fcf1')
        self.assertEqual(interface.ipv6_mask, '64')
        self.assertEqual(interface.ipv6_scope, 'Link')
        self.assertEqual(interface.mtu, '1500')
        self.assertEqual(interface.rx_packets, '2')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '3')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

        _name = 'eth0'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Ethernet')
        self.assertEqual(interface.mac_addr, '08:00:27:31:65:b5')
        self.assertEqual(interface.ipv4_addr, '10.0.2.15')
        self.assertEqual(interface.ipv4_bcast, '10.0.2.255')
        self.assertEqual(interface.ipv4_mask, '255.255.255.0')
        self.assertEqual(interface.ipv6_addr, 'fe80::3db9:eaaa:e0ae:6e09')
        self.assertEqual(interface.ipv6_mask, '64')
        self.assertEqual(interface.ipv6_scope, 'Link')
        self.assertEqual(interface.mtu, '1500')
        self.assertEqual(interface.rx_packets, '1089467')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '508121')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

        _name = 'lo'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Local Loopback')
        self.assertEqual(interface.mac_addr, None)
        self.assertEqual(interface.ipv4_addr, '127.0.0.1')
        self.assertEqual(interface.ipv4_bcast, None)
        self.assertEqual(interface.ipv4_mask, '255.0.0.0')
        self.assertEqual(interface.ipv6_addr, '::1')
        self.assertEqual(interface.ipv6_mask, '128')
        self.assertEqual(interface.ipv6_scope, 'Host')
        self.assertEqual(interface.mtu, '65536')
        self.assertEqual(interface.rx_packets, '9643')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '9643')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

    def test_linux_syntax_007(self):
        console_output = SAMPLE_OUTPUT_LINUX_SYNTAX_7
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 3)

        interface_list = interfaces.list_interfaces()
        self.assertIn('enp11s0', interface_list)
        self.assertIn('lo', interface_list)
        self.assertIn('wlp2s0b1', interface_list)

        _name = 'enp11s0'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Ethernet')
        self.assertEqual(interface.mac_addr, '78:2b:cb:ce:1d:92')
        self.assertEqual(interface.ipv4_addr, None)
        self.assertEqual(interface.ipv4_bcast, None)
        self.assertEqual(interface.ipv4_mask, None)
        self.assertEqual(interface.ipv6_addr, None)
        self.assertEqual(interface.ipv6_mask, None)
        self.assertEqual(interface.ipv6_scope, None)
        self.assertEqual(interface.mtu, '1500')
        self.assertEqual(interface.rx_packets, '0')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '0')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

        _name = 'lo'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Local Loopback')
        self.assertEqual(interface.mac_addr, None)
        self.assertEqual(interface.ipv4_addr, '127.0.0.1')
        self.assertEqual(interface.ipv4_bcast, None)
        self.assertEqual(interface.ipv4_mask, '255.0.0.0')
        self.assertEqual(interface.ipv6_addr, '::1')
        self.assertEqual(interface.ipv6_mask, '128')
        self.assertEqual(interface.ipv6_scope, 'Host')
        self.assertEqual(interface.mtu, '65536')
        self.assertEqual(interface.rx_packets, '902')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '902')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

        _name = 'wlp2s0b1'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Ethernet')
        self.assertEqual(interface.mac_addr, '68:a3:c4:2f:07:b0')
        self.assertEqual(interface.ipv4_addr, '192.168.2.11')
        self.assertEqual(interface.ipv4_bcast, '192.168.2.255')
        self.assertEqual(interface.ipv4_mask, '255.255.255.0')
        self.assertEqual(interface.ipv6_addr, 'fe80::6aa3:c4ff:fe2f:7b0')
        self.assertEqual(interface.ipv6_mask, '64')
        self.assertEqual(interface.ipv6_scope, 'Link')
        self.assertEqual(interface.mtu, '1500')
        self.assertEqual(interface.rx_packets, '3542')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '2860')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

    def test_linux_syntax_008(self):
        console_output = SAMPLE_OUTPUT_LINUX_SYNTAX_8
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 3)

        interface_list = interfaces.list_interfaces()
        self.assertIn('eth0', interface_list)
        self.assertIn('lo', interface_list)
        self.assertIn('wlan0', interface_list)

        _name = 'eth0'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Ethernet')
        self.assertEqual(interface.mac_addr, '78:2b:cb:ce:1d:92')
        self.assertEqual(interface.ipv4_addr, None)
        self.assertEqual(interface.ipv4_bcast, None)
        self.assertEqual(interface.ipv4_mask, None)
        self.assertEqual(interface.ipv6_addr, None)
        self.assertEqual(interface.ipv6_mask, None)
        self.assertEqual(interface.ipv6_scope, None)
        self.assertEqual(interface.mtu, '1500')
        self.assertEqual(interface.rx_packets, '0')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '0')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

        _name = 'lo'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Local Loopback')
        self.assertEqual(interface.mac_addr, None)
        self.assertEqual(interface.ipv4_addr, '127.0.0.1')
        self.assertEqual(interface.ipv4_bcast, None)
        self.assertEqual(interface.ipv4_mask, '255.0.0.0')
        self.assertEqual(interface.ipv6_addr, '::1')
        self.assertEqual(interface.ipv6_mask, '128')
        self.assertEqual(interface.ipv6_scope, 'Host')
        self.assertEqual(interface.mtu, '65536')
        self.assertEqual(interface.rx_packets, '382')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '382')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

        _name = 'wlan0'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Ethernet')
        self.assertEqual(interface.mac_addr, '68:a3:c4:2f:07:b0')
        self.assertEqual(interface.ipv4_addr, '192.168.2.11')
        self.assertEqual(interface.ipv4_bcast, '192.168.2.255')
        self.assertEqual(interface.ipv4_mask, '255.255.255.0')
        self.assertEqual(interface.ipv6_addr, 'fe80::6aa3:c4ff:fe2f:7b0')
        self.assertEqual(interface.ipv6_mask, '64')
        self.assertEqual(interface.ipv6_scope, 'Link')
        self.assertEqual(interface.mtu, '1500')
        self.assertEqual(interface.rx_packets, '242')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '256')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

    def test_openbsd_syntax_001(self):
        console_output = SAMPLE_OUTPUT_OPENBSD_SYNTAX_1
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 3)

        interface_list = interfaces.list_interfaces()
        self.assertIn('enp2s0', interface_list)
        self.assertIn('lo', interface_list)
        self.assertIn('virbr0', interface_list)

        _name = 'enp2s0'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Ethernet')
        self.assertEqual(interface.mac_addr, 'aa:aa:aa:aa:aa:aa')
        self.assertEqual(interface.ipv4_addr, '0.0.0.100')
        self.assertEqual(interface.ipv4_bcast, '0.0.0.0')
        self.assertEqual(interface.ipv4_mask, '255.255.255.0')
        self.assertEqual(interface.ipv6_addr, 'aaaa::aaaa:aaaa:aaaa:aaaa')
        self.assertEqual(interface.ipv6_mask, '64')
        self.assertEqual(interface.ipv6_scope, 'link')
        self.assertEqual(interface.mtu, '1500')
        self.assertEqual(interface.rx_packets, '64219')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '37986')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

        _name = 'lo'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Local Loopback')
        self.assertEqual(interface.mac_addr, None)
        self.assertEqual(interface.ipv4_addr, '127.0.0.1')
        self.assertEqual(interface.ipv4_bcast, None)
        self.assertEqual(interface.ipv4_mask, '255.0.0.0')
        self.assertEqual(interface.ipv6_addr, '::1')
        self.assertEqual(interface.ipv6_mask, '128')
        self.assertEqual(interface.ipv6_scope, 'host')
        self.assertEqual(interface.mtu, '65536')
        self.assertEqual(interface.rx_packets, '12')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '12')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

        _name = 'virbr0'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Ethernet')
        self.assertEqual(interface.mac_addr, '11:11:11:11:11:11')
        self.assertEqual(interface.ipv4_addr, '0.0.0.0')
        self.assertEqual(interface.ipv4_bcast, '0.0.0.0')
        self.assertEqual(interface.ipv4_mask, '255.255.255.0')
        self.assertEqual(interface.ipv6_addr, None)
        self.assertEqual(interface.ipv6_mask, None)
        self.assertEqual(interface.ipv6_scope, None)
        self.assertEqual(interface.mtu, '1500')
        self.assertEqual(interface.rx_packets, '0')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '0')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

    def test_openbsd_syntax_002(self):
        console_output = SAMPLE_OUTPUT_OPENBSD_SYNTAX_2
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 3)

        interface_list = interfaces.list_interfaces()
        self.assertIn('eth0', interface_list)
        self.assertIn('eth0:1', interface_list)
        self.assertIn('lo', interface_list)

        _name = 'eth0'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Ethernet')
        self.assertEqual(interface.mac_addr, 'f2:3c:91:70:98:9d')
        self.assertEqual(interface.ipv4_addr, '96.126.108.191')
        self.assertEqual(interface.ipv4_bcast, '96.126.108.255')
        self.assertEqual(interface.ipv4_mask, '255.255.255.0')
        self.assertEqual(interface.ipv6_addr, 'fe80::f03c:91ff:fe70:989d')
        self.assertEqual(interface.ipv6_mask, '64')
        self.assertEqual(interface.ipv6_scope, 'link')
        self.assertEqual(interface.mtu, '1500')
        self.assertEqual(interface.rx_packets, '8861190')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '8562901')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')

        _name = 'eth0:1'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Ethernet')
        self.assertEqual(interface.mac_addr, 'f2:3c:91:70:98:9d')
        self.assertEqual(interface.ipv4_addr, '192.168.135.145')
        self.assertEqual(interface.ipv4_bcast, '0.0.0.0')
        self.assertEqual(interface.ipv4_mask, '255.255.128.0')
        self.assertEqual(interface.ipv6_addr, None)
        self.assertEqual(interface.ipv6_mask, None)
        self.assertEqual(interface.ipv6_scope, None)
        self.assertEqual(interface.mtu, '1500')
        self.assertEqual(interface.rx_packets, None)
        self.assertEqual(interface.rx_errors, None)
        self.assertEqual(interface.rx_dropped, None)
        self.assertEqual(interface.rx_overruns, None)
        self.assertEqual(interface.rx_frame, None)
        self.assertEqual(interface.tx_packets, None)
        self.assertEqual(interface.tx_errors, None)
        self.assertEqual(interface.tx_dropped, None)
        self.assertEqual(interface.tx_overruns, None)
        self.assertEqual(interface.tx_carrier, None)
        self.assertEqual(interface.tx_collisions, None)

        _name = 'lo'
        interface = interfaces.get_interface(name=_name)
        self.assertEqual(interface.type, 'Local Loopback')
        self.assertEqual(interface.mac_addr, None)
        self.assertEqual(interface.ipv4_addr, '127.0.0.1')
        self.assertEqual(interface.ipv4_bcast, None)
        self.assertEqual(interface.ipv4_mask, '255.0.0.0')
        self.assertEqual(interface.ipv6_addr, '::1')
        self.assertEqual(interface.ipv6_mask, '128')
        self.assertEqual(interface.ipv6_scope, 'host')
        self.assertEqual(interface.mtu, '65536')
        self.assertEqual(interface.rx_packets, '2988597')
        self.assertEqual(interface.rx_errors, '0')
        self.assertEqual(interface.rx_dropped, '0')
        self.assertEqual(interface.rx_overruns, '0')
        self.assertEqual(interface.rx_frame, '0')
        self.assertEqual(interface.tx_packets, '2988597')
        self.assertEqual(interface.tx_errors, '0')
        self.assertEqual(interface.tx_dropped, '0')
        self.assertEqual(interface.tx_overruns, '0')
        self.assertEqual(interface.tx_carrier, '0')
        self.assertEqual(interface.tx_collisions, '0')


if __name__ == '__main__':
    unittest.main()
