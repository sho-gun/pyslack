import os
import platform
import sys
import subprocess
import slackweb

def makeStr(list):
    str = ''
    for s in list:
        str += s + ' '
    return str

def main():
    url = os.environ.get('SLACK_WEBHOOK')
    if url is None:
        print('Environment Variable "SLACK_WEBHOOK" does not exists.')
        exit(1)

    if len(sys.argv) > 1:
        args = ['python3'] + sys.argv[1:]
        if platform.system() == 'Windows':
            args[0] = 'py'

        slack = slackweb.Slack(url=url)
        slack.notify(text='START: ' + makeStr(args))

        completed_process = subprocess.run(args)

        if completed_process.returncode == 0:
            slack.notify(text='FINISH: ' + makeStr(args))
        else:
            slack.notify(text='STOP: ' + makeStr(args))

if __name__ == '__main__':
    main()
