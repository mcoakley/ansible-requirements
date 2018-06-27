#!/bin/bash

module_list_url=http://docs.ansible.com/ansible/latest/modules/list_of_all_modules.html

curl $module_list_url | \
grep module.html | \
grep '<a class="reference internal"' | \
awk '{ match($0, /href="(.+)#.+">/, a); print a[1]; }'
