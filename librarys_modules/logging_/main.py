import logging
import requests

# конфиг для логгера
logging.basicConfig(level=logging.DEBUG)
# создание логгера
logger = logging.getLogger()
logging.getLogger('urllib3').setLevel('FATAL')


# проверить какие логгеры были использованы
# for key in logging.Logger.manager.loggerDict:
#     print(key)

def main(name):
    logger.debug(f'Enter in the main() function: {name=}')

    r = requests.get('https://www.google.ru')


if __name__ == '__main__':
    main('harlok13')
