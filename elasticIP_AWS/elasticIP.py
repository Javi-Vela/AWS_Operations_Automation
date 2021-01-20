import botocore.session
import botocore


# Start session
session = botocore.session.get_session()
client = session.create_client('ec2', region_name='eu-west-4')
response = client.describe_addresses()
for x in response["Addresses"]:
    # Prove that it is in use
    try: 
        error = x["InstanceId"]
    except:
        print ("The elastic ip with ip", x["PublicIp"], "is not being used")
