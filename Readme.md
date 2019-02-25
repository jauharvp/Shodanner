The shodanner is host scanner based on the shodan API.

Usage: 

 ____  _               _                             

/ ___|| |__   ___   __| | __ _ _ __  _ __   ___ _ __ 

\___ \| '_ \ / _ \ / _` |/ _` | '_ \| '_ \ / _ \ '__|

 ___) | | | | (_) | (_| | (_| | | | | | | |  __/ |   

|____/|_| |_|\___/ \__,_|\__,_|_| |_|_| |_|\___|_|   

                                                     

                        

usage: shodanner.py [-h] [-s SERVER] [-b BANNER] [-v VULNS] [-a ALL]

optional arguments:
  -h, --help            show this help message and exit

  -s SERVER, --server SERVER
                        Fetch Server Information

  -b BANNER, --banner BANNER
                        Fetch metadata Information

  -v VULNS, --vulns VULNS
                        Fetch Vulnerabilities on the host

  -a ALL, --all ALL     Fecth all the Information
