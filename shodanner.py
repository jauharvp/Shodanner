#!/usr/bin/python3
# import shodan
import requests
import json
import pyfiglet
import argparse
from termcolor import colored

#ToolBanner

def shodanner_banner():
    shodanner_tool_banner = pyfiglet.figlet_format("Shodanner")
    scriptor = ""
    banner_space = "                      "
    print(shodanner_tool_banner)
    print(banner_space,scriptor,"\n")

#Configuration
shodanner_banner()
API_KEY = "YAFad1cTeqtWscFLAjZbqbmkw6VUPKOP"
# API_KEY = input("Enter your shodan API key: ")

def basic_func(target_ip):
    host_url = "https://api.shodan.io/shodan/host/{}?key={}".format(target_ip, API_KEY)
    host_request = requests.get(host_url) # request for the details
    if host_request.status_code==200:
        host_resp = host_request.text # response store as text
        host_json = json.loads(host_resp) # Conversion of the text to json

    else:
        print("No Results found "+str(host_request.status_code))
        print(host_request.text())

    if 'data' in host_json:
        data_desc = host_json['data'][0]

    if 'http' in data_desc:
        http_data_desc = data_desc['http']
    return host_resp, host_json, data_desc, http_data_desc


def host_server_info(target_ip):
    host_resp, host_json, data_desc, http_data_desc = basic_func(target_ip)
    print(colored("\nServer Informations",'red'))
    print(colored(" - - - - - - - - - \n",'red'))
    print("IP Address      : ", host_json['ip_str'])
    print("Operating System: ",str(host_json['os']).strip('[]'))
    if 'hostnames' in host_json:
        print("Hostnames       : ", str(host_json['hostnames']).strip('[]'))
    print("ASN             : ", str(host_json['asn']))
    print("Open Ports      : ",str(host_json['ports']).strip('[]')) # print value and strip the data
    if 'server' in http_data_desc:
        print("Server Hosted   : ",http_data_desc['server'])


def host_metadata_banner(target_ip):
    host_resp, host_json, data_desc, http_data_desc = basic_func(target_ip)
    print(colored("\nMetadata Banner ", 'red'))
    print(colored("\n - - - - - - -  -\n",'red'))
    if 'data' in data_desc:
        banner_data_desc = data_desc['data']
        print(banner_data_desc)

def host_server_vulns(target_ip):
    host_resp, host_json, data_desc, http_data_desc = basic_func(target_ip)
    print(colored("\nServer Vulnerabilities  ",'red'))
    print(colored("\n - - - - - - - - - - - -",'red'))
    space = "               "
    if 'vulns' in data_desc:
        vulns_data_desc = data_desc['vulns']
        for key in vulns_data_desc:
            print (colored("Vulnerability CVE ID : ",'yellow'),(key))
            print (colored("CVSS Score           : ",'yellow'),(vulns_data_desc[key]['cvss']))
            print (colored("Summary              :",'yellow'), (vulns_data_desc[key]['summary']),("\n\n"))

def main():
    hsi = argparse.ArgumentParser()
    hsi.add_argument("-s","--server", help="Fetch Server Information")
    hsi.add_argument("-b","--banner", help="Fetch metadata Information")
    hsi.add_argument("-v","--vulns", help="Fetch Vulnerabilities on the host")
    hsi.add_argument("-a","--all", help="Fecth all the Information")
    hsi_args = hsi.parse_args()
    if hsi_args.server:
        host_server_info(hsi_args.server)
    elif hsi_args.banner:
        host_metadata_banner(hsi_args.banner)
    elif hsi_args.vulns:
        host_server_vulns(hsi_args.vulns)
    elif hsi_args.all:
        host_server_info(hsi_args.all)
        host_metadata_banner(hsi_args.all)
        host_server_vulns(hsi_args.all)


# host_server_info()
# host_metadata_banner()
# host_server_vulns()
main()
exit()
# host_detils()

#177.130.110.209
#216.59.56.108
