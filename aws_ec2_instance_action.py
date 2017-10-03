#!/usr/bin/env python

import boto3
import time
from pprint import pprint


class AwsApi(object):
    """
    This class is to start, stop or terminate single or multiple aws ec2 instances for any account.
    """
    def __init__(self):
        """
        Initialize the objects for ec2 clients and resources.
        """
        self.ec2_instance = boto3.resource('ec2')
        self.ec2_client = boto3.client('ec2')

    def stop_ec2_instance(self, instance_list):
        """
        This is to stop aws ec2 instance(s). This method will need list of instances at runtime to stop.
        :return:
        """
        for ins in instance_list:
            instance = self.ec2_instance.Instance(ins)
            try:
                response = instance.stop()
                print response
            except Exception, e1:
                raise OSError("Error while instance was stopped ...." + e1.message, e1.args, e1.__class__)
            finally:
                print("Instance %s was attempted to stop" % instance)
        print ("Instance %s has been stopped" % instance)

    def start_ec2_instance(self, instance_list):
        """
        This is to start aws ec2 instance(s).This method will need list of instance(s) at runtime to start.
        :return:
        """
        for ins in instance_list:
            instance = self.ec2_instance.Instance(ins)
            try:
                response = instance.start()
                print response
            except Exception, e1:
                raise OSError("Error while instance was starting ..." + e1.message, e1.args, e1.__class__)
            finally:
                print("Instance %s was attempted to start" % instance)
        print ("Instance %s has been started" % instance)

    def terminate_ec2_instance(self, instance_list):
        """
        This is to terminate aws ec2 instance(s).This method will need list of instance(s) at runtime to terminate.
        :return:
        """
        for ins in instance_list:
            instance = self.ec2_instance.Instance(ins)
            try:
                response = instance.terminate()
                print response
            except Exception, e1:
                raise OSError("Error while instance was terminating ...." + e1.message, e1.args, e1.__class__)
            finally:
                print("Instance %s was attempted to terminate" % instance)
        print ("Instance %s has been terminated" % instance)


def main():
    """
    program control to kick-off the execution of aws ec2 operations.
    :return:
    Example: instance_list = ['i-1823138d', 'i-1823138d']
    """
    instance_list = list()

    # Location of the file on the server where you will have the list of instance(s) to perform the operations.
    file_path = '/opt/devops/python_source_code/instances'
    with open(file_path) as f:
        for line_terminated in f:
            line = line_terminated.strip()
            instance_list.append(line)
    for instance in instance_list:
        print instance

    # Object initialization
    aws = AwsApi()

    # You can run either one of the below operations on the same list of instance(s) to perform any of the operations it specifies.
    aws.stop_ec2_instance(instance_list)
    #aws.start_ec2_instance(instance_list)
    #aws.terminate_ec2_instance(instance_list)

if __name__ == "__main__":
    main()
