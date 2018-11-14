#
#
# add your configurations in a list format
#
#host_conf = ['sh processes cpu | exclude 0.00', 'sh memory summary | exclude 00000']

#host_conf = ['sh run | include aaa']

host_conf = ['sh run | sec line vty']
