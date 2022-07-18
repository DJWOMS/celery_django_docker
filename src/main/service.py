from django.core.files import File
import datetime


def send(user_email):
    f = open(f'./emails.txt', 'a')
    testfile = File(f)
    testfile.write(str(datetime.datetime.now()) + "  " + user_email + '\n')
    testfile.close()
    f.close()
