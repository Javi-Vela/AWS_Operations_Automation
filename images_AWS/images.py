import botocore.session
import botocore


def image(directory):

	#list images
	imag = client.describe_images(repositoryName = directory)
	max1=imag['imageDetails'][0]['imagePushedAt']
	max2=imag['imageDetails'][0]['imagePushedAt']
	k = len(imag['imageDetails'])
	i = range(len(imag['imageDetails']))
	digest = [[]]
	s=0
	l=0

	#order images
	if k > 2:
		print ("The directory is: "+directory+"\n")
		#most recent images
		date_max1 = max((q['imagePushedAt']) for q in imag['imageDetails'])
		date_max2 = max((q['imagePushedAt']) for q in imag['imageDetails'] if q['imagePushedAt'] != date_max1)


		#remove images from dictionary by index
		for j in i:
			if imag['imageDetails'][j]['imagePushedAt'] == date_max1:
				index = j
			if imag['imageDetails'][j]['imagePushedAt'] == date_max2:
				index2 = j
		print ("Stay: "+str(imag['imageDetails'][index]['imageDigest'])+" Date: "+str(imag['imageDetails'][index]['imagePushedAt']))
		print ("Stay: "+str(imag['imageDetails'][index2]['imageDigest'])+" Date: "+str(imag['imageDetails'][index2]['imagePushedAt'])+"\n")
		del imag['imageDetails'][index]
		del imag['imageDetails'][index2]
		
		

		#convert dictionary to array 
		for g in imag['imageDetails']:
			digest[s]=g['imageDigest']
			digest.append(1)
			s+=1


		#print images and remove
		print ("Remove: ")
		for h in imag['imageDetails']:
			print ("Date: "+str(h['imagePushedAt'])+" Image digest: "+str(h['imageDigest']))
			#remove image
			#delet=client.batch_delete_image(repositoryName=directory, imageIds=[{'imageDigest' : digest[l]}])
			#l+=1



#--------------------------------------------------------------main-----------------------------------------

#start session
session = botocore.session.get_session()
client = session.create_client('ecr', region_name='eu-center-4')

#repository name and sed
repos = client.describe_repositories()

for x in repos['repositories']:	
	image(x['repositoryName'])
	#print()



	
