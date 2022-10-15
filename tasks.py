''' 
Screen:

Add a new task:
Title [20] >> Car maintenance
Date [now] >> 12/12/2022
Time [now] >>2pm

New task added:
Car maintenance		2pm 		12/December/2022
Enter new? [Y/n] >>

Add a new task:
Title [20] >> Laundry

'''

def new():
    print('='*20,'Add new task', '='*20)
    
    while True:
        title = input('Title[20] >> ')
        date = input('Date[now] >> ')
        time = input('Time [now] >> ')

        print('New task added:')
        print(title, time, date)

        with open('tasks.csv', 'a') as f:
            f.write(title + ',' + time + ',' + date + '\n')
        new = input('Enter new? [Y/n]>>')
        if new == 'n' or new == 'N':
            break
        
def	complete():
	print('complete task')

def cancel():
	print('cancel task')