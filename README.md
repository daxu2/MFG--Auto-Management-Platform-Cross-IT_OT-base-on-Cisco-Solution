# MFG--Auto-Management-Platform-Cross-IT_OT-base-on-Cisco-Solution
   First of all, IT/OT is more closed and seamless integration. customers want to have single plane to manage IT/OT device.broken the border between IT and OT

   Secondly, Secure is highest priority for all customer. what can we provide an secure and innovation solution to help customer to create secure workspace and factory,who will win the customer

   Thirdly, we proive proactive  IT/OT operations, provide auto dedect,auto monitor, and more innovative services, integrate within company workflow and customer private apps.
   
  Other things you might include:
    Technology stack: sample Code is composed with 3 modules.This code is used to get data from cyber vision & dna space & dnac server and helps to display on Splunk and kibana dashboards the telemetry data.
    
   1.Cyber vision data-adapt.py : This is a Sample code using Python,This code is used to get data from cyber vision and helps to display on Splunk and kibana dashboards the telemetry data,you can using follow command to run the code python3 Cyber vision data-adapt.py -token ics-e8fbcfb8cd54c6d70fba097b208f5115d5957c99-dbdd29d584c19dd2a37c8e71ee72a8310f74a586 -i 172.16.63.248 -t 1 -c 1, -token is cyber vison token ,'172.16.63.248' is cyber vison IP address, -t is mean how many minute to get data from dnac once,'-c' is mean how many time you want to retrieve data from cyber vison,if =0 mean,this will run for ever.
    
   2.dnac_data-adapt.py : This is a Sample code using Python,This code is used to get data from dnac server and helps to display on Splunk and kibana dashboards the telemetry data,you can using follow command to run the code python3 dnac_data-adapt.py -u admin -p Cisc0123 -i 172.16.63.248 -t 1 -c 1, 'admin is DNAC username,'Cisc0123' is DNAC password,'172.16.63.248' is DNAC IP address, -t is mean how many minute to get data from dnac once,'-c' is mean how many time you want to retrieve data from DNAC,if =0 mean,this will run for ever. 
    
   3.dnaspace_data-adapt.py: This is a Sample code using Python,This code is used to get data from dna space and helps to display on Splunk and kibana dashboards the telemetry data,you can using follow command to run the code python3 dnaspace_data-adapt.py -token eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhcHBJZCI6ImFwcC00OTA5RTY1RUYyOEE0MkQzQTQ2QzE4MEVGRjA2QjBFNiIsInZlcnNpb24iOiJ2MSIsImFjdGl2YXRpb25SZWZJZCI6IkJDMDgyOUQ1QzYxMDQzQTVCNzFCNDEzMDE1RjY3OTJFIiwiY3VzdG9tZXIiOiJFdGhhblpob3UiLCJleHBpcmVzSW4iOjE2MjI0MzI2MDE3MDcsInRlbmFudElkIjoxMDA1MSwiYmFzZVVybCI6Imh0dHBzOi8vcGFydG5lcnMuZG5hc3BhY2VzLmlvIiwicGFydG5lclRlbmFudElkIjoiNTJFM0E4QkU3Nzk4NDY1ODg0RUYxOUZEMzk4RkEyRjMiLCJpYXQiOjE2MjI0MjkwMDEsImV4cCI6MTYyMjQzMjYwMX0.JQs3h-qQ8fGQ97ERNLBiNHn-mT_7pYFzBPd3k1YGpNH3Q1gjMJYOBq8cvRipe7B3phFk7h8Ho9wcxjvgngp-_ichxrSn1hF3Vr1Ohhg-DMtoXx3dxRZK8S3A2Qej6_TEZScfxDm47RV8uUugXogV7sjaQJt0t8-sF6r3Lu2NGoM -appid app-4909E65EF28A42D3A46C180EFF06B0E6 -refid BC0829D5C61043A5B71B413015F6792E -t 1 -c 1, -token is dna space token,-appid is you new appkication id create on dna space  -t is mean how many minute to get data from dnac once,'-c' is mean how many time you want to retrieve data from DNAC,if =0 mean,this will run for ever.    
    
    
![Data Collector Engine develop by Pythone](https://github.com/daxu2/MFG--Auto-Management-Platform-Cross-IT_OT-base-on-Cisco-Solution/blob/main/images/develop-python.jpg)
![Data Visibility develop by spunk](https://github.com/daxu2/MFG--Auto-Management-Platform-Cross-IT_OT-base-on-Cisco-Solution/blob/main/images/develop-splunk.jpg)   


# Use Case Description
Technology Summary :
1.using Cyber Vision to gather IT data,and show customize dashboard by spunk and Kibara.

2.using DNAC Server and Cyber Vision to gather key IT/OT asset and integrate into customer ITIL system.

3.using DNA Space and sensor to monitor MFG OT Environment Monitor and provide sure work space.

4.Notification base on Cyber Vision,DNAC Server,DNA Space monitoring ,and alert by Webex Team and Wechat.

5.DNAC Policy auto active base on Cyber Vision and DNA Space alert event.

Business Summary:
1.IT/OT Unified Management, customer have single plane to manage IT/OT device.broken the border between IT and OT

2.provide Secure Workspace & Factory, provide an secure and innovation solution to help customer to create secure workspace and factory

3.Proactive Operation,provide auto dedect,auto monitor, and more innovative services, integrate within company workflow and customer private apps

4.IT/OT visibility, provide MFG vertical whole level visibility function

![IO/OT_Asset_management](https://github.com/daxu2/MFG--Auto-Management-Platform-Cross-IT_OT-base-on-Cisco-Solution/blob/main/images/outcome-asset-management.jpeg)
![Factory_ENV_monitor](https://github.com/daxu2/MFG--Auto-Management-Platform-Cross-IT_OT-base-on-Cisco-Solution/blob/main/images/outcome-OT_ENV_monitor.jpeg)
![Protective Operation](https://github.com/daxu2/MFG--Auto-Management-Platform-Cross-IT_OT-base-on-Cisco-Solution/blob/main/images/outcome-ops.jpeg)

# Topology For This Test

You need to prepare 1 DNAC Server, 1 Catalyst Switch,1 IE Swith, 1 C9800 and AP,1 DNA Space account and developkit with sensor,1 cyber vision server ,1 Server for install code and develop environment，you also need to can access internet becasue you will intergrate Webext Team and Wechat Cloud Service.


![Test Topology](https://github.com/daxu2/MFG--Auto-Management-Platform-Cross-IT_OT-base-on-Cisco-Solution/blob/main/images/topology.jpeg)

# Installation & Configuration
  This sample Code is composed with 3 modules.
  
Module 1:cyber vision_data-adapt.py:

  1) install Python3 on Application Server
  
  2) Copy cyber vision_data-adapt.py to Application Server folder
  
  3) sudo pip3 install requests
  
  4）run the code python3 Cyber vision data-adapt.py -token ics-e8fbcfb8cd54c6d70fba097b208f5115d5957c99-dbdd29d584c19dd2a37c8e71ee72a8310f74a586 -i 172.16.63.248 -t 1 -c 1, -token is cyber vison token ,'172.16.63.248' is cyber vison IP address, -t is mean how many minute to get data from dnac once,'-c' is mean how many time you want to retrieve data from cyber vison,if =0 mean,this will run for ever.  

Module 2:dnac_data-adapt.py :

  1) install Python3 on Application Server
  
  2) Copy assurnace_haixin.py to Application Server folder
  
  3) under same folder,you need to create clientdata and devicedata floder
  
  4) sudo pip3 install requests
  
  5）run the code python3 dnac_data-adapt.py -u admin -p Cisc0123 -i 172.16.63.248 -t 1 -c 1, 'admin is DNAC username,'Cisc0123' is DNAC password,'172.16.63.248' is DNAC IP address, -t is mean how many minute to get data from dnac once,'-c' is mean how many time you want to retrieve data from DNAC,if =0 mean,this will run for ever.

Module 3:dnac_data-adapt.js :

  1) install Python3 on Application Server
  
  2) Copy dnac_data-adapt.py to Application Server folder
  
  3) sudo pip3 install requests
  
  4）run the code python3 dnaspace_data-adapt.py -token eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhcHBJZCI6ImFwcC00OTA5RTY1RUYyOEE0MkQzQTQ2QzE4MEVGRjA2QjBFNiIsInZlcnNpb24iOiJ2MSIsImFjdGl2YXRpb25SZWZJZCI6IkJDMDgyOUQ1QzYxMDQzQTVCNzFCNDEzMDE1RjY3OTJFIiwiY3VzdG9tZXIiOiJFdGhhblpob3UiLCJleHBpcmVzSW4iOjE2MjI0MzI2MDE3MDcsInRlbmFudElkIjoxMDA1MSwiYmFzZVVybCI6Imh0dHBzOi8vcGFydG5lcnMuZG5hc3BhY2VzLmlvIiwicGFydG5lclRlbmFudElkIjoiNTJFM0E4QkU3Nzk4NDY1ODg0RUYxOUZEMzk4RkEyRjMiLCJpYXQiOjE2MjI0MjkwMDEsImV4cCI6MTYyMjQzMjYwMX0.JQs3h-qQ8fGQ97ERNLBiNHn-mT_7pYFzBPd3k1YGpNH3Q1gjMJYOBq8cvRipe7B3phFk7h8Ho9wcxjvgngp-_ichxrSn1hF3Vr1Ohhg-DMtoXx3dxRZK8S3A2Qej6_TEZScfxDm47RV8uUugXogV7sjaQJt0t8-sF6r3Lu2NGoM -appid app-4909E65EF28A42D3A46C180EFF06B0E6 -refid BC0829D5C61043A5B71B413015F6792E -t 1 -c 1, -token is dna space token,-appid is you new appkication id create on dna space  -t is mean how many minute to get data from dnac once,'-c' is mean how many time you want to retrieve data from DNAC,if =0 mean,this will run for ever. 



# Credits and references

    Projects that inspired you
    Related projects
    Books, papers, talks, or other sources that have meaningful impact or influence on this code

# Licensing info

These terms govern this Cisco Systems, Inc. (“Cisco”), example or demo source code and its associated documentation (together, the “Sample Code”). By downloading, copying, modifying, compiling, or redistributing the Sample Code, you accept and agree to be bound by the following terms and conditions (the “License”). If you are accepting the License on behalf of an entity, you represent that you have the authority to do so (either you or the entity, “you”). Sample Code is not supported by Cisco TAC and is not tested for quality or performance. This is your only license to the Sample Code and all rights not expressly granted are reserved.

1. LICENSE GRANT: Subject to the terms and conditions of this License, Cisco hereby grants to you a perpetual, worldwide, non-exclusive, non-transferable, non-sublicensable, royalty-free license to copy and modify the Sample Code in source code form, and compile and redistribute the Sample Code in binary/object code or other executable forms, in whole or in part, solely for use with Cisco products and services. For interpreted languages like Java and Python, the executable form of the software may include source code and compilation is not required.

2. CONDITIONS: You shall not use the Sample Code independent of, or to replicate or compete with, a Cisco product or service. Cisco products and services are licensed under their own separate terms and you shall not use the Sample Code in any way that violates or is inconsistent with those terms (for more information, please visit: www.cisco.com/go/terms ).

3. OWNERSHIP: Cisco retains sole and exclusive ownership of the Sample Code, including all intellectual property rights therein, except with respect to any third-party material that may be used in or by the Sample Code. Any such third-party material is licensed under its own separate terms (such as an open source license) and all use must be in full accordance with the applicable license. This License does not grant you permission to use any trade names, trademarks, service marks, or product names of Cisco. If you provide any feedback to Cisco regarding the Sample Code, you agree that Cisco, its partners, and its customers shall be free to use and incorporate such feedback into the Sample Code, and Cisco products and services, for any purpose, and without restriction, payment, or additional consideration of any kind. If you initiate or participate in any litigation against Cisco, its partners, or its customers (including cross-claims and counter-claims) alleging that the Sample Code and/or its use infringe any patent, copyright, or other intellectual property right, then all rights granted to you under this License shall terminate immediately without notice.

4. LIMITATION OF LIABILITY: CISCO SHALL HAVE NO LIABILITY IN CONNECTION WITH OR RELATING TO THIS LICENSE OR USE OF THE SAMPLE CODE, FOR DAMAGES OF ANY KIND, INCLUDING BUT NOT LIMITED TO DIRECT, INCIDENTAL, AND CONSEQUENTIAL DAMAGES, OR FOR ANY LOSS OF USE, DATA, INFORMATION, PROFITS, BUSINESS, OR GOODWILL, HOWEVER CAUSED, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

5. DISCLAIMER OF WARRANTY: SAMPLE CODE IS INTENDED FOR EXAMPLE PURPOSES ONLY AND IS PROVIDED BY CISCO “AS IS” WITH ALL FAULTS AND WITHOUT WARRANTY OR SUPPORT OF ANY KIND. TO THE MAXIMUM EXTENT PERMITTED BY LAW, ALL EXPRESS AND IMPLIED CONDITIONS, REPRESENTATIONS, AND WARRANTIES INCLUDING, WITHOUT LIMITATION, ANY IMPLIED WARRANTY OR CONDITION OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT, SATISFACTORY QUALITY, NON-INTERFERENCE, AND ACCURACY, ARE HEREBY EXCLUDED AND EXPRESSLY DISCLAIMED BY CISCO. CISCO DOES NOT WARRANT THAT THE SAMPLE CODE IS SUITABLE FOR PRODUCTION OR COMMERCIAL USE, WILL OPERATE PROPERLY, IS ACCURATE OR COMPLETE, OR IS WITHOUT ERROR OR DEFECT.

6. GENERAL: This License shall be governed by and interpreted in accordance with the laws of the State of California, excluding its conflict of laws provisions. You agree to comply with all applicable United States export laws, rules, and regulations. If any provision of this License is judged illegal, invalid, or otherwise unenforceable, that provision shall be severed and the rest of the License shall remain in full force and effect. No failure by Cisco to enforce any of its rights related to the Sample Code or to a breach of this License in a particular situation will act as a waiver of such rights. In the event of any inconsistencies with any other terms, this License shall take precedence.
![image](https://user-images.githubusercontent.com/31427568/130733277-aac9ed31-867f-424f-ad3f-11dc9ca7a5bb.png)
