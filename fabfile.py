from fabric.api import run, sudo, task,put,get,cd, prefix
from fabric.api import local
from fabric.api import env
from datetime import datetime

env.hosts =["159.203.177.196"]
env.user="dario"
env.password="chilechile"
DATABASE="project_web"
BACKUP_FOLDER='descargas/'
#poner la bandera en la ejecucion
# fab -H 159.203.177.196 show_dir

# cambio de usuario
# fab -H 159.203.177.196 show_dir --user=dario

def show_dir():
    sudo('ls')

def create_folder(folder):
    run(f'mkdir {folder}')

def delete_folder(folder):
    sudo('rm -rf {}'.format(folder))

@task
def pull():
    run('cd proyecto_flask && git pull')
@task
def deploy():
    with cd('proyecto_flask'):
        pass
@task
def upload_txt_file():
    put(
        local_path='example.txt',
        remote_path='./proyecto_flask'
    )
@task
def get_txt_file(file):
    get(
        local_path='./descargas',
        remote_path='./proyecto_flask/{}'.format(file)
    )
@task
def install_requirements():
    # run('cd proyecto_flask && source env/bin/activate && pip install -r requirements.txt')
    with cd('proyecto_flask'):
        with prefix('source env/bin/activate'):
            run('pip install -r requirements.txt')
@task
def show_dir_local():
    local('dir')

def get_backup_name(database):
    return '{}_{}.sql'.format(database,datetime.now().strftime("%d_%m_%Y"))

def get_backup(backup):
    get(
        remote_path=backup,
        local_path=BACKUP_FOLDER
    )

def delete_backup(backup):
    sudo('rm {}'.format(backup))

def load_backup(backup_path):
    local('mysql -u root --password=tritubot2018 -e "DROP DATABASE {}"'.format(DATABASE))
    local('mysql -u root --password=tritubot2018 -e "CREATE DATABASE {}"'.format(DATABASE))
    local('mysql -u root --password=tritubot2018 {} < {}'.format(DATABASE,backup_path))
 
@task
def backup():
    backup_name = get_backup_name(DATABASE)
    run('mysqldump -u dario --password=chilechile {} > {}'.format(DATABASE,backup_name))
    get_backup(backup_name)
    backup_path = '{}{}'.format(BACKUP_FOLDER,backup_name)
    #load_backup(backup_path)
    delete_backup(backup_name)