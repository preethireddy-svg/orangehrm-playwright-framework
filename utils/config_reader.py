import yaml

class ConfigReader:
    def __init__(self, config_path="config/config.yaml"): #constructor
        with open(config_path, "r") as file: # opens config file in readable mode, with ensures autoclose
            self.data = yaml.safe_load(file) # Here it converst yaml file to Pythin format and stores in self.data

    def get(self, key):
        return self.data.get(key) # used to fetch values from self.data like config.get("url") and it returns url