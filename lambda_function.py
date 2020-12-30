import json

print('Loading function')

def lambda_handler(event, context):
	print('-')
	print('--------------------> Starting handler...')
	
	print(event)
	try:
		for record in event['Records']:
			if record['eventName'] == 'INSERT':
				handle_insert(record)
			elif record['eventName'] == 'MODIFY':
				handle_modify(record)
			elif record['eventName'] == 'REMOVE':
				handle_remove(record)
		return "Success!"
	except Exception as e: 
		print(e)
		return "Error"


def handle_insert(record):
	print("==> INSERT Event")
	
	#Get newImage content
	newImage = record['dynamodb']['NewImage']
	
	#Parse values
	newDeviceId = newImage['deviceId']['S']

	print ('New device added with deviceId=' + newDeviceId)

	print("Done!")

def handle_modify(record):
	print("==> UPDATE Event")

	#Parse oldImage and name
	oldImage = record['dynamodb']['OldImage']
	oldName = oldImage['name']['S']
	
	#Parse newImage and name
	newImage = record['dynamodb']['NewImage']
	newName = newImage['name']['S']

	#Check for change
	if oldName != newName:
		print('Name changed - oldName=' + oldName + ', newName=' + newName)

	print("Done!")

def handle_remove(record):
	print("==> REMOVE Event")

	#Parse oldImage
	oldImage = record['dynamodb']['OldImage']
	
	#Parse values
	oldDeviceId = oldImage['deviceId']['S']

	print ('Device removed with deviceId=' + oldDeviceId)

	print("Done!")
	