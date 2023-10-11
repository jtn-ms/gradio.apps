```sh
pip install handi
netsh wlan show profile | findstr All | sed "s/    All User Profile     : //" | row 1|endstr " "
netsh wlan show profile name=${wifi_adapter_name} key=clear | findstr Key
```