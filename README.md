# ISP Uptime Monitoring

Author Loic J. Duros / Released under the GPLv3
  
## Overview

   ISP Uptime Monitoring is a small Python script to run from the command line with a similar purpose as the proprietary Windows "Net Uptime Monitor".
   It checks your connection without requiring root unlike the usual ICMP scripts and outputs the status regularly.  
   Use >> [filename] at the end of script call to output to a log file and let it run to gather data for your ISP support calls.
   
## Details
  It checks your connection against a host or a list of hosts (Default is Google, please change) every 5 seconds. 
  If an error occurs (any type of error), the check interval is decreased to 1 second and a row is output to inform the user
  that a failure is ongoing with the start time.
  Once the script is able to contact the host(s) again, a new row is output with the end
  datetime of the failure, as well as the duration in seconds.
  The error is there just so we can tell what exactly is going on and that it isn't a false alarm.
   
## Typical output:
    
                                           ISP Uptime Monitoring Tool                                         
    2016-02-15 13:44:18   |    Log Starting    |                                                  
    ---------------------------------------------------------------------------------------------------------
    Failure Start/End     |      Duration      |                      Error                  
    ---------------------------------------------------------------------------------------------------------
    2016-02-15 13:44:33   |      started       |        [Errno 101] Network is unreachable        
    2016-02-15 13:45:16   |         43         |        [Errno 101] Network is unreachable    
    ---------------------------------------------------------------------------------------------------------
    2016-02-15 13:45:37   |      started       |                    timed out                     
    2016-02-15 13:45:58   |         21         |           [Errno 113] No route to host         
    ---------------------------------------------------------------------------------------------------------
    C-c C-c
    Good bye! Hope your ISP issues are resolved!
