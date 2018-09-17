CIDR="192.168.177.0/24"
iptables -A INPUT -i tun+ -j ACCEPT
iptables -A INPUT -p tcp -m tcp --dport 1194 -j ACCEPT
iptables -A INPUT -p udp -m udp --dport 1194 -j ACCEPT
iptables -A FORWARD -i tun+ -j ACCEPT
iptables -A FORWARD -i tun+ -j ACCEPT
iptables -A FORWARD -d $CIDR -j ACCEPT
iptables -A FORWARD -j REJECT --reject-with icmp-host-prohibited
iptables -A OUTPUT -s $CIDR -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT
iptables -t nat -A POSTROUTING -s $CIDR -j MASQUERADE
sysctl -w "net.ipv4.ip_forward=1"
echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf

