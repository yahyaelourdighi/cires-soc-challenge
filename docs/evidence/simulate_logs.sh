#!/bin/bash
sudo logger -t sshd "Jan 14 12:30:12 server sshd[1830]: Failed password for invalid user test1 from 203.0.113.5 port 50234 ssh2"
sleep 1
sudo logger -t sshd "Jan 14 12:30:14 server sshd[1830]: Failed password for invalid user test1 from 203.0.113.5 port 50234 ssh2"
sleep 1
sudo logger -t sshd "Jan 14 12:30:16 server sshd[1830]: Failed password for invalid user test1 from 203.0.113.5 port 50234 ssh2"
sleep 1
sudo logger -t sshd "Jan 14 12:30:20 server sshd[1830]: Accepted password for backupuser from 203.0.113.5 port 50234 ssh2"
