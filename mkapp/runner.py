import os

def get_app_root(app_name):
  found = False
  try:
    os.mkdir(app_name)
  except FileExistsError:
    found = True
    
  return os.path.abspath(app_name), found
  
def make_app_folder_structure(app_folder, app_name):
  os.mkdir("{}/bin".format(app_folder))
  os.mkdir("{}/{}".format(app_folder, app_name))
  os.mkdir("{}/data".format(app_folder))
  os.mkdir("{}/tests".format(app_folder))
  
  
def init_package(pkg_folder):
  init_file = open("{}/__init__.py".format(pkg_folder),"w+")
  runner_file = open("{}/runner.py".format(pkg_folder),"w+")
  
def make_app_files(app_folder, app_name):
  with open("{}/README.md".format(app_folder),"w+") as f:
    f.write("# {}".format(app_name))
  
  f_git_ignore = open("{}/.gitignore".format(app_folder),"w+")
  
  
  
def mk_pkg(app_folder, app_name, pkg_name):
  pkg_folder = "{}/{}/{}".format(app_folder, app_name, pkg_name)
  os.mkdir(pkg_folder)
  return pkg_folder

def create_app(app_folder, app_name):
  make_app_folder_structure(app_dir, app_name)
  make_app_files(app_dir, app_name)
  init_package("{}/{}".format(app_folder,app_name))
  
  

def create_pkg(app_folder, app_name, pkg_name):
  pkg_folder = mk_pkg(app_folder, app_name, pkg_name)
  init_package(pkg_folder)
    
if __name__ == "__main__":
    app_name = input("App name?\n")
    app_dir, found = get_app_root(app_name)
    if found:
      print('Found app at {}'.format(app_dir))
    else:
      print('Created app folder at {}'.format(app_dir))
    mode = int(input("1) Create App\n2)Create submodule\n"))
    if mode == 1:
      print("Create app")
      create_app(app_dir, app_name)
    if mode == 2:
      pkg_name = input("Package name:\n")
      create_pkg(app_dir, app_name, pkg_name)
      
      
