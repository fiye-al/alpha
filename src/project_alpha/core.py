import yaml
from project_alpha.data_processing import process_data
from project_alpha.models.model import train_model

def main():
    print("Project Alpha core running")
    cfg = yaml.safe_load(open('config/config.yaml'))
    df = process_data(cfg['data_path'])
    train_model()
