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

def disp_list(filter='all', max=5):
    tasks = get_list(filter)
    i = 1
    for task in tasks:
        print_task(i, task)
        i += 1
        if i > max:
            print('. . .')
            break
def print_task(idx, task):
    title, date, time = task
    '{lorem:>10}'.format(lorem='Lorem Ipsum')
    print(f'{idx:<2} - {title:<20} {date:<15} {time:<10}')
    

def get_list(filter='all'):
    tasks = []
    with open('tasks.csv', 'r') as f:
        for line in f.readlines():
            line = line.strip()            #clear new line char '\n'
            task = line.split(',')        #give me a list
            tasks.append(task)            # add it to my list tasks=(list of list)
    return tasks

def new():
    print()
    print('='*20,'Add new task', '='*20)
    
    while True:
        title = input('Title[20] >> ')
        title = title.substring[0,20]    #clip to length 20
        
        if title == '':
            break;
            
        date = input('Date[today] >> ')

        if date == '':
            date = 'today'
            
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