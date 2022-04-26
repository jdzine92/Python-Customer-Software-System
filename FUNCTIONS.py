########################
###  JORDAN SYSTEMS  ###
########################

#--- IMPORT MODULES ---#
import tkinter as tk
import sqlite3

#Function for Search Records button within search frame.
def search(Program):
	#connect to database
	conn = sqlite3.connect("patients.db")
	#create cursor
	c = conn.cursor()
	#get data from search_box in main.py and assign it to user_search variable
	user_search = Program.search_box.get()
	print("Hello")
	#select everything from patients table, where last name = whatever was entered
	
	sql = "SELECT * FROM patientstable WHERE last_name = %s"
	name = (user_search, )
	result = c.execute(sql, name)
	#if no match, print result
	if not result:
		result = "Record not found, please try again."
	#display result on screen	
	user_search_label = Label(searchframe, text=result)
	user_search_label.grid(row=0, column=0)
	conn.commit()
	conn.close()
 	
	
#Submit data function for button inside frame
#ADD RECORD TO DB
def submit_record(Program):
	#make global so add_record can access
	global submit_record
	#connect to database
	conn = sqlite3.connect("patients.db")
	#create cursor
	c = conn.cursor()

	#insert into table
	c.execute("INSERT INTO patientstable VALUES (:f_name, :l_name, :dob, :add_l1, :add_l2, :add_l3, :postcode)",
			{

				'f_name': f_name.get(),
				'l_name': l_name.get(),
				'dob': dob.get(),
				'add_l1': add_l1.get(),
				'add_l2': add_l2.get(),
				'add_l3': add_l3.get(),
				'postcode': postcode.get()
			}

		)
	#commit and close db
	conn.commit()
	conn.close()
	#display error or success message to user
	if c.rowcount < 1:
		error_label = Label(addrecordframe, fg="white", bg="gray30", text="Error, record was not entered. ")
		error_label.grid(row=10, column=2, pady=10, ipady=4, sticky=W)
		error_label.config(font=("Calibri", 13))
	else:
		success_label = Label(addrecordframe, fg="white", bg="gray30", text="Record entered sucessfully. ")
		success_label.grid(row=10, column=2, pady=10, ipady=4, sticky=W)
		success_label.config(font=("Calibri", 13))

	#clear textboxes after submitting
	f_name.delete(0, END)
	l_name.delete(0, END)
	dob.delete(0, END)
	add_l1.delete(0, END)
	add_l2.delete(0, END)
	add_l3.delete(0, END)
	postcode.delete(0, END)

#Display function for ADD_BUTTON
def add_record(Program):
	#FRAME for add record, make global so submit_record, edit can access
	global addrecordframe
	addrecordframe = tk.LabelFrame(Program.main, bg="gray30", width=650, height=350)
	addrecordframe.grid(row=3, column=1, pady=10)
	#force width and height on frame
	addrecordframe.grid_propagate(0)

	#add record message
	addrecord_label = tk.Label(addrecordframe, fg="white", bg="gray30", text="Adding new record ")
	addrecord_label.grid(row=3, column=1, pady=10, padx=(20,0), ipady=4, sticky=W)
	addrecord_label.config(font=("Calibri", 13)) 

	#entry boxes (make global so submit can access)
	global f_name
	f_name = Entry(addrecordframe, width=30)
	f_name.grid(row=4, column=2, pady=5, padx=5, ipady=2, sticky=W)

	global l_name
	l_name = Entry(addrecordframe, width=30)
	l_name.grid(row=4, column=4, pady=5, padx=5, ipady=2, sticky=W)

	global dob
	dob = Entry(addrecordframe, width=15)
	dob.grid(row=5, column=4, pady=5, padx=5, ipady=2, sticky=W)

	global add_l1
	add_l1 = Entry(addrecordframe, width=30)
	add_l1.grid(row=5, column=2, pady=5, padx=5, ipady=2, sticky=W)

	global add_l2
	add_l2 = Entry(addrecordframe, width=30)
	add_l2.grid(row=6, column=2, pady=5, padx=5, ipady=2, sticky=W)

	global add_l3
	add_l3 = Entry(addrecordframe, width=30)
	add_l3.grid(row=7, column=2, pady=5, padx=5, ipady=2, sticky=W)

	global postcode
	postcode = Entry(addrecordframe, width=30)
	postcode.grid(row=8, column=2, pady=5, padx=5, ipady=2, sticky=W)

	#text box labels
	f_name_label = tk.Label(addrecordframe, fg="white", bg="gray30", text="First Name")
	f_name_label.grid(row=4, column=1, padx=10, pady=5, sticky=E)

	l_name_label = tk.Label(addrecordframe, fg="white", bg="gray30", text="Last Name")
	l_name_label.grid(row=4, column=3, padx=10, sticky=E)

	dob_label = tk.Label(addrecordframe, fg="white", bg="gray30", text="DOB")
	dob_label.grid(row=5, column=3, padx=10, sticky=E)

	add_l1_label = tk.Label(addrecordframe, fg="white", bg="gray30", text="Address Line 1")
	add_l1_label.grid(row=5, column=1, padx=10, pady=5, sticky=E)

	add_l2_label = tk.Label(addrecordframe, fg="white", bg="gray30", text="Address Line 2")
	add_l2_label.grid(row=6, column=1, padx=10, pady=5, sticky=E)

	add_l3_label = tk.Label(addrecordframe, fg="white", bg="gray30", text="City")
	add_l3_label.grid(row=7, column=1, padx=10, pady=5, sticky=E)

	postcode_label = tk.Label(addrecordframe, fg="white", bg="gray30", text="Postcode")
	postcode_label.grid(row=8, column=1, padx=10, pady=5, sticky=E)

	#Submit entry button
	submit_button = tk.Button(addrecordframe, text="Add Record", command=submit_record,  fg="white", bg="black")
	submit_button.grid(row=9, column=2, pady=10, padx=20, ipadx=5, ipady=5)
	submit_button.config(font=("Calibri", 12)) 

#FUNCTIONS FOR SHOW ALL_BUTTON (from menu)
#Delete function for SHOW_ALL
def delete():
	#connect to database
	conn = sqlite3.connect("patients.db")
	#create cursor
	c = conn.cursor()
	#delete function (search by oid)
	c.execute("DELETE from patientstable WHERE oid = " + delete_box.get())
	#Commit and close connection
	conn.commit()
	conn.close()
#Display function for SHOW_ALL
def query():
	#FRAME for show all
	global showrecordframe
	showrecordframe = LabelFrame(main, bg="gray30", width=650, height=350)
	showrecordframe.grid(row=3, column=1, pady=10)
	#force width and height on frame
	showrecordframe.grid_propagate(0)

	#connect to database
	conn = sqlite3.connect("patients.db")
	#create cursor
	c = conn.cursor()
	#Show user how many records there are in db
	#run query (select everything)
	c.execute("SELECT * FROM patientstable")
	records = c.fetchall()
	recordcount = len(records)

	#showing all records label
	allrecords_label = Label(showrecordframe, fg="white", bg="gray30", text="There are " + str(recordcount) + " records in the database today.")
	allrecords_label.grid(row=0, column=0, padx=(20, 0), pady=(20,0), ipady=4, sticky=W)
	allrecords_label.config(font=("Calibri", 13))
	#run query (select everything and the primary key(oid))
	c.execute("SELECT *,oid FROM patientstable")
	#fetch all records (assign var)
	#show all records in the system
	records = c.fetchall()
	''' format results:
	set variable print_records to nill
	cycle through each item in record, adding a new line
	after every entry. We have made it str(record) because
	there are a mixture of ints and strs in the data, and 
	we cannot concantanate these together without converting
	everything to a string first ''' 
	print_records = ''
	for record in records:
		print_records += str(record[7]) + " | " + str(record[0]) + " " + str(record[1]) + "\n" + str(record[2]) + "\n" + str(record[3]) + ", " + str(record[4]) + ", " + str(record[5]) + ", " + str(record[6]) + "\n\n" 
	#show results in query label
	query_label = Label(showrecordframe, text=print_records)
	query_label.grid(row=1, column=0, columnspan=2, pady=10, padx=30, ipadx=10, ipady=10, sticky=W)		
	#commit and close db
	conn.commit()
	conn.close()
	#Delete entry box label
	delete_box_label = Label(showrecordframe, text="Select ID to modify: ", fg="white", bg="gray30")
	delete_box_label.grid(row=1, column=2, pady=(30,0), padx=(20, 0), sticky=W)
	delete_box_label.config(font=("Calibri", 13))
	#Entry box to enter ID the user wishes to delete from DB
	global delete_box
	delete_box = Entry(showrecordframe, width=10)
	delete_box.grid(row=1, column=2, padx=(165,0), pady=(30,0), sticky=W)
	#delete button - calls DEF DELETE
	delete_button = Button(showrecordframe, text="Delete Record", command=delete,  fg="white", bg="black")
	delete_button.grid(row=1, column=2, pady=(110,0), padx=(30,0), ipadx=10, ipady=10, sticky=W)
	#edit button - calls DEF EDIT
	edit_button = Button(showrecordframe, text="Edit Record", command=edit, fg="white", bg="black")
	edit_button.grid(row=1, column=2, pady=(110,0), padx=(140,0), ipadx=16, ipady=10, sticky=W)	

#Update record function for SHOW_ALL
def update_record():
	#SQLITE code for updating record
	#connect to database
	conn = sqlite3.connect("patients.db")
	#create cursor
	c = conn.cursor()
	#create record_id var
	record_id = delete_box.get()
	#update records (names on left when table was first created)
	#names on right are new variable
	c.execute("""UPDATE patientstable SET 
		first_name = :first,
		last_name = :last,
		DOB = :dob,
		addressl1 = :addressl1,
		addressl2 = :addressl2,
		addressl3 = :addressl3,
		postcode = :postcode

		WHERE oid = :oid""",
		#designate key value pairs, tell program what these values are
		{
		'first':f_name_edit.get(),
		'last':l_name_edit.get(),
		'dob':dob_edit.get(),
		'addressl1':add_l1_edit.get(),
		'addressl2':add_l2_edit.get(),
		'addressl3':add_l3_edit.get(),
		'postcode':postcode_edit.get(),
		'oid': record_id
		})

	conn.commit()
	conn.close()

#Edit function for SHOW_ALL
def edit():
	#FRAME edit record, using addrecordframe
	addrecordframe = LabelFrame(main, bg="gray30", width=650, height=350)
	addrecordframe.grid(row=3, column=1, pady=10)
	#force width and height on frame
	addrecordframe.grid_propagate(0)

	#Edit record message
	addrecord_label = Label(addrecordframe, fg="white", bg="gray30", text="Editing record ")
	addrecord_label.grid(row=3, column=1, pady=10, padx=(20,0), ipady=4, sticky=W)
	addrecord_label.config(font=("Calibri", 13)) 

	#SQLITE code for editing
	#connect to database
	conn = sqlite3.connect("patients.db")
	#create cursor
	c = conn.cursor()
	#get user input from delete box
	record_id = delete_box.get()
	#run query (select everything that matches user oid input
	c.execute("SELECT * FROM patientstable WHERE oid = " + record_id)

	#fetch all records (assign var)
	records = c.fetchall()

	#make entry boxes global
	global f_name_edit
	global l_name_edit
	global dob_edit
	global add_l1_edit
	global add_l2_edit
	global add_l3_edit
	global postcode_edit

	#entry boxes for edit 
	
	f_name_edit = Entry(addrecordframe, width=30)
	f_name_edit.grid(row=4, column=2, pady=5, padx=5, ipady=2, sticky=W)
	
	l_name_edit = Entry(addrecordframe, width=30)
	l_name_edit.grid(row=4, column=4, pady=5, padx=5, ipady=2, sticky=W)
	
	dob_edit = Entry(addrecordframe, width=15)
	dob_edit.grid(row=5, column=4, pady=5, padx=5, ipady=2, sticky=W)

	add_l1_edit = Entry(addrecordframe, width=30)
	add_l1_edit.grid(row=5, column=2, pady=5, padx=5, ipady=2, sticky=W)
	
	add_l2_edit = Entry(addrecordframe, width=30)
	add_l2_edit.grid(row=6, column=2, pady=5, padx=5, ipady=2, sticky=W)
	
	add_l3_edit = Entry(addrecordframe, width=30)
	add_l3_edit.grid(row=7, column=2, pady=5, padx=5, ipady=2, sticky=W)

	postcode_edit = Entry(addrecordframe, width=30)
	postcode_edit.grid(row=8, column=2, pady=5, padx=5, ipady=2, sticky=W)

	#text box labels
	f_name_label = Label(addrecordframe, fg="white", bg="gray30", text="First Name")
	f_name_label.grid(row=4, column=1, padx=10, pady=5, sticky=E)

	l_name_label = Label(addrecordframe, fg="white", bg="gray30", text="Last Name")
	l_name_label.grid(row=4, column=3, padx=10, sticky=E)

	dob_label = Label(addrecordframe, fg="white", bg="gray30", text="DOB")
	dob_label.grid(row=5, column=3, padx=10, sticky=E)

	add_l1_label = Label(addrecordframe, fg="white", bg="gray30", text="Address Line 1")
	add_l1_label.grid(row=5, column=1, padx=10, pady=5, sticky=E)

	add_l2_label = Label(addrecordframe, fg="white", bg="gray30", text="Address Line 2")
	add_l2_label.grid(row=6, column=1, padx=10, pady=5, sticky=E)

	add_l3_label = Label(addrecordframe, fg="white", bg="gray30", text="City")
	add_l3_label.grid(row=7, column=1, padx=10, pady=5, sticky=E)

	postcode_label = Label(addrecordframe, fg="white", bg="gray30", text="Postcode")
	postcode_label.grid(row=8, column=1, padx=10, pady=5, sticky=E)

	#Save edited record button
	submit_button = Button(addrecordframe, text="Save Record", command=update_record,  fg="white", bg="black")
	submit_button.grid(row=9, column=2, pady=10, padx=20, ipadx=5, ipady=5)
	submit_button.config(font=("Calibri", 12))

	#Insert data into fields 
	for record in records:
		f_name_edit.insert(0, record[0])
		l_name_edit.insert(0, record[1])
		dob_edit.insert(0, record[2])
		add_l1_edit.insert(0, record[3])
		add_l2_edit.insert(0, record[4])
		add_l3_edit.insert(0, record[5])
		postcode_edit.insert(0, record[6])

	#commit and close db
	conn.commit()
	conn.close()

def setup(Program):
	#FRAME for setup
	setupframe = tk.LabelFrame(Program.main, bg="gray30", width=750, height=450, borderwidth=0)
	setupframe.grid(row=3, column=1, pady=10)
	#force width and height on frame
	setupframe.grid_propagate(0)
	#Setup welcome message
	wel_setup = tk.Label(setupframe, fg="white", bg="gray30", text="Setup ")
	wel_setup.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)
	wel_setup.config(font=("Calibri", 16))

	def color():
		#make global so that program can access
		select_color = colorchooser.askcolor()
		select_color.set("blue")
		#call colour window
		select_color = colorchooser.askcolor()
		
	sel_clr_btn = tk.Button (setupframe, text="Set Theme", command=color, borderwidth=0)
	sel_clr_btn.grid(row=7, column=1, padx=20)
	sel_clr_btn.config(font=("Calibri", 13))

 