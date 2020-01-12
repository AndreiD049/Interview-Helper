import sys
import os
import random
import glob

def select_n_random_files(n, path, ext=None):
    """
    Selects @n random files from @path, @ext is the desired extension if present
    returns a list of random absolute paths
    """
    #make sure path ends with a separator
    if path[-1] != os.path.sep: path += os.path.sep
    files = glob.glob(path + "*" + (("." + ext) if ext != None else ""))
    return random.sample(files, n) if len(files) > n else files

def select_n_valid_files(validator, n, path, ext=None):
    files = select_n_random_files(n, path, ext)
    valid_results = list(map(validator, files))
    while not all(valid_results):
        # invalidate the file (move to error folder)
        error_fld = os.path.join(path, "error")
        # create error folder if doesn't exist
        if not os.path.exists(error_fld):
            os.mkdir(error_fld)
        
        for idx, r in enumerate(valid_results):
            # move error files to other folder
            if not r:
                error_file = files[idx]
                os.rename(error_file, os.path.join(error_fld, os.path.basename(os.path.normpath(error_file))))
        files = select_n_random_files(n, path, ext)
        valid_results = list(map(validator, files))
    return files

if __name__ == "__main__":
    from validators import ValidatorErrorChecking
    print(select_n_valid_files(ValidatorErrorChecking.validate, 3, r"D:\Interview\data\error_checking", "json"))
