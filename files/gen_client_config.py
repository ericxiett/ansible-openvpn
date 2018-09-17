import sys

KEYS_PATH = '/etc/openvpn/easy-rsa/keys/'
CLIENTS_PATH = '/home/openvpn_clients/'

def main():

    if len(sys.argv) < 2:
        print("Should input client user")
        exit(1)

    user = sys.argv[1]
    conf_file = CLIENTS_PATH + user + '_114.118.24.246.ovpn'
    with open(KEYS_PATH+'ca.crt', 'r') as f:
        with open(conf_file, 'a+') as fconf:
            fconf.write('<ca>\n')
            for line in f.readlines():
                fconf.write(line)
            fconf.write('</ca>\n')

    index = 0
    start = 0
    with open(KEYS_PATH+user+'.crt', 'r') as f:
        with open(conf_file, 'a+') as fconf:
            fconf.write('\n')
            fconf.write('<cert>\n')
            lines = []
            for line in f.readlines():
                lines.append(line)
                if 'BEGIN CERTIFICATE' in line:
                    start = index
                index += 1

            for li in lines[start:]:
                fconf.write(li)
            fconf.write('</cert>\n')

    with open(KEYS_PATH+user+'.key', 'r') as f:
        with open(conf_file, 'a+') as fconf:
            fconf.write('\n')
            fconf.write('<key>\n')
            for line in f.readlines():
                fconf.write(line)
            fconf.write('</key>\n')
            fconf.write('\n')


if __name__ == '__main__':
    sys.exit(main())
