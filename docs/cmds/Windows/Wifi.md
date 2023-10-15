## Password

```sh
pip install handi
# netsh wlan show profile | findstr All | sed "s/    All User Profile     : //" | row 1|endstr " "
export SSID=`netsh wlan show interface | findstr SSID | sed "s/    SSID                   : //"| row 1`
netsh wlan show profile name=${SSID} key=clear | findstr Key
```

## BSSID

```sh
netsh wlan show interface | findstr BSSID | sed "s/    BSSID                  : //"
```

## SSID

```sh
curl https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid=00:0C:42:1F:65:E9
```