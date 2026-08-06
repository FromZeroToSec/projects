from datetime  import datetime


def write_log (message, level):
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    with open('app.log', 'a') as f:
        f.write(f'[{formatted_time}] [{level}] {message}\n')

if __name__ == '__main__':
    write_log('Hello world', 'INFO')