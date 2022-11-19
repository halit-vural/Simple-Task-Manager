# Task Manager Project
 Simple Python project for beginners. This repo explains the project development steps to learners.
 
 The running version can be seen on Replit:
 https://replit.com/@HalitVural1/Simple-Task-Manager?v=1 
 
 
# Title: Task Manager (TM)
**Developer:** Halit Vural
October 2022
## 1. Introduction
Users can enter TO-DO tasks with date and time. Task Manager (TM) will store notes as a TO-DO list and it will list the tasks when requested.
Users can cancel the selected task. Users can delete the task or mark it as completed. TM may list completed tasks on another screen. It can list the d-day of the task in the tasks screen. TM will have a focus screen where it lists only today’s tasks. It can order the tasks according to priority level and time. Users can delay a task until tomorrow by selecting the ‘delay’ command. Users can also delay the task to a specific date.
## 2. Requirements Analysis
We will use the MoSCoW method to analyze and group our requirements.
1. Must-have Requirements
- Users can enter TO-DO tasks with date and time.
- It will store notes as a TO-DO list in a file.
- It will list the tasks on the home screen.
- Users can mark as completed.
- User can delete the task

## 2. Should-have Requirements
- Users can delay a task until tomorrow by selecting the ‘delay’ command.
- It will have a focus screen where it lists only today’s tasks.
- Users can cancel the selected task.
- It can list completed tasks on another screen.
- It can order the tasks according to priority level and time.
## 3. Could-have Requirements
- Users can delay the task to a specific date.
- It will warn users for past due tasks.
- It can list the d-day of the task in the tasks screen.
## 4. Won’t-have Requirements
- Users can group the tasks in different epics/stories.
## 3. Screen Designs
### Home Screen:

```
================== Task Manager ==================
1 - Laundry                                         3pm          Today
2 - Car wash                                       1pm          Tomorrow
3 - Car maintenance	                        2pm	     12-December-2022

(N)ew (C)omplete  (#)Cancel  (F)ocus  (L)deLay  (Q)uit
(S)how completed  (X)NeXt Page (P)revious Page

>>_
```
        

### New Task Screen:
```
Add a new task:
Title [20] >> Car maintenance
Date [now] >> 12/12/2022
Time [now] >>2pm

New task added:
Car maintenance		2pm 		12/December/2022
Enter new? [Y/n] >>

Add a new task:
Title [20] >> Laundry
Date [now] >>
Time [now] >>

New task added:
Laundry 			3pm		Today

Enter new? [Y/n] >>n

```

→ This page will return to the home screen when finished.





We will complete the must-have requirements one by one. When all of them are implemented, we will deploy it as version 1.0. The version number will increase after each requirement is implemented and the version is deployed.

## Version 0.1.0: User can enter TO-DO tasks with date and time.

So let’s begin with the home screen and adding a new task.

Complete code will be like:

```
def disp_main_screen():
	print('''
	================== Task Manager ==================
	''')
	list_tasks()
	list_commands()

def list_tasks():
	print('''
	1 - Laundary	3pm	Today
	2 - Car wash	1pm	Tomorrow''')

def list_commands():
	print('''
	(N)ew (C)omplete  (#)Cancel  (F)ocus  (L)deLay  (Q)uit
	(S)how completed  (X)NeXt Page (P)revious Page''')
	print('>>>', end=' ')

def new_task():
	print('new task')
	
def	complete_task():
	print('complete task')

def cancel_task():
	print('cancel task')

def clear_screen():
	print('''  
	   ''' *30)
	   
def main():
	cmd = ' '
	while cmd != 'Q':
		clear_screen()
		disp_main_screen()
		cmd = input()
		cmd = cmd.upper()
		if cmd == 'N':
			new_task()
		elif cmd == 'C':
			complete_task()
		elif cmd == '#':
			cancel_task()
		elif cmd == 'Q':
			print('Goodbye.')
		else:
			print('The command not available.')
	

main()  # this line will run all the program

```


## Version 0.1.1: 
Defines the new task screen function.

### New Task Screen:
```
Add a new task:
Title [20] >> Car maintenance
Date [now] >> 12/12/2022
Time [now] >>2pm

New task added:
Car maintenance 	2pm	12/December/2022
Enter new? [Y/n] >>

Add a new task:
Title [20] >> Laundry
Date [now] >>
Time [now] >>

New task added:
Laundry 	3pm	Today

Enter new? [Y/n] >>n

```

→ This page will return to the home screen when finished.


## Version 0.2.0: System will store notes as a TO-DO list in a file. 
The file is written in csv format. Each value will be separated with a comma.


## Version 0.3.0: System will list the tasks on the home screen
Now the program can read and list the tasks on screen. It uses a for loop to read the lines from the file.


## Version 0.4.0: Users can mark selected task as completed
We added a new column to store the status of the task. When the task assigned as completed, the status will change to completed. When a new task is added, the status will be new.

At this point, we need to add an index column (id) to the tasks file. That index will help us select the related task and update its status. So, new task will apply indexes to added tasks from the beginning.

## Version 1.0: Users can delete the selected task
With this requirement completion, we can publish our first version of the application.


