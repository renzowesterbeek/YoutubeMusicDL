# Declaration of functions used in console and ui version of the app
# App by Renzo Westerbeek - 2015

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise