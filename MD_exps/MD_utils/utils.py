import os 

def create_md_path(label, sys_label=None): 
    """
    create MD simulation path based on its label (int), 
    and automatically update label if path exists. 
    """
    if sys_label: 
        md_path = f'omm_runs_{sys_label}_{label}'
    else: 
         md_path = f'omm_runs_{label}'
    try:
        os.mkdir(md_path)
        return md_path
    except: 
        return create_md_path(label + 1, sys_label=sys_label)


def get_dir_base(file_path): 
    return os.path.basename(os.path.dirname(file_path))

def touch_file(file): 
    """
    create an empty file for bookkeeping sake
    """
    with open(file, 'w'): 
        pass
