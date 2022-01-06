from pprint import pprint
import os

def open_file(path, name_files):
    result = {}
    path = os.path.join(path, name_files)
    with open(path , 'rt', encoding='utf-8') as f:
        result = {
            'data': f.readlines(),
            'name': name_files
        }
    return result

def write_file(path, name_files, data):
    path = os.path.join(path, name_files)
    with open(path , 'wt', encoding='utf-8') as f:
        for v in data:
            for s in v['data']:
                f.write(s)
            f.write('\n')
    return 'Файл записан'

def run_read(path_folder):
    result = []
    for dirs, folder, files in os.walk(path_folder):
        e = []
        for f in files:
            e.append(open_file(path_folder, f))
        break
    result = sorted(e, key=lambda x:len(x['data']))
    
    return result    

def main():
    path_folder_open = os.path.join(os.getcwd(), 'Python', 'task_3')
    path_folder_write = os.path.join(os.getcwd(), 'Python')
    file_write = 'Task_3.txt'
    data = run_read(path_folder_open)
    result = write_file(path_folder_write, file_write, data)
    
    return result

print(main())