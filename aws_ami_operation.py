#!/usr/bin/python
########################################################################################################################
#  This script is to create AMI and tag AMI from the existing resource. This script can be used as a step to           #
#  to help modify the instance and create AMI and tag it as necessary.                                                 #
#  Usage:                                                                                                              #
#       aws_ami_operation.py                                                                                           #
#                                                                                                                      #
########################################################################################################################
import boto3
import time
from pprint import pprint


class AwsEC2API(object):
    """
    This is to create the multiple aws instances on specified subnets
    """
    def __init__(self, resourceid):
        """
        To initialize the aws loadbalancer client to perform the operations on it.
        """
        AWS_ACCESS_KEY_ID= '<key>'
        AWS_SECRET_ACCESS_KEY= '<skey>'
        self.client = boto3.client('elb', aws_access_key_id=AWS_ACCESS_KEY_ID,
                                       aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name='us-west-2')
        self.resourceid = resourceid


    def create_ami_tag(self, tag_dict):
        """
        To tag the resource
        :return:
        """
        if self.resourceid is None:
            raise ValueError("Missing resourceId to tag")

        if tag_dict in None:
            raise ValueError("Missing tag key-value for the resource")

        for key_tag, key_value in tag_dict.items:
            response = self.client.create_tags(Resources=[self.resourceid ],Tags=[{'Key': key_tag, 'Value': key_value}])
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                pprint(response)
                print("successfully tagged the instance %s" % )
            else:
                print("ERROR:Unable to process the AMI tagging request")


    def create_ami_from_ec2_instance(self, image_name, description='development_ami'):
        """
        To create new AMI from the existing resource
        :return:
        """
        if self.resourceid is None:
            raise ValueError("Missing resourceId to tag")

        if image_name is None:
            raise ValueError("Missing Image_name value. Please check")

        response = self.client.create_image(InstanceId=self.resourceid, Name=image_name, Description=description, NoReboot=True )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            pprint(response)
            print("successfully tagged the ami from the ec2 instance: %s" % self.resourceid)
        else:
            print("ERROR:Unable to process the AMI creation request")


def main():
    # Test aws instanceID
    resource_id_list = ['i-ddhry9f41']
    image_name = 'test'
    description = 'test_ami_creation'


    # Test tags
    for resource in resource_id_list:
        ami_operation = AwsEC2API(resource)

        # create AMI from instance
        ami_operation.create_ami_from_ec2_instance()

        # Tag AMI
        ami_operation.create_ami_tag(image_name)


# Main execution point
if __name__ == '__main__':
    main()
