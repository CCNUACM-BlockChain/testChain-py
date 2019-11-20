import sys

configDict = None

def initConfig():
    configFileName = sys.argv[1]
    with open(configFileName,'r') as configFile:
        configFileContent = configFile.read()
        global configDict
        configDict = {}
        exec(configFileContent,configDict,configDict)

def loadConfig(name: str):
    if configDict is None:
        initConfig()
    return configDict[name]