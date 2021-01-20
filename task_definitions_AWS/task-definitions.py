import botocore.session
import botocore
from os import system

session = botocore.session.get_session()
client = session.create_client('ecs', region_name='eu-west-4')

#we obtain the families of the task
families = client.list_task_definition_families()

#we travel family to family
for familie in families['families']:	
	tasks = client.list_task_definitions(familyPrefix = familie)
	k = len(tasks['taskDefinitionArns'])

	#print all options 
	if k >= 2:
		print('All the family tasks '+familie+': ')

		for task in tasks['taskDefinitionArns']:
			print (task)

		print(' ')


		print('The task will be preserved: '+tasks['taskDefinitionArns'][k-1]+'\n') 
		del tasks['taskDefinitionArns'][k-1]


		for task in tasks['taskDefinitionArns']:
			print ('Is going to disactivate: '+task)
		print (' ')


		#disactivate tasks manually
		resp = input('Do you want to make the changes? (y/n)')
		if resp == 'y':
			for task in tasks['taskDefinitionArns']:
				derigister = client.deregister_task_definition(taskDefinition=task)

		#disable tasks automatically
		#for task in tasks['taskDefinitionArns']:
		#	derigister = client.deregister_task_definition(taskDefinition=task)	


		system("clear")



