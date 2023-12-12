'''
Objectives

Install Psutil.

Create a Python script that fetches this information using Psutil:

    Time spent by normal processes executing in user mode
    Time spent by processes executing in kernel mode
    Time when system was idle
    Time spent by priority processes executing in user mode
    Time spent waiting for I/O to complete.
    Time spent for servicing hardware interrupts
    Time spent for servicing software interrupts
    Time spent by other operating systems running in a virtualized environment
    Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel

    '''

import psutil

def get_times():
    cpu_times = psutil.cpu_times()
    print("Time spent by normal processes executing in user mode:", cpu_times.user) 
    print("Time spent by processes executing in kernel mode:", cpu_times.system) 
    print("Time when system was idle:", cpu_times.idle)
    print("Time spent by priority processes executing in user mode:", cpu_times.nice) 
    print("Time spent waiting for I/O to complete:", cpu_times.iowait)
    print("Time spent for servicing hardware interrupts:", cpu_times.irq)
    print("Time spent for servicing software interrupts:", cpu_times.softirq)
    print("Time spent by other operating systems running in a virtualized environment:", cpu_times.steal)
    print("Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel:", cpu_times.guest)
