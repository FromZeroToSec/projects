from datetime  import datetime


def write_log(message, level):
    allowed_levels = ["INFO", "WARNING", "ERROR"]
    if level in allowed_levels:
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open('app.log', 'a') as f:
            f.write(f'[{formatted_time}] [{level}] {message}\n')
    else:
        print('Invalid log level')




if __name__ == '__main__':
    write_log('Hello world', 'INFO')

