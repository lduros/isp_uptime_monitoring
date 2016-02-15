#!/usr/bin/env python

"""
   ISP Uptime Monitoring. Checks your connection every 5 seconds. 
   Use >> at the end of script call to output to a log file.

   Copyright (C) 2016  Loic J. Duros

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software Foundation,
   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

"""
import sys
import socket
import time
import datetime
import time

template = "{TIME:^25}|{LENGTH:^20}|{ERROR:^50}"

normal_interval = 5
error_interval = 1
 
def check_connectivity(hosts=None, port=80):
    """
    Check a site/port to see if connected to the Internet. Default is
    set to Google on Port 80, but it could and probably should be
    changed to one or more sites.
    """
    if not hosts:
        hosts = ["8.8.8.8"]
    for host in hosts:
        socket.setdefaulttimeout(1)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    return True

def print_separator(size=105):
    """
    Print a separator for the table.
    """
    print "-" * size

def print_header():
    print "Monitor your ISP"
    print template.format(TIME="Failure Start", LENGTH="Length", ERROR="Error")
    print_separator()
    print template.format(TIME=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), LENGTH="Log Starting", ERROR="")    
    print_separator()

def monitor_connection():
    """
    Runs a loop to check connectivity. When it fails, it outputs the
    date and time along with the error.  After the connection is
    resumed, it provides the length of the outage and the last error
    triggered. The check is every 5 seconds when everything is working
    fine, and goes up to every second if the connection is down.
    """
    print_header()
    failure_start = None
    current_error = None
    while True:
        try:
            check_connectivity()
            if failure_start:
                failure_end = int(time.time() - failure_start)
                print template.format(TIME=datetime.datetime.fromtimestamp(failure_start).strftime("%Y-%m-%d %H:%M:%S"), LENGTH=failure_end, ERROR=current_error)
                print_separator()
                failure_start = None
        except Exception as ex:
            current_error = ex
            if not failure_start:
                failure_start = time.time()
                print template.format(TIME=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), LENGTH="started", ERROR=current_error)
        try:
            if failure_start:
                # check more often.
                time.sleep(normal_interval)
            else:
                time.sleep(error_interval)
        except KeyboardInterrupt:
            print "\nGood bye! Hope your ISP issues are resolved!"
            exit()
    
if __name__ == "__main__":
    monitor_connection()