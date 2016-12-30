from api import app
from yaml import load

config_file = open('conf/config.yaml', 'r')
conf = load(config_file)


if __name__ == '__main__':
    app.run(
        host=conf['server']['address']['host'],
        port=conf['server']['address']['port'],
        debug=conf['server']['debug'],
        workers=conf['server']['workers'])
