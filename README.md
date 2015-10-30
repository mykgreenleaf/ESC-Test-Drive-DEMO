# ESC-Test-Drive-DEMO
ECS Test Drive DEMO set up and Scripts - Python

ECS Demo Cookbook
Accessing ECS Objects Using Python (Windows 7)
Using both the S3 and SWIFT API

1.	Create an account on the ECS Test Drive site  https://portal.ecstestdrive.com/
a.	Once the account is created, make sure to create at least ONE secret key for S3!  Click on CREDENTIALS  MANAGE SECRET KEYS  CREATE SECRET KEY
b.	Create a SWIFT Password!  Click on CREDENTIALS  Swift Password  SET PASSWORD (make it something EASY to remember!) 
c.	Click on CREDENTIALS once again, and keep the site open. You will need it to establish access with your programs and tools.
2.	Install S3 Browser (http://s3browser.com/) and/or Cyberduck (https://cyberduck.io/)
3.	Enter credentials for desktop tool to establish connectivity.  
a.	Cyberduck S3:
i.	Click CONNECTION.
ii.	Select “S3 Amazon Simple Storage Service” from drop down list
iii.	Cut and paste the END POINT (object.ecstestdrive.com) from the ECS Test Drive CREDENTIALS site into the SERVER field
iv.	Cut and paste Access key and Secret Access Key into appropriate fields
b.	Cyberduck SWIFT:
i.	Click CONNECTION.
ii.	Select “Swift Openstack Object Storage” from drop down list
iii.	Cut and paste the END POINT (swift.ecstestdrive.com) from the ECS Test Drive CREDENTIALS site into the SERVER field
iv.	Cut and paste Tenant ID, Secret Key and Password into appropriate fields
c.	S3 Browser:
i.	Select ACCOUNTS  ADD NEW ACCOUNT
ii.	Choose any name
iii.	Select “S3 Compatible Storage” from drop down list
iv.	Cut and paste End point (object.ecstestdrive.com) and Keys from ECS Test Drive CREDENTIALS into appropriate fields.
4.	Install Python.  V2.7 release (https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi) 
a.	Run the msi to install.
b.	Add c:\python27\ to the PATH system environment variable (My Computer  Properties  Advanced System Settings  Environment Variables  Path.  Then click edit and add the value to the end.
5.	Install boto.  Boto is the Python library used to access AWS S3 (AWS SDK).  
a.	Cd c:\python27\scripts
b.	Pip install boto
6.	Install the python SWIFT library
a.	Cd c:\python27\scripts
b.	Pip install python-swiftclient
7.	Write your scripts!  Or, install the four files I included in a new directory on your laptop.  
a.	For S3 Demo:  Run the ecsdemo.py script (c:\python.exe ecsdemo.py).  I included lots of pauses to allow you to observe output using Cyberduck, S3 Browser, or Windows Explorer…depending on where the file/object is moved or created.
b.	For SWIFT Demo:  Run the viprtest-swift.py script (c:\python.exe viprtest-swift.py).  The code is heavily documented and includes lots of pauses.
8.	Interesting Links:
a.	Good Samples at CEPH  http://ceph.com/docs/master/radosgw/s3/python/
b.	Intro to boto  http://boto.readthedocs.org/en/latest/s3_tut.html#creating-a-connection
c.	EMC Getting Started with Python and ECS Page  https://community.emc.com/docs/DOC-37048
d.	EMC Getting Started with ALL SDK’s  https://community.emc.com/docs/DOC-27910
