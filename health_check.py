#!/usr/bin/env python3
'''Script to run in background monitoring system statistics: CPU usage, disk
space, available memory, and name resolution.
Sends email if there are problems, such as:
    - Report error if CPU usage is over 80%
    - Report error if available disk space is lower than 20%
    - Report error if available memory is less than 500MB
    - Report error if the hostname 'localhost' cannot be resolved to
      '127.0.0.1'
'''
import shutil, psutil, os, socket, emails

def check_cpu_constrained():
    '''Returns True if the cpu is having too much usage, False otherwise.'''
    return psutil.cpu_percent(1) > 80

def check_disk_full(disk='/', min_percent=20):
    '''Returns True if there isn't enough disk space, False otherwise.'''
    du = shutil.disk_usage(disk)

    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total

    if percent_free < min_percent:
        return True
    return False

def check_memory_full():
    '''Returns True if there isn't enough memory, False otherwise.'''
    mem = psutil.virtual_memory()

    min_mem = 500 * 1024 * 1024 # 500MB

    return mem.available < min_mem

def check_no_network():
    '''Returns True if localhost fails to resolve 127.0.0.1, False
    otherwise.'''
    try:
        socket.gethostbyname('localhost')
        return False
    except:
        return True

def email_error(subject):
    '''Generates and sends email with the subject line describing an issue that
    was detected.'''
    sender = 'automation@example.com'
    receiver = '<username>@example.com'
    body = '''Please check your system and resolve the issue as soon as
    possible.'''
    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)

def main():
    #TODO: Call functions every 60 seconds
    checks = [
            (check_cpu_constrained(),
                'Error - CPU usage is over 80%'),
            (check_disk_full(),
                'Error - Available disk space is less than 20%'),
            (check_memory_full(),
                'Error - Available memory is less than 500MB'),
            (check_no_network(),
                'Error - localhost cannot be resolved to 127.0.0.1')
            ]

    everything_ok = True

    # Call all functions in list and send email for each issue detected
    for check, msg in checks:
        if check():
            print(msg)
            email_error(msg)
            everything_ok = False

    if not everything_ok:
        sys.exit(1)

    print('Everything ok.')
    sys.exit(0)

if __name__ == '__main__':
    main()
