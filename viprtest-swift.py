# Sample Python script to demonstrate SWIFT access/functionality to ECS test Drive
# SOurce script downloaded from https://community.emc.com/docs/DOC-37964...THANK YOU...
# and slightly customized.
#
# Mike Greenleaf - 10/5/2015
#
# Establish our connection and import the print library
from swiftclient import Connection
from pprint import pprint

# Setup your endpoint and credentials here
# Also, the key is the password.  Swift password TAB
endpoint = 'https://swift.ecstestdrive.com'
user = 'USER'
key = 'PASSWORD'

# Config for testing
container_name = 'python-test'
object_name = 'hello.txt'

# This uses swauth (v1.0) auth
# ECS Test drive provides endpoint for V1.0 and 2.0 auth
swift = Connection(
                authurl=endpoint + "/auth/v1.0", 
                user=user, 
                key=key, 
                auth_version="1",
                #insecure=True...default is FALSE
                )


print '  '
print('Logged in using swauth, listing containers\n')
print '------------------------\n'


(headers, containers) = swift.get_account()

# Uncommment to print out http header
#print 'account headers: '
#pprint(headers)

print 'account containers: '
pprint(containers)
print '------------------------\n'
raw_input("Any Containers listed?...")

# Create container
print 'creating container %s...' % container_name
swift.put_container(container=container_name)
print 'done!'
print '------------------------\n'

(headers, containers) = swift.get_account()

print ' '
print 'List account containers again: '
pprint(containers)
print '------------------------\n'
raw_input("Any Containers listed this time?...")

# Upload object to container
print ' '
print 'creating object %s in %s...' % (object_name, container_name)
swift.put_object(container=container_name, 
                      obj=object_name, 
                      contents='Hello World!',
                      content_type='text/plain')
print 'done!'
print '------------------------\n'

# Read object back
print ' '
print 'reading object %s in %s...\n' % (object_name, container_name)
(headers,content) = swift.get_object(container=container_name, obj=object_name)
print 'content: %s\n' % content

# Uncomment to print out http header
#print 'headers: '
#pprint(headers)

print 'done!'
print '------------------------\n'
raw_input("Object created, now verify with Cyberduck...")


# Delete object...clean up
print ' '
print 'Deleting object %s in %s...\n' % (object_name, container_name)
swift.delete_object(container=container_name, obj=object_name)
print 'done!'
print '------------------------\n'

# Delete container
print 'deleting container %s...' % container_name
swift.delete_container(container=container_name)
print 'done!'
print '------------------------\n'
raw_input ("Refresh Cyberduck.  Object and container still there?")


