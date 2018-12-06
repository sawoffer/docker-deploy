#!/usr/bin/env python
import os, requests, subprocess

os.system('clear')

img = requests.get('http://10.36.131.149:5000/v2/_catalog')

repos = img.json()['repositories']

for i, r in enumerate(repos, start=0):
  print "{}) {}".format(i, r)

choice = int(raw_input())
#print 'user selected {}'.format(repos[choice])
#print '{}'.format(repos[choice])

image = repos[choice]

os.system('clear')

tags = requests.get('http://10.36.131.149:5000/v2/{}/tags/list'.format(image))

tag = tags.json()['tags']

os.system('clear')

for i, r in enumerate(sorted(tag), start=0):
  print "{}) {}".format(i, r)

choice = int(raw_input())

s_tag = tag[choice]

os.system('clear')

docker = '{}:{}'.format(image, s_tag)

#menuItems = [
#    { "cm_dev" },
#    { "cm_ift" },
#    { "cm_psi" },
#    { "cm_prom" },
#]

menuItems = [
    'cm_dev',
    'cm_ift',
    'cm_psi',
    'cm_prom',
]

for i, r in enumerate(menuItems, start=0):
  print "{}) {}".format(i, r)

choice = int(raw_input())

stand =  '{}'.format(menuItems[choice])

args = '{} {}'.format(stand, docker)

subprocess.call('bash deploy.sh {}'.format(args), shell=True)
