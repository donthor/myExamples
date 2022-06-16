from multiprocessing import Value
from tabulate import tabulate
from pkg_resources import parse_version
from genie.testbed import load
from genie.utils import Dq
from contextlib import redirect_stdout
switch_info = []
final_switch_info = []
report = []
tb = load('iosxe_testbed.yaml')
# print(tb)
dev = tb.devices['csr1000v-1']
dev.connect()
p1 = dev.parse('show version')
report.append(p1['version']['hostname'])
p2 = dev.parse('show ip interface brief')
# print(p1)
interfaces = p2['interface']
print(interfaces)
print()
for item in interfaces:
    # print(item)
    switch_info.append(item)
    for each in interfaces[item]:
        # print(each)
        # print(interfaces[item][each])
        if each == 'ip_address':
            switch_info.append(interfaces[item][each])
        if each == 'protocol':
            switch_info.append(interfaces[item][each])
    final_switch_info.append(switch_info)
    switch_info = []
print(final_switch_info)
print()
print(p1['version']['hostname'])
print(tabulate(final_switch_info, headers=['Interface', 'IP Address', 'Protocol'], tablefmt='grid'))