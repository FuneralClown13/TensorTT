import os


class Config:
    path = f'{os.getcwd()}'
    download_dir_name = 'downloads'
    download_dir_path = f'{path}\\{download_dir_name}'

