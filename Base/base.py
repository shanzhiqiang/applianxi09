import yaml,os

class GetData:

    def get_yml_data(self,yml_name):
        with open("./Data"+os.sep+yml_name,"r",encoding="utf-8") as f:
            return yaml.safe_load(f)