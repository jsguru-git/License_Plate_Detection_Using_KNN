import sys
import MySQLdb
import Main
from datetime import datetime
from twilio.rest import Client

def  sms(str2, date,inTime, plate):
	print("entered")
	# put your own credentials here:
	str2 = '7741932130'
	ACCOUNT_SID = "AC2f24970ae089ef0187450a2567cd60a0"
	AUTH_TOKEN = "6a5abd288ff15c8ad2c3d53ac056ecbf"
	client = Client(ACCOUNT_SID,AUTH_TOKEN)
	str1 = '+91'
	num = str1+str2
	body="Your car : "
	body = body + plate
	body = body + ' has entered XYZ society on '
	new = body + date
	new =  new + " at "
	new = new + inTime
	print(new)
	try:
	       
		client.messages.create(to=num, from_="+16699001521", body=new)
		print("sent")
	except:
		print("not sent")
def entry(plate):
	try:
		dbc = MySQLdb.connect("localhost", "root", "Sneha@1998", "plate") 
		
		sql = "select *from plateInfo where number = '"+plate+"'"
		cursor = dbc.cursor()
		cursor.execute(sql)
		results = cursor.fetchall()
		try:
			num_ = map(str, results[0][1])
			now = datetime.now()
			#print("now =", now)
			dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
			list_ = dt_string.split(' ')
			date = list_[0]
			inTime = list_[1]
			print(date)
			print(inTime)
			#will send the sms
			try:
				sms(num_, date, inTime, plate)
			except:
				print('unable to send sms')			
			#just for the outtime
			#sleep(1)
			now = datetime.now()
			dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
			list_ = dt_string.split(' ')
			outTime = list_[1]
			try:
				sql = "select plt_no from resiInfo where plt_no = '"+plate+"'"
			except:
				print('couldnot access resiInfo')			
			cursor = dbc.cursor()
			cursor.execute(sql)
			results = cursor.fetchall()
		
			if(results == ()):
				
				resident = 'no'
			else:
				resident = 'yes'
			try:
				print(plate)
				sql = "insert into history (number, date, inTime, outTime, resident) values('"+plate+"','"+date+"','"+inTime+"','"+outTime+"','"+resident+"')"
				cursor = dbc.cursor()
				cursor.execute(sql)
				dbc.commit()	
			except:
				print("error while updating history")	
		except:
			print("error while updating history2")		
	except:
		print('error in connecting to db')	
		
		


if __name__ == '__main__':
	main()

