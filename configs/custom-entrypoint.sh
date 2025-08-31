#!/bin/bash
for script in /var/run/s6/etc/cont-init.d/*; do
    if [[ "$script" != "/var/run/s6/etc/cont-init.d/1-config-filebeat" ]]; then
        bash "$script"
    fi
done
exec /init
