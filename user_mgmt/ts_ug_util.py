#!/usr/bin/env python

import argparse
from mgmt import *

"""
Copyright 2018 ThoughtSpot

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

def main():

    args = parse_args()
    print(args)

    if args.command == 'delete':
        delete_user = DelUser()
        if delete_user.valid_args(args):
            sync = SyncUserAndGroups(tsurl=args.ts_url, username=args.username, password=args.password,
                                     disable_ssl=args.disable_ssl)
            if args.users is not None:
                delete_user.delete_users(args, sync)
            if args.user_file is not None:
                delete_user.delete_users_from_file(args, sync)
            if args.groups is not None:
                delete_user.delete_groups(args, sync)
            if args.group_file is not None:
                delete_user.delete_groups_from_file(args, sync)

    elif args.command == 'get':
        # Synchronize users and groups with ThoughtSpot from a properly formatted Excel file.
        sync_excel = SyncExcel()
        if sync_excel.valid_args(args):
            uags = UGXLSReader().read_from_excel(args.filename)
            sync = SyncUserAndGroups(
                tsurl=args.ts_url,
                username=args.username,
                password=args.password,
                disable_ssl=args.disable_ssl,
            )
            sync.sync_users_and_groups(
                users_and_groups=uags, remove_deleted=args.purge
            )

    elif args.command == 'sync_excel':
        get_users = GetUsers()
        if get_users.valid_args(args):
            get_users.dump_users_and_groups(args)

    elif args.command == 'transfer_ownership':
        transfer_ownership = TransferOwnership()
        if transfer_ownership.valid_args(args):
            transfer_ownership.transfer_ownership(args)

    elif args.command == 'validate_json':
        validate_json = ValidateJson()
        validate_json.validate(args)

    else:
        print ("Invalid command argument")

def parse_args():
    """
    Parses the arguments from the command line.
    :returns: The arguments object.
    """

    # COMMON INPUTS
    parser = argparse.ArgumentParser(description="TS Comunity Utilities")
    parser.add_argument("-t", "--ts_url", help="URL to ThoughtSpot, e.g. https://myserver")
    parser.add_argument("-u", "--username", default='tsadmin', help="Name of the user to log in as.")
    parser.add_argument("-p", "--password", default='admin', help="Password for login of the user to log in as.")
    parser.add_argument("--disable_ssl", action="store_true", help="Will ignore SSL errors.", default=False)

    subparser = parser.add_subparsers(description='Sub commands', dest='command')

    # HANDLING DELETE OPS AS SEPARATE COMMANDS
    delete_ops = subparser.add_parser('delete', help='Delete user, user group')
    delete_ops.add_argument("--users", help="List of comma separated users.  Use quotes if there are spaces.")
    delete_ops.add_argument("--groups", help="List of comma separated groups.  Use quotes if there are spaces.")
    delete_ops.add_argument("--user_file",
                            help="File containing list of users to delete.  One user per line, optionally quoted.")
    delete_ops.add_argument("--group_file",
                            help="File containing list of groups to delete.  One user per line, optionally quoted.")

    # HANDLING GET OPERATIONS AS SEPARATE COMMANDS
    get_ops = subparser.add_parser('get', help='Gets User, User groups')
    get_ops.add_argument("-o", "--output_type", default="xls", help="Output type, either xls or json")
    get_ops.add_argument("-f", "--filename", default="users_and_groups",
                         help="Either the name of the json file or root of Excel file names.")

    # HANDLING SYNC FROM EXCEL OPERATIONS AS SEPARATE COMMANDS
    sync_ops = subparser.add_parser('sync_excel', help='Syncs user and groups from an excel file')
    sync_ops.add_argument("--purge", action="store_true", help="Is set, will delete users not being synced.")
    sync_ops.add_argument("-f", "--filename", help="Either the name of the Excel file name with the users and groups.")

    # HANDLING TRANSFER OWNERSHIP OPERATIONS AS SEPARATE COMMANDS
    trans_owner_ops = subparser.add_parser('transfer_ownership', help='Transfers ownership of content from one user to other')
    trans_owner_ops.add_argument("--from_user", help="Name of the user to transfer content from.")
    trans_owner_ops.add_argument("--to_user", help="Name of the user to transfer content to.")
    #does not have disable_ssl

    # HANDLING VALIDATE JSON OPERATIONS AS SEPARATE COMMANDS
    validate_ops = subparser.add_parser('validate_json', help='Syncs user and groups from an excel file')
    #validate_ops.add_argument('-v', '--validate_json', action="store_true", default=False, help='Validate JSON details flag')
    validate_ops.add_argument("-f", "--filename", help="Name of the json file to be validated.")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
