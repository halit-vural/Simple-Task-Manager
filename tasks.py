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

def list(filter='all', max=15):
    with open('tasks.csv', 'r') as f:
        i = 1
        for line in f.readlines():
            print(i,'-', line)
            i += 1
            if i > max:
                print('. . .')
                break

def new():
    print()
    print('='*20,'Add new task', '='*20)
    
    while True:
        title = input('Title[20] >> ')

        if title == '':
            break;
            
        date = input('Date[now] >> ')

        if date == '':
            date = 'now'
            
        time = input('Time [now] >> ')

        if time == '':
            time = 'now'

        print()
        print('New task added:')
        print(title, time, date)

        with open('tasks.csv', 'a') as f:
            f.write(title + ',' + date + ',' + time + '\n')
        print()
        new = input('Enter new? [Y/n]>> ')
        if new == 'n' or new == 'N':
            break
        
def	complete():
	print('complete task')

def cancel():
	print('cancel task')