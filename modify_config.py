import yaml
import os

yaml_file=open('src/configs/model/segmentor_model/sam.yaml','r')
d=yaml.safe_load(yaml_file)
d['sam']['checkpoint_dir'] = os.getcwd() + "/datasets/bop23_challenge/pretrained/segment-anything"
yaml_file.close()
os.remove('src/configs/model/segmentor_model/sam.yaml')

yaml_file = open('src/configs/model/segmentor_model/sam.yaml', 'w')
yaml.dump(d, yaml_file, default_flow_style=False, sort_keys=False)
yaml_file.close()
