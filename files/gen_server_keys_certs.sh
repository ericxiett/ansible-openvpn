#!/usr/bin/env bash

set -x

cd /etc/openvpn/easy-rsa

source ./vars

./clean-all

./build-ca <<EOF
CN
SD
JN
Inspur
cloud
inspur
server
inspur@inspur.com
EOF

./build-key-server --batch server

./build-dh

cd /etc/openvpn/easy-rsa/keys
cp dh2048.pem ca.crt server.crt server.key /etc/openvpn

