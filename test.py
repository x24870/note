import os, errno, shutil

DEST_DIR_NAME = 'migrated_packages'

def mkdir_p(path):
    try:
        os.mkdir('migrate')
    except OSError as excp:
        if excp.errno == errno.EEXIST and os.path.isdir():
            pass
        else:
            raise

def copy_package(package_name):
    #package_name will be FP1, FP2 or NIC
    print('Copy %s packages...', package_name)

    os.chdir(os.path.join('.', os.path.join(package_name, 'package')))
    current_dir = os.getcwd()

    file_list = os.listdir()
    dest_path = '../' + DEST_DIR_NAME
    for f in file_list:
        shutil.copy(os.path.join(current_dir, f), os.path.join(dest_path, f))

    os.chdir('..')
    os.chdir('..')

def migrate():
    print('Creating "%s" directory...' % DEST_DIR_NAME)
    mkdir_p(DEST_DIR_NAME)

    copy_package('FP1')
    copy_package('FP2')
    copy_package('NIC')

    print('Done')

if __name__ == '__main__':
    migrate()