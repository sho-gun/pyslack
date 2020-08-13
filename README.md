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
```
# Linux / Mac
export SLACK_WEBHOOK="https://hooks.slack.com/..."
```

- Run as follows.
```
pyslack YOUR_PYTHON_SCRIPT.py
```

### Appendix
Default python commands are: "python3" for Linux / Mac, and "py" for Windows.

If you want to use other commands, you can define it as environment variable PYSLACK_PYTHON.
```
# Linux / Mac
export PYSLACK_PYTHON="python"
```
