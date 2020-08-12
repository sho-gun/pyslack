# pyslack
Push start/end notifications of Python scripts to slack channel.

### Installation
All you need is to run following command.
```
# Linux / Mac
pip install git+https://github.com/sho-gun/pyslack

# Windows
py -m pip install git+https://github.com/sho-gun/pyslack
```

### How to Use
- Get Slack WebHook URL from https://slack.com/services/new/incoming-webhook
- Register the URL as environment variable named SLACK_WEBHOOK
- Run as follows.
```
pyslack YOUR_PYTHON_SCRIPT.py
```
