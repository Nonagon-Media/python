#!/usr/bin/env python3

# Script to display the instance-id of all EC2 containing the string "POC" in a tag
import boto3

# initiate a boto session
session = boto3.Session(profile_name='default')

# create a resource object: (e.g. ec2, s3, sqs)
ec2 = session.resource('ec2')


# Print the instance ids of all instances
# You get ec2.Instance(id='i-123abcd')
for i in ec2.instances.all():
    # Assign the object to a variable
    currentinstance = i

    # Get the tags for the current instnace
    instancetags = currentinstance.tags

    # Iterate the list of tags to get ones tagged POC
    for currenttag in instancetags:
        mytag = currenttag

        if mytag["Key"] == "Purpose":
            check = "POC"

            if check in mytag["Value"]:
                print(currentinstance.id)
