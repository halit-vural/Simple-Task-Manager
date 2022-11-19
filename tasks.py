

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
        add(new_task)
        
        print()
        print('New task added:')
        print(title, time, date)
        print()
        # new = input('Enter new? [Y/n]>> ')
        # if new == 'n' or new == 'N':
        #     break
        
        return new_task
        
def	complete(tasks, id):
    print('complete task: ', id)
    task = get_task(tasks, id)
    print('task:', task)
    if task:
        status = task[-1]
        if status == 'completed':
            new_status = 'new'        #toggle status
        else:
            new_status = 'completed'
    
        task[-1] = new_status
    
        if find_replace(tasks, task):
            print('replaced..')
            update_in_file(tasks)
    else:
        print('Task not found..')
    return tasks

def is_completed(task):
    s = get_status(task)
    return s == 'completed'

def get_status(task):
    return task[-1]
    
def find_replace(data, new):
    print('find replace...')
    found = False
    for idx in range(len(data)):
        task = data[idx]
        id = task[0]
        # print(id)
        if new[0] == id:
            found = True
            # print('you found it!')
            data[idx] = new
    if not found:
        print('Nothing to change..')
        return False
    return True            
            

def get_id(task):
    return task[0]

def get_task(tasks, id):
    for task in tasks:
        if task[0] == id:
            return task
    return None

def add(task):
    # print('writing..', task)
    idx, title, date, time, status = task
    with open('tasks.csv', 'a') as f:
            f.write(idx + ',' + title + ',' + date + ',' + time + ',' + status + '\n')
  
def update_in_file(tasks):
    '''Find the task in the file and write the new data'''
    print('writing into file...')
    with open('tasks.csv', 'w') as f:
        for task in tasks:
            print(task)
            idx, title, date, time, status = task
            f.write(f'{idx},{title},{date},{time},{status}\n')
      

def cancel(tasks, id):
    print('cancel task: ', id)
    task = get_task(tasks, id)
    print('task:', task)
    if task:
        print('delete:', task)
        tasks.remove(task)
        update_in_file(tasks)
    else:
        print('Task not found..')
    return tasks