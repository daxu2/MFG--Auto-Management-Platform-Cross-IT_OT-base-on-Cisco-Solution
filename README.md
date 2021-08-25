# MFG--Auto-Management-Platform-Cross-IT_OT-base-on-Cisco-Solution
   First of all, IT/OT is more closed and seamless integration. customers want to have single plane to manage IT/OT device.broken the border between IT and OT

   Secondly, Secure is highest priority for all customer. what can we provide an secure and innovation solution to help customer to create secure workspace and factory,who will win the customer

   Thirdly, we proive proactive  IT/OT operations, provide auto dedect,auto monitor, and more innovative services, integrate within company workflow and customer private apps.
   
  Other things you might include:
    Technology stack: This Example Code is composed with 3 moduel,data visibility by splunk can not be upload on github,so this demo code only include data collect engine module.   
    1.Cyber vision data-adapt.py : This is a Saple code using Python,this code is get data from cyber vision and can be display on Splunk and kibana,you can using follow command to run the code python3 Cyber vision data-adapt.py -token ics-e8fbcfb8cd54c6d70fba097b208f5115d5957c99-dbdd29d584c19dd2a37c8e71ee72a8310f74a586 -i 172.16.63.248 -t 1 -c 1, -token is cyber vison token ,'172.16.63.248' is cyber vison IP address, -t is mean how many minute to get data from dnac once,'-c' is mean how many time you want to retrieve data from cyber vison,if =0 mean,this will run for ever.  
    2.dnac_data-adapt.py : This is a Saple code using Python,this code is get data from DNAC and can be display on Splunk,you can using follow command to run the code python3 dnac_data-adapt.py -u admin -p Cisc0123 -i 172.16.63.248 -t 1 -c 1, 'admin is DNAC username,'Cisc0123' is DNAC password,'172.16.63.248' is DNAC IP address, -t is mean how many minute to get data from dnac once,'-c' is mean how many time you want to retrieve data from DNAC,if =0 mean,this will run for ever. 
    3.dnaspace_data-adapt.py: This is a Saple code using Python,this code is get data from DNA Space and can be display on Splunk and kibana,you can using follow command to run the code python3 dnaspace_data-adapt.py -token eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhcHBJZCI6ImFwcC00OTA5RTY1RUYyOEE0MkQzQTQ2QzE4MEVGRjA2QjBFNiIsInZlcnNpb24iOiJ2MSIsImFjdGl2YXRpb25SZWZJZCI6IkJDMDgyOUQ1QzYxMDQzQTVCNzFCNDEzMDE1RjY3OTJFIiwiY3VzdG9tZXIiOiJFdGhhblpob3UiLCJleHBpcmVzSW4iOjE2MjI0MzI2MDE3MDcsInRlbmFudElkIjoxMDA1MSwiYmFzZVVybCI6Imh0dHBzOi8vcGFydG5lcnMuZG5hc3BhY2VzLmlvIiwicGFydG5lclRlbmFudElkIjoiNTJFM0E4QkU3Nzk4NDY1ODg0RUYxOUZEMzk4RkEyRjMiLCJpYXQiOjE2MjI0MjkwMDEsImV4cCI6MTYyMjQzMjYwMX0.JQs3h-qQ8fGQ97ERNLBiNHn-mT_7pYFzBPd3k1YGpNH3Q1gjMJYOBq8cvRipe7B3phFk7h8Ho9wcxjvgngp-_ichxrSn1hF3Vr1Ohhg-DMtoXx3dxRZK8S3A2Qej6_TEZScfxDm47RV8uUugXogV7sjaQJt0t8-sF6r3Lu2NGoM -appid app-4909E65EF28A42D3A46C180EFF06B0E6 -refid BC0829D5C61043A5B71B413015F6792E -t 1 -c 1, -token is dna space token,-appid is you new appkication id create on dna space  -t is mean how many minute to get data from dnac once,'-c' is mean how many time you want to retrieve data from DNAC,if =0 mean,this will run for ever.    
    
    
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
![Protective Operation](https://github.com/daxu2/MFG--Auto-Management-Platform-Cross-IT_OT-base-on-Cisco-Solution/blob/main/images/outcome-OT_ENV_monitor.jpeg)

# Topology For This Test

You need to prepare 1 DNAC Server, 1 Catalyst Switch,1 IE Swith, 1 C9800 and AP,1 DNA Space account and developkit with sensor,1 cyber vision server ,1 Server for install code and develop environment，you also need to can access internet becasue you will intergrate Webext Team and Wechat Cloud Service.
![Test Topology](https://github.com/daxu2/MFG--Auto-Management-Platform-Cross-IT_OT-base-on-Cisco-Solution/blob/main/images/topology.jpeg)

# Installation & Configuration
  This Example Code is composed with 3 moduel.
  
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

A license is required for others to be able to use your code. An open source license is more than just a usage license, it is license to contribute and collaborate on code. Open sourcing code and contributing it to Code Exchange or Automation Exchange requires a commitment to maintain the code and help the community use and contribute to the code.

Choosing a license can be difficult and depend on your goals for your code, other licensed code on which your code depends, your business objectives, etc. This template does not intend to provide legal advise. You should seek legal counsel for that. However, in general, less restrictive licenses make your code easier for others to use.

    Cisco employees can find licensing options and guidance here.

Once you have determined which license is appropriate, GitHub provides functionality that makes it easy to add a LICENSE file to a GitHub repo, either when creating a new repo or by adding to an existing repo.

When creating a repo through the GitHub UI, you can click on Add a license and select from a set of OSI approved open source licenses. See detailed instructions.

Once a repo has been created, you can easily add a LICENSE file through the GitHub UI at any time. Simply select Create New File, type LICENSE into the filename box, and you will be given the option to select from a set of common open source licenses. See detailed instructions.

Once you have created the LICENSE file, be sure to update/replace any templated fields with appropriate information, including the Copyright. For example, the 3-Clause BSD license template has the following copyright notice:

Copyright (c) <YEAR>, <COPYRIGHT HOLDER>

See the LICENSE for this template repo as an example.

Once your LICENSE file exists, you can delete this section of the README, or replace the instructions in this section with a statement of which license you selected and a link to your license file, e.g.

This code is licensed under the BSD 3-Clause License. See LICENSE for details.

Some licenses, such as Apache 2.0 and GPL v3, do not include a copyright notice in the LICENSE itself. In such cases, a NOTICE file is a common place to include a copyright notice. For a very simple example, see NOTICE.

In the event you make use of 3rd party code, it is required by some licenses, and a good practice in all cases, to provide attribution for all such 3rd party code in your NOTICE file. For a great example, see https://github.com/cisco/ChezScheme/blob/master/NOTICE.
Best practices

Information below can help you make your repo meet our requirements and be more useful to others.
Good practices

    Manage sensitive data for scripts. For example, store passwords/API keys and other sensitive data in env.py or parse it as arguments. In Python, you can use ConfigParser for applications and programs: encrypt sensitive data in your database.
    Include in Installation section how to run your script for different OS like Windows/macOS/Linux
    Print usage if you run script or program without any input data (support -h -help flags)
    Catch an error and print useful information in console and interface
    Add error management to handle if users miss some parameters or add them in the wrong format
    Add links for resources where users can test code/app. For example, add links DevNet sandboxs (Always-on or reservable). You can find a list of all available sandboxes here https://devnetsandbox.cisco.com/RM/Topology
    Add links where users can download and how to install additional soft/app/libraries that are needed to run your code. For example, installer for Python, node, etc.
    Add NOTICE file with copyright if you use GPLv3 or Apache 2.0 license (sample)
    Dockerize app or part of an app, like a server/client
![image](https://user-images.githubusercontent.com/31427568/130733277-aac9ed31-867f-424f-ad3f-11dc9ca7a5bb.png)
