# ISP Uptime Monitoring

Author Loic J. Duros / Released under the GPLv3
  
## Overview

   ISP Uptime Monitoring is a small Python script to run from the command line.
   It checks your connection without requiring root unlike the usual ICMP scripts and outputs the status regularly.  
   Use >> at the end of script call to output to a log file and let it run to gather data for your ISP support calls.
   
## Details
  It checks your connection against a host or a list of hosts (Default is Google, please change) every 5 seconds. 
  If an error occurs (any type of error), the check interval is decreased to 1 second and a row is output to inform the user
  that a failure is ongoing. Once the script is able to contact the host(s) again, a new row is output with the start
  datetime of the failure, as well as the duration in seconds.
  The error is there just so we can tell what exactly is going on and that it isn't a false alarm.
   
## Typical output:
    
                                          ISP Uptime Monitoring Tool                                        

          Failure Start      |      Duration      |                      Error                       
     ---------------------------------------------------------------------------------------------------------
       2016-02-15 12:36:33   |    Log Starting    |                                                  
     ---------------------------------------------------------------------------------------------------------
       2016-02-15 12:36:43   |       ongoing      |           [Errno 113] No route to host           
       2016-02-15 12:36:43   |         11         |           [Errno 113] No route to host           
     ---------------------------------------------------------------------------------------------------------
       2016-02-15 12:37:29   |       ongoing      |        [Errno 101] Network is unreachable        
       2016-02-15 12:37:29   |         16         |        [Errno 101] Network is unreachable        
     ---------------------------------------------------------------------------------------------------------
      C-c C-c
      Good bye! Hope your ISP issues are resolved!
