This script will get all AWS ips and parse them.

I use this script to pipe to CSF and whitelist all the ip's

python iprange.py >> /etc/csf/csf.allow; csf -r

