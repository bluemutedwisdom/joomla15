#!/usr/bin/python
"""Set Joomla admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively

"""

import sys
import getopt
import hashlib

from dialog_wrapper import Dialog
from mysqlconf import MySQL

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError, e:
        usage(e)

    password = ""
    email = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Joomla Password",
            "Enter new password for the Joomla 'admin' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "Joomla Email",
            "Enter email address for the Joomla 'admin' account.",
            "admin@example.com")
    
    hashpass = hashlib.md5(password).hexdigest()

    m = MySQL()
    m.execute('UPDATE joomla.jos_users SET email=\"%s\" WHERE username=\"admin\";' % email)
    m.execute('UPDATE joomla.jos_users SET password=\"%s\" WHERE username=\"admin\";' % hashpass)

if __name__ == "__main__":
    main()

