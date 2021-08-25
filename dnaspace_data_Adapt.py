import time
import requests
import json
import sys
import getopt


mytimeinterval = 30
runcount = 1

def get_key_auth_token(ip,ver,uname,pword):
    # The url for the post ticket API request
    post_url = "https://partners.dnaspaces.io/client/v1/partner/activateOnPremiseApp"
    print(post_url)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # All APIC-EM REST API query and response content type is JSON
    headers = {'content-type': 'application/json',
               'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhcHBJZCI6ImFwcC00OTA5RTY1RUYyOEE0MkQzQTQ2QzE4MEVGRjA2QjBFNiIsInZlcnNpb24iOiJ2MSIsImFjdGl2YXRpb25SZWZJZCI6IkJDMDgyOUQ1QzYxMDQzQTVCNzFCNDEzMDE1RjY3OTJFIiwiY3VzdG9tZXIiOiJFdGhhblpob3UiLCJleHBpcmVzSW4iOjE2MjI0MzI2MDE3MDcsInRlbmFudElkIjoxMDA1MSwiYmFzZVVybCI6Imh0dHBzOi8vcGFydG5lcnMuZG5hc3BhY2VzLmlvIiwicGFydG5lclRlbmFudElkIjoiNTJFM0E4QkU3Nzk4NDY1ODg0RUYxOUZEMzk4RkEyRjMiLCJpYXQiOjE2MjI0MjkwMDEsImV4cCI6MTYyMjQzMjYwMX0.JQs3h-qQ8fGQ97ERNLBiNHn-mT_7pYFzBPd3k1YGpNH3Q1gjMJYOBq8cvRipe7B3phFk7h8Ho9wcxjvgngp-_ichxrSn1hF3Vr1Ohhg-DMtoXx3dxRZK8S3A2Qej6_TEZScfxDm47RV8uUugXogV7sjaQJt0t8-sF6r3Lu2NGoM'}
    mydate = {"appId": "app-4909E65EF28A42D3A46C180EFF06B0E6", "activationRefId": "BC0829D5C61043A5B71B413015F6792E"}
    # POST request and response
    try:
        r = requests.post(post_url, data=json.dumps(mydate), headers=headers)
        # Remove '#' if need to print out response
        print("get_X_auth_token\n")
        # data = r.json()
        print(t.text)
        return

    except:
        # Something wrong, cannot get service ticket
        print("Status: %s" % r.status_code)
        print("Response: %s" % r.text)
        sys.exit()


def get_firehose_evt(ip,ver,uname,pword):
    print('get_devicelist')
    ticket = get_key_auth_token(ip,ver,uname,pword)
    #headers = {"X-Auth-Token": ticket}
    headers = {'content-type':'application/json','X-Auth-Token':ticket}
    url = "https://partners.dnaspaces.io/api/partners/v1/firehose/events"
    #print ("\nExecuting get_devicelist:\n")
    #print(url)
    params={'family':'Unified AP'}
    try:
        # The request and response of "GET" request
        requests.packages.urllib3.disable_warnings()
        resp= requests.get(url,headers=headers,params=params,verify = False)
        print ("GET '%s' Status: "%url,resp.status_code,'\n') # This is the http request status
        return(resp)
    except:
       print ("Something wrong with GET get_devicelist")
       sys.exit()


def getfirehose_evtinfo(ip,ver,uname,pword):
    dnac_device = {}
    dnac_device['time']=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    dnac_aplist=[]
    resp = get_firehose_evt(ip,ver,uname,pword)
    if (resp.status_code == 200) :
       # Get the json-encoded content from response
       response_json = resp.json()
       #print(json.dumps(response_json,indent=2))
       for siteitem in response_json['response']:
              tmp_device = {}
              tmp_device['macAddress']=siteitem['macAddress']
              tmp_device['platformId']=siteitem['platformId']
              tmp_device['reachabilityStatus']=siteitem['reachabilityStatus']
              tmp_device['hostname']=siteitem['hostname']
              tmp_resp = get_devicedetailbymacaddr(ip,ver,uname,pword,siteitem['macAddress'])
              if (tmp_resp.status_code == 200) :
                   try: 
                      tmp_resp_json = tmp_resp.json()
                      #print('tmp_device json track\n')
                      #print(json.dumps(tmp_resp_json,indent=2))
                      tmp_device['location']=tmp_resp_json['response'].get('location','')
                      tmp_device['overallHealth']=tmp_resp_json['response'].get('overallHealth','0')
                      #tmp_device['location']=tmp_resp_json['response'].['location']
                      #tmp_device['overallHealth']=tmp_resp_json['response']['overallHealth']
                   except:
                      print('tmp_device json track Error\n')
              #print(tmp_device)
              dnac_aplist.append(tmp_device)
              time.sleep(0.5)
       dnac_device['AP'] = dnac_aplist
       #print(json.dumps(dnac_device,indent=2) )
       #write to file
       millis = int(round(time.time() * 1000))
       fielname = device_Folder+'device'+str(millis)+'.json'
       #print(fielname)
       with open(fielname,"w") as f:
          json.dump(dnac_device,f)
          print("write file finish\n")
    else :
       print("get allsiteoverall error code %d" % status)



def main(argv):
  #处理 返回值options是以元组为元素的列表。
  for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('test_arg.py -u <username> -p <password> -i <ip address> -t <timeinterval> -c <runcount>')
            print('or: test_arg.py --username=<username> --password=<password> --ip <ip address> --timer <timeinterval> --count <runcount>')
            sys.exit()
        elif opt in ("-u", "--username"):
            m_USERNAME = arg
        elif opt in ("-p", "--password"):
            m_PASSWORD = arg
        elif opt in ("-i", "--ip"):
            m_APICEM_IP = arg
        elif opt in ("-t", "--timer"):
            mytimeinterval = int(arg)
        elif opt in ("-c", "--count"):
            runcount = int(arg)
  print('username:%s \n' % m_USERNAME)
  print('password:%s \n' % m_PASSWORD)
  print('IP Address:%s \n' % m_APICEM_IP)
  print('Time Inteval:%d \n' % mytimeinterval)
  print('runcount:%d \n' % runcount)
  #getdnacinfo()
  set_dnacrate(m_APICEM_IP,VERSION,m_USERNAME,m_PASSWORD)
  if (runcount == 0) :
     print('Run forever\n')
     while True:
        get_firehose_evt(m_APICEM_IP,VERSION,m_USERNAME,m_PASSWORD)
        time.sleep(1)
        getfirehose_evtinfo(m_APICEM_IP,VERSION,m_USERNAME,m_PASSWORD)
        time.sleep(mytimeinterval*60)
  else :
     while (runcount > 0) :
       get_firehose_evt(m_APICEM_IP,VERSION,m_USERNAME,m_PASSWORD)
       getfirehose_evtinfo(m_APICEM_IP,VERSION,m_USERNAME,m_PASSWORD)
       runcount = runcount -1
       if (runcount == 0):
          print('Run finish and exit\n')
          sys.exit(2)
       else:
          time.sleep(mytimeinterval*60)

if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    print(sys.argv)
    main(sys.argv[1:])
