import yaml

data = {"list":["我是谁",1,1.2]}

with open("./lianxi.yml","a",encoding="utf-8") as f:
    yaml.safe_dump(data,f,encoding="utf-8",allow_unicode=True)