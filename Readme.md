The shodanner is host scanner based on the shodan API.                                             

                        

Usage: shodanner.py [-h] [-s SERVER] [-b BANNER] [-v VULNS] [-a ALL]

optional arguments:
    
    -h, --help            show this help message and exit

    -s SERVER, --server SERVER
                        Fetch Server Information

    -b BANNER, --banner BANNER
                        Fetch metadata Information

    -v VULNS, --vulns VULNS
                        Fetch Vulnerabilities on the host

    -a ALL, --all ALL     Fecth all the Information
    
    ```
    #python3 shodanner.py -v 192.168.0.1

Note : Make sure that your Shodan API Key has been added to the code under configuration.
```
#Configuration
shodanner_banner()
API_KEY = "<Your Shodan Key here>"
```
