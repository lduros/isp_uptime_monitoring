#!/usr/bin/env python

"""
   ISP Uptime Monitoring. A small script to check your connection
   every 5 seconds.  Use >> at the end of script call to output to a
   log file.

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
import socket
import time
import datetime

template = "{TIME:^25}|{LENGTH:^20}|{ERROR:^50}"

normal_interval = 5  # seconds between which connection is checked.
error_interval = 1   # seconds between which connection is checked in case of issue.


def check_connectivity(hosts=None, port=80):
    """
    Check a site/port to see if connected to the Internet. Default is
    set to Google on Port 80, but it could and probably should be
    changed to one or more sites. Please change IP from Google to
    another resource or set of resources.
    """
    if not hosts:
        hosts = ["google.com"]
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
    """
    Prints header when script execution starts.
    """
    print "\n\n"
    print "{0:^105}".format("ISP Uptime Monitoring Tool")
    print "\n\n"
    print template.format(TIME=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), LENGTH="Log Starting", ERROR="")    
    print_separator()
    print template.format(TIME="Failure Start/End", LENGTH="Duration", ERROR="Error")
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
                failure_length = int(time.time() - failure_start)
                failure_end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print template.format(TIME=failure_end,
                                      LENGTH=failure_length,
                                      ERROR=current_error)
                print_separator()
                failure_start = None
        except Exception as ex:
            current_error = ex
            if not failure_start:
                failure_start = time.time()
                print template.format(TIME=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                      LENGTH="started",
                                      ERROR=current_error)
        try:
            # check more often if there's already an issue.
            if failure_start:
                time.sleep(error_interval)
            else:
                time.sleep(normal_interval)
        except KeyboardInterrupt:
            print "\nGood bye! Hope your ISP issues are resolved!"
            exit()


if __name__ == "__main__":
    monitor_connection()
