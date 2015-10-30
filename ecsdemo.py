# Short script to demonstrate S3 bucket and object creation, copying, and deletion
# using Python programming language with AWS SDK (boto)
#
# Mike Greenleaf 9/12/2015
# Updated 10/5/2015
# Compliments to Amazon for the sample script.  Heavily modified for my demo.

# Import the SDK
import boto

# Import uuid to be used for creating a unique bucket name
import uuid

# The AWS SDK for Python (Boto) will look for
# access keys in these environment variables:
#
#    AWS_ACCESS_KEY_ID='...'
#    AWS_SECRET_ACCESS_KEY='...'
#
# For more information about this interface to Amazon S3, see:
# http://boto.readthedocs.org/en/latest/s3_tut.html

# Import the boto s3.connection function into variable S3Connection
from boto.s3.connection import S3Connection

# Set environmental variables for ACCESS KEY, SECRET KEY and ENDPOINT.  other possible
# variables are documented at https://community.emc.com/docs/DOC-37048.  We are using
# the ECS TEST Drive site to test (https://portal.ecstestdrive.com/) which has a defined
# ENDPOINT and listens on port 443.  If using straigh IP address, ECS S3 listens on ports
# 9220 (HTTP) and 9221 (HTTPS)
accessKeyId = 'ACCESS KEY'
secretKey = 'SECRET KEY'
host = 'object.ecstestdrive.com'

# Create a connection to the ECS S3 service.  Set variable conn as the connection string.
#
# Other possible variable to include are documented at site https://community.emc.com/docs/DOC-37048
conn = S3Connection(aws_access_key_id=accessKeyId,
                    aws_secret_access_key=secretKey,
                    host=host,
                    )

# Kick off the demo .  
print " "
raw_input("Welcome to the ECS S3 DEMO!")
print " "

# Everything uploaded to ECS via S3 must belong to a bucket. These buckets are
# in the global namespace, and must have a unique name.
#
# For more information about bucket name restrictions, see:
# http://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html

# create a unique bucket NAME and assign to variable "bucket_name"
bucket_name = "ecs-demo-%s" % uuid.uuid4()
raw_input("First, we will  create a new bucket...")
print " "
print "Creating new bucket with name: " + bucket_name
print " "

# create new bucket and assign to variable "bucket"
conn.create_bucket(bucket_name)

# List out all buckets in namespace.  Out will include NEW bucket as well as those created
# prior to the start of the demo
print "  "
print "Lets list all of our buckets by creation date"
print "  "

for bucket in conn.get_all_buckets():
        print "{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
        )
print "  "

# Files in S3 are called "objects" and are stored in buckets. A specific
# "object" is referred to by its key (i.e., name) and holds data. Here, we create
# a new object with the KEY "python_sample_key.txt" and CONTENT "Hello World!".
#
# For more information on keys and set_contents_from_string, see:
# http://boto.readthedocs.org/en/latest/s3_tut.html#storing-data

# Create a NEW OBJECT (KEY) in our BUCKET.
#
# Import boto s3.key function into variable Key.  Then, set the variable K to the NEWLY created
# bucket name.  Lastly, create a new OBJECT (key) with the name python_sample_key
from boto.s3.key import Key
k = Key(bucket)
k.key = 'python_sample_key.txt'

# put some content in the new object (key)
raw_input("Now lets create an object and put it in our new bucket...")
print "  "
print "Uploading some data to " + bucket_name + " with key: " + k.key
k.set_contents_from_string('Hello World!')

# Fetch the key to show that we stored something. Key.generate_url will
# construct a URL that can be used to access the object for a limited time.
# Here, we set it to expire in 30 minutes.  
#
# For a more detailed overview of generate_url's options, see:
# http://boto.readthedocs.org/en/latest/ref/s3.html#boto.s3.key.Key.generate_url
#
# Set a time for the URL to expire
expires_in_seconds = 1800

# Now generate URL and set it to the value demourl
print " "
raw_input("Create a public URL for our new object...")
print " "
print "Generating a public URL for the object we just uploaded. This URL will be active for %d seconds" % expires_in_seconds
print " "
demourl = k.generate_url(expires_in_seconds)

# Print out the URL
print demourl
print " "

# Print out the CONTENTS of the URL.  This is the actual data.
import urllib2
response = urllib2.urlopen(demourl)
raw_input ("Access the URL to print out the contents of the object...")
print " "
print "The data contents of the object are:   ",response.read()
print " "

# Delete the object...clean up
raw_input("Now delete the object we created.  Press enter to delete the object...")

# Buckets cannot be deleted unless they're empty. Since we still have a
# reference to the key (object), we can just delete it.
print " "
print "Deleting the object."
print " "
k.delete()

# Copy a file from local PC to S3 Bucket
raw_input("Demontrate how to copy a file from our local PC to our S3 Bucket. Press enter to continue...")

# This is what the object will be named in the bucket.
k.key = 'uploadedcopyfile.txt'

# Set the name of the local PC file to copy
k.set_contents_from_filename("copyfile.txt")

raw_input("Once complete, delete this object.  Press enter to continue...")
print " "
print "Deleting the object"
print " "

# Delete the object
k.delete()

# Copy a file from my local PC called "frompc.txt" to another name "topc.txt" in the same location
# using s3 to copy the file
raw_input("Demonstrate how to use S3 to make a local copy of a file.  Press enter to continue...")
print " "

# This is what the object will be called in the bucket
k.key = 'myfile.txt'

# This is the SOURCE PC file 
k.set_contents_from_filename('frompc.txt')

# This is the TARGET PC file
k.get_contents_to_filename('topc.txt')
print " "
raw_input("Validate the new file was created.  Look at both the S3 bucket and PC")

# Now delete both the object and the bucket.
print " "
raw_input("Now delete both the object and the bucket...")

# Buckets cannot be deleted unless they're empty. Since we still have a
# reference to the key (object), we can just delete it.
print " "
print "Deleting the object."
k.delete()

# Now that the bucket is empty, we can delete it.
print " "
print "Deleting the bucket."
conn.delete_bucket(bucket_name)
print "  "

# Lastly, list out the buckets again.  Only remaining buckets will be bukects created prior to the start of our DEMO.
for bucket in conn.get_all_buckets():
        print "{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
        )

# Clean up PC file
import os
print "  "
os.remove("c:/ecsdemo/topc.txt")

print "  "
raw_input ("End of DEMO.  Thank you!")
