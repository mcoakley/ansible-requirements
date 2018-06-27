#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib2
import sys

ansible_version = 'latest'
base_url = 'http://docs.ansible.com/ansible/' + ansible_version + '/modules/'
url = 'list_of_all_modules.html'

page = urllib2.urlopen(base_url + url)
soup = BeautifulSoup(page, 'lxml')

for aItem in soup.find_all('a', href=True, class_='reference internal'):
  if '_module.html' in aItem['href']:
    module_url = aItem['href'].split('#')[0]

    module_page = urllib2.urlopen(base_url + module_url)
    module_soup = BeautifulSoup(module_page, 'lxml')

    for divItem in module_soup.find_all('div'):
      if 'id' in divItem.attrs and divItem['id'] == 'requirements':
        for liItem in divItem.find_all('li'):
          if liItem.string is not None:
            print liItem.string.encode('utf-8')
