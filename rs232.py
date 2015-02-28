import time
import serial
import csv

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=115200,
	parity=serial.PARITY_ODD,
	stopbits=serial.STOPBITS_TWO,
	bytesize=serial.SEVENBITS
)

ser.open()
ser.isOpen()

def update_csv(data):
	writer = csv.writer(open("test_data.csv", "wb"),delimiter='\n')
	writer.writerow(data)



input=1
out=''
table=[]
option="true"

while 1 :
	
		
		
		
		if  ser.inWaiting() > 0:
			out += ser.read(20)
			if out!='':
				reader = csv.reader(open("test_data.csv"),delimiter='|')
				for row in reader:
					
					if row[1]=="Inventory":
						if row[2]!=out:
							option="true"
							table.append(row[0]+"|"+row[1]+"|"+out)
						else:
							table.append(row[0]+"|"+row[1]+"|"+row[2])

					else:
						table.append(row[0]+"|"+row[1]+"|"+row[2])

				
				if option=="true":
					update_csv(table)
				table =[]
				print out
				out=''
				ser.write("020501283403")
				ser.flush()
				ser.flushInput()
				ser.flushOutput()
				time.sleep(2)
			
		elif ser.inWaiting()<=0:
			print "Item Removed"
			reader = csv.reader(open("test_data.csv"),delimiter='|')
			for row in reader:

                                        if row[1]=="Inventory":
						table.append(row[0]+"|"+row[1]+"|NoItems")
                                        else:     
						table.append(row[0]+"|"+row[1]+"|"+row[2])
			
			update_csv(table)
			table =[]

			time.sleep(5)

