from datetime  import datetime
import os 

def write_log(message, level):
    allowed_levels = ["INFO", "WARNING", "ERROR"]
    if level in allowed_levels:
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open('app.log', 'a') as f:
            f.write(f'[{formatted_time}] [{level}] {message}\n')
    else:
        print('Invalid log level')


def get_logs_size():
    size = os.path.getsize('app.log')
    return size

if __name__ == '__main__':
    write_log('Hello world', 'INFO')
    print(get_logs_size())

