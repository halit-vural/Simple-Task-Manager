

def get_list(filter='all'):
    tasks = []
    with open('tasks.csv', 'r') as f:
        for line in f.readlines():
            line = line.strip()            #clear new line char '\n'
            task = line.split(',')         #give me a list
            tasks.append(task)             #add it to my list tasks=(list of list)
    return tasks

def new(new_idx):
    ''' 
        Add a new task:
        Title [20] >> Car maintenance
        Date [now] >> 12/12/2022
        Time [now] >>2pm
        
        New task added:
        Car maintenance		2pm 		12/December/2022
    '''
    print()
    print('='*20,'Add a new task', '='*20)
    
    title = input('Title[30] >> ')
    title = title[0:30]    #clip to length
    
    if title != '':        
        date = input('Date[today] >> ')
    
        if date == '':
            date = 'today'
            
        time = input('Time [now] >> ')
    
        if time == '':
            time = 'now'
    
        new_idx = str(new_idx)
        status = 'new'
        new_task = [new_idx, title, date, time, status]
        write(new_task)
        
        print()
        print('New task added:')
        print(title, time, date)
        print()
        # new = input('Enter new? [Y/n]>> ')
        # if new == 'n' or new == 'N':
        #     break
        
        return new_task
        
def	complete(tasks, idx):
    task = tasks[idx]
    status = task[-1]
    if status == 'completed':
        new_status = 'new'        #toggle status
    else:
        new_status = 'completed'

    task[-1] = new_status

    update(tasks)
    return task

def write(task):
    print(task)
    new_idx, title, date, time, status = task
    with open('tasks.csv', 'a') as f:
            f.write(new_idx + ',' + title + ',' + date + ',' + time + ',' + status + '\n')
  
def update(tasks):
    '''Find the task in the file and write the new data'''
    print('writing into file...')
    with open('tasks.csv', 'w') as f:
        for task in tasks:
            print(task)
            idx, title, date, time, status = task
            f.write(idx + ',' + title + ',' + date + ',' + time + ',' + status + '\n')
      

def cancel():
	print('cancel task')