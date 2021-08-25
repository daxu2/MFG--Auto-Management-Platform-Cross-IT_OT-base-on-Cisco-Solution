# MFG--Auto-Management-Platform-Cross-IT_OT-base-on-Cisco-Solution
   First of all, IT/OT is more closed and seamless integration. customers want to have single plane to manage IT/OT device.broken the border between IT and OT

   Secondly, Secure is highest priority for all customer. what can we provide an secure and innovation solution to help customer to create secure workspace and factory,who will win the customer

   Thirdly, we proive proactive  IT/OT operations, provide auto dedect,auto monitor, and more innovative services, integrate within company workflow and customer private apps.
   
  Other things you might include:

    Technology stack: This Example Code is composed with 3 moduel,data visibility by splunk can not be upload on github,so this demo code only include data collect engine module.   
    1.Cyber vision data-adapt.py :--- TThis is a Saple code using Python,this code is get data from cyber vision and can be display on Splunk and kibana,you can using follow command to run the code python3 Cyber vision data-adapt.py -token ics-e8fbcfb8cd54c6d70fba097b208f5115d5957c99-dbdd29d584c19dd2a37c8e71ee72a8310f74a586 -i 172.16.63.248 -t 1 -c 1, -token is cyber vison token ,'172.16.63.248' is cyber vison IP address, -t is mean how many minute to get data from dnac once,'-c' is mean how many time you want to retrieve data from cyber vison,if =0 mean,this will run for ever.
    2.dnac_data-adapt.py :--- This is a Saple code using Python,this code is get data from DNAC and can be display on Splunk,you can using follow command to run the code python3 dnac_data-adapt.py -u admin -p Cisc0123 -i 172.16.63.248 -t 1 -c 1, 'admin is DNAC username,'Cisc0123' is DNAC password,'172.16.63.248' is DNAC IP address, -t is mean how many minute to get data from dnac once,'-c' is mean how many time you want to retrieve data from DNAC,if =0 mean,this will run for ever.
    3.dnaspace_data-adapt.py :--- This is a Saple code using Python,this code is get data from DNA Space and can be display on Splunk and kibana,you can using follow command to run the code python3 dnaspace_data-adapt.py -token eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhcHBJZCI6ImFwcC00OTA5RTY1RUYyOEE -t 1 -c 1, -token is dna space token,-appid is you new appkication id create on dna space  -t is mean how many minute to get data from dnac once,'-c' is mean how many time you want to retrieve data from DNAC,if =0 mean,this will run for ever.
![Data Collector Engine develop by Pythone](https://github.com/daxu2/MFG--Auto-Management-Platform-Cross-IT_OT-base-on-Cisco-Solution/blob/main/images/develop-python.jpg)
![Data Visibility develop by spunk](https://github.com/daxu2/MFG--Auto-Management-Platform-Cross-IT_OT-base-on-Cisco-Solution/blob/main/images/develop-splunk.jpg)   
 
    
![image](https://user-images.githubusercontent.com/31427568/130733277-aac9ed31-867f-424f-ad3f-11dc9ca7a5bb.png)
